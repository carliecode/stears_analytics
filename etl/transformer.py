import pandas as pd
import config.app_config as cfg

logger = cfg.get_logger()

def set_data_rules(data: pd.DataFrame) -> pd.DataFrame:
    try:
        logger.info("Setting data transformation rules.")
        data['close_date'] = pd.to_datetime(data['close_date'])
        data['engage_date'] = pd.to_datetime(data['engage_date'])
        name_filter = data['sales_agent'].str.contains('darcel|kami|jonathan', case=False)
        data = data[name_filter]
        date_filter = data['close_date'].dt.year == 2017
        data = data[date_filter]
        logger.info("Data rules set successfully.")
        return data
    except Exception as e:
        logger.error(f"Error formatting data: {e}")
        raise

def group_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        logger.info("Starting to group data.")
        data = data.groupby(['product', 'deal_stage']).size().reset_index(name='count')
        data = data.sort_values(by='count', ascending=False).head(5)
        logger.info("Data grouped successfully.")
        return data
    except Exception as e:
        logger.error(f"Error filtering data: {e}")
        raise
        

def transform(data: pd.DataFrame) -> None:
    try:
        logger.info("Execution of transformation module has started.")
        data = set_data_rules(data)
        data = group_data(data)
        data.to_csv('.\data\grouped_data.csv', index=False)
        logger.info("Transformation module finished successfully.")
    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
        raise