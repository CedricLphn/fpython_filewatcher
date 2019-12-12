import logging


class Logs:
    def __init__(self, ):
        self.logger = None

    def handle_log_cases(case, text="", filename='/logs/fw.log', self=None):
        """Custom switch for returning the right method from logging lib
        :args: case, text(optional), filename(optional)
        :return: logging method
        """
        if case == 'set':
            # Gets or creates a logger
            self.logger = logging.getLogger(filename)
            self.logger.setLevel(logging.WARNING)

            file_handler = logging.FileHandler(filename)
            formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        if case == 'debug':
            self.logger.debug(text)

        if case == 'info':
            self.logger.info(text)

        if case == 'warning':
            self.logger.warning(text)

        if case == 'critical':
            self.logger.critical(text)
