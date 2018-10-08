import logging
import logstash
import sys

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(logstash.LogstashHandler('52.14.57.246', 5959, version=1))

logger.debug("This is a test debug message.")
logger.info("This is a test info message.")
logger.warning("This is a test warning message.")
logger.error("This is a test error message.")
logger.critical("This is a test critical message.")

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
logger.info('python-logstash: test extra fields', extra=extra)
