import config.app_config as cfg
import etl.extractor as extractor
import etl.transformer as transformer
import etl.loader as loader
import os

logger = cfg.get_logger()


if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')  
    logger.info('**********************************************************')  
    logger.info('======================Program Starts======================')
    data = extractor.extract()
    transformer.transform(data)
    loader.load()
    logger.info('======================Program Ends======================')
    logger.info('**********************************************************')  
    print('The progra has ended')
    exit()
  
