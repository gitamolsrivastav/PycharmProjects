import logging
import inspect

def customLogger(logLevel):

    # get the name of the class/method from which this method is logged

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode= 'w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger








