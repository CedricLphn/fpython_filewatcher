import logging


def handle_log_cases(case, text="", filename='/logs/fw.log'):
    """Custom switch for returning the right method from logging lib
    :args: case, text(optional), filename(optional)
    :return: logging method
    """
    if case == 'set':
        return logging.basicConfig(filename=filename, level=logging.DEBUG)

    if case == 'debug':
        return logging.debug(text)

    if case == 'info':
        return logging.info(text)

    if case == 'warning':
        return logging.warning(text)

    if case == 'critical':
        return logging.critical(text)