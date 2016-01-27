#!/usr/bin/env python
import os
import logging

import config


def convert_plist_file():
    plist_file_path = os.path.realpath(args.plist_file_path)
    logger.info(plist_file_path)
    logger.debug(config.OUTPUT_DIRECTORY)


if __name__ == '__main__':
    args = config.parse_args()

    logging.basicConfig(filename=config.LOGGING_FILE, level=config.LOGGING_LEVEL)
    logger = logging.getLogger(__name__)

    convert_plist_file()
