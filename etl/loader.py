import pandas as pd
import config.app_config as cfg
import matplotlib.pyplot as plt

logger = cfg.get_logger()

def load_data() -> pd.DataFrame:
    try:
        logger.info("Starting to load chart data from CSV file.")
        df = pd.read_csv('.\data\grouped_data.csv')
        logger.info("Chart data is loaded successfully.")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def create_chart(data: pd.DataFrame) -> None:
    try:
        logger.info("Starting to create chart.")
        print(data)
        if data.empty:
            logger.warning("Data is empty. No chart will be created.")
            return
        data = data.pivot(index='product', columns='deal_stage', values='count')
        data.plot(kind='bar', stacked=True)
        plt.title('Top 5 Products by Deal Stage')
        plt.xlabel('Product')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('chart.png')
        plt.close()
        logger.info("Chart created and saved successfully.")
    except Exception as e:
        logger.error(f"Error creating bar chart: {e}")
        raise

def load() -> None:
    try:
        logger.info("Execution of load module has started.")
        data = load_data()
        create_chart(data)
        logger.info("Load module execution finished successfully.")
    except Exception as e:
        logger.error(f"Error during execution: {e}")
        raise