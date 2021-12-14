import logging

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


class TLogger():
    """
    T(EASE)Logger : Wrapper class for Standard Python logger with some presets for TEASE,
                    to help down on code duplication and enforce project wide standards

    Parameters:
        name        : Name of the Logger
        infoLevel   : logging level of the Logger (e.g. logging.DEBUG/INFO/WARNING/ERROR)
        fileHandler : string file path to the file handler log file (e.g. /logs/xyz.log)
    """

    def __init__(self, name: str, infoLevel=logging.INFO, fileHandler=None):
        try:
            if name is None:
                raise ValueError("Name argument not specified")

            logformat = '%(asctime)s %(levelname)s [%(name)s %(funcName)s] %(message)s'
            self.logformat = logformat
            self.name = name.upper()
            self.logger = logging.getLogger(self.name)
            self.logger.setLevel(infoLevel)

            self.add_consolehandler(infoLevel, logformat)

        except Exception as e:
            if self.logger:
                self.logger.error(str(e))

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)

    def setLevel(self, infoLevel):
        # Python's standard Logging has lots of design issues, especially with its API and expected behaviours
        # To dynamically reset the loglevel, you need to also change the parent levels as well as all handlers!
        self.logger.parent.setLevel(infoLevel)
        for handler in self.logger.parent.handlers:
            handler.setLevel(infoLevel)

        self.logger.setLevel(infoLevel)
        for handler in self.logger.handlers:
            handler.setLevel(infoLevel)

        return self.logger.level

    def add_consolehandler(self, infoLevel=logging.INFO,
                           logformat='%(asctime)s %(levelname)s [%(name)s %(funcName)s] %(message)s'):
        sh = logging.StreamHandler()
        sh.setLevel(infoLevel)

        formatter = logging.Formatter(logformat)
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)



