from loguru import logger
from config.read_env import *
from distutils.util import strtobool

if __name__ == "__main__":

    if strtobool(coba_aja):
        logger.info("Coba_Aja: {} ", coba_aja)
        logger.info("My_Config: {}", my_config)
    
    logger.info("My message: Hello") 
    print("Hello World")