import os
from io import StringIO
import config.app_config as app
import pandas as pd
from minio import Minio
from concurrent.futures import ThreadPoolExecutor

logger = app.get_logger()

def load_file(client: Minio, bucket_name: str, file_name: str) -> pd.DataFrame:
    df = pd.DataFrame()
    try:
        logger.info(f"Attempting to load file: {file_name} from bucket: {bucket_name}")
        file = client.get_object(bucket_name=bucket_name, object_name=file_name)
        file_data = file.read().decode('utf-8')

        if file_name.lower().endswith('.csv'):
            df = pd.read_csv(StringIO(file_data))
            logger.info(f"Successfully loaded CSV file: {file_name}")
        elif file_name.lower().endswith('.json'):
            df = pd.read_json(StringIO(file_data))
            logger.info(f"Successfully loaded JSON file: {file_name}")

        return df
    except Exception as e:
        logger.error(f"Failed to load file: {file_name} from bucket: {bucket_name}, Error: {e}")
        raise


def read_files_from_minio_bucket(client: Minio, bucket_name: str) -> pd.DataFrame:
    df = pd.DataFrame()
    try:
        logger.info(f"Listing objects in bucket: {bucket_name}")
        
        csv_file_object_names = [csv_file.object_name for csv_file in client.list_objects(bucket_name) if str.lower(csv_file.object_name).endswith('.csv')]
        json_file_object_names = [json_file.object_name for json_file in client.list_objects(bucket_name) if str.lower(json_file.object_name).endswith('.json')]
        
        logger.info(f"Found {len(csv_file_object_names)} CSV files and {len(json_file_object_names)} JSON files in bucket: {bucket_name}")

        if csv_file_object_names:
            logger.info("Loading CSV files")
            with ThreadPoolExecutor() as execs:
                dfs_csv = list(execs.map(lambda file_name: load_file(client, bucket_name, file_name), csv_file_object_names))
                if dfs_csv:
                    df = pd.concat([df] + dfs_csv)

        if json_file_object_names:
            logger.info("Loading JSON files")
            with ThreadPoolExecutor() as execs:
                dfs_json = list(execs.map(lambda file_name: load_file(client, bucket_name, file_name), json_file_object_names))
                if dfs_json:
                    df = pd.concat([df] + dfs_json)


        logger.info("Successfully loaded all files from bucket")
        return df
    except Exception as e:
        logger.error(f"Failed to read files from bucket: {bucket_name}, Error: {e}")
        raise

def extract() -> pd.DataFrame:
    try:
        logger.info("Execution of extraction module has started")

        endpoint = '127.0.0.1:9091'
        access_key = os.getenv('MINIO_ACCESS_KEY', 'minioadmin')
        secret_key = os.getenv('MINIO_SECRET_KEY', 'minioadmin')
        bucket_name = 'stears'

        client = Minio(
            endpoint=endpoint, 
            access_key=access_key, 
            secret_key=secret_key, 
            secure=False
        )

        df = read_files_from_minio_bucket(client=client, bucket_name=bucket_name)
        logger.info("Execution of extraction module has completed successfully")
        return df
    except Exception as e:
        logger.error(f"An error occurred during the data extraction process in function 'execute': {e}")
        raise

if __name__ == '__main__':
    execute()