import logging

logger = logging.getLogger(__name__)


def setup_log_config():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s : %(levelname)-8s : [%(filename)s : %(lineno)d] : %(message)s'
    )
