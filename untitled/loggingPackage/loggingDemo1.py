import logging
import logging.config
import loggingPackage.custom_logger as cl

"""logging.basicConfig(format = '%(asctime)s: %(levelname)s : %(message)s',filename = "test.log",
                    datefmt = '%m/%d/%Y %H:%M:%S', level = logging.DEBUG)
logging.debug("print the debug level")
logging.warning("print the warning message")"""

class LoggerDemo():

    def testLog(self):

        #create logger and set log level
        logging.config.fileConfig('logging.conf') #  set the config file
        logger = logging.getLogger(LoggerDemo.__name__) #create logger
        logger.setLevel(logging.DEBUG)   # set log level

        #create handler and set level

        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")

    def customlogTest(self):
        log = cl.customLogger(logging.DEBUG)
        log.debug("Tracing the logs to debug level")
        log.warning("tracing the logs to warning level")



demo = LoggerDemo()
demo.testLog()
demo.customlogTest()








