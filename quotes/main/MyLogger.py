import logging, inspect

class MyLogger:
    logger: logging.Logger = None
    
    @staticmethod
    def configure():
        FORMAT = '%(asctime)s ; %(name)s ; %(message)s ; %(clientip)s'
        # logging.basicConfig(format=FORMAT)
        logger_name = inspect.stack()[1][3]
        handler = logging.FileHandler('app.log', 'a', 'utf-8')
        logger = logging.getLogger('Web Quotes')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
        MyLogger.logger = logger