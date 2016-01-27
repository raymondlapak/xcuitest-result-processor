import argparse
import logging
import os

# Path to an output directory where the results of the conversion will be stored,
# either relative to .plist file location, or absolute.
OUTPUT_DIRECTORY = 'converted-result'

# Level of logging statements to be saved in logging file
LOGGING_LEVEL = logging.INFO

# Path to a logging file
LOGGING_FILE = 'plist-processor.log'


def parse_args():
    """
    Parse command-line arguments
    :return: parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('plist_file_path', help='Path to a .plist file with XCUITest execution results')
    parser.add_argument('-o', '--output-dir', help='Path to an output directory to store conversion results')
    parser.add_argument('-ll', '--logging-level', help='Level of script logging')
    parser.add_argument('-lf', '--logging-file', help='Logging file path')
    args = parser.parse_args()
    set_args(args)
    return args


def set_args(args):
    """
    Update default settings with command-line arguments
    :param args: parsed command-line arguments
    """
    if args.logging_level:
        global LOGGING_LEVEL
        level = logging.getLevelName(args.logging_level.upper())
        if type(level) is int:
            LOGGING_LEVEL = level
        else:
            logging.warn('Logging level not updated, invalid value provided')
    if args.logging_file:
        set_logging_file(args.logging_file)
    if args.output_dir:
        global OUTPUT_DIRECTORY
        OUTPUT_DIRECTORY = args.output_dir


def set_logging_file(logging_file):
    """
    Update default LOGGING_FILE value with the provided argument
    :param str logging_file: path to the logging file
    """
    global LOGGING_FILE
    log_dir = os.path.dirname(os.path.realpath(logging_file))
    print log_dir
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except os.error:
            logging.warn('Couldn\'t create logging directory %s, --logging-file argument ignored, '
                         'default logging file is used' % log_dir)
            return
    try:
        with open(logging_file, 'a'):
            pass
        LOGGING_FILE = logging_file
    except IOError:
        logging.warn('Couldn\'t create logging file %s, --logging-file argument ignored, '
                     'default logging file is used' % logging_file)