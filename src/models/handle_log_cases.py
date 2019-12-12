import logging
import time


def follow(thefile):
    thefile.seek(0, 2)  # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        yield line


def handle_log_cases(case, text="", filename='/logs/fw.log'):
    """Custom switch for returning the right method from logging lib
    :args: case, text(optional), filename(optional)
    :return: logging method
    """
    if case == 'set':
        return logging.basicConfig(filename=filename, level=logging.DEBUG)

    if case == 'debug':
        follow(filename)
        return logging.debug(text)

    if case == 'info':
        follow(filename)
        return logging.info(text)

    if case == 'warning':
        follow(filename)
        return logging.warning(text)

    if case == 'critical':
        follow(filename)
        return logging.critical(text)
