from python_utils.logging import logging
import argparse

# Create logger
logger = logging.init_logger()

def parse_args():
    '''
    Description: Parses command line arguments

    Args: None

    Returns:
        args: parsed arguments
    '''
    logger.info("Parsing args")

    parser = argparse.ArgumentParser(
        description="Run application with specific config source"
    )

    parser.add_argument('-s', '--source', type=str, choices=['container', 'env'], default='env',
                        help='The source to fetch configs from (container or env). Default is env.'
    )

    # Parse arguments
    args = parser.parse_args()

    logger.info('Returning parsed args')

    return args