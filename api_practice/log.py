import logging


class LoggerConfig:
    logging.basicConfig(filename=r'D:\py\pycharmProjects\api\log_msg.log',
                        filemode='a',
                        level=logging.INFO,
                        format='%(levelname)-8s : %(asctime)s : [%(filename)s : %(lineno)d] : %(message)s')
    logger = logging.getLogger()