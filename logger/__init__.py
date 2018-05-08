import logging
import os

log_handler = logging.StreamHandler()
try:
    log_level_name = os.environ['LOG_LEVEL']
except:
    log_level_name = 'INFO'
log_level = logging.getLevelName(log_level_name)
log_handler.setLevel(log_level)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))


c_logger = logging.getLogger('EduCerts')
c_logger.addHandler(log_handler)
c_logger.setLevel(log_level)
c_logger.info('logger is initialized for %s' % (os.environ.get('HEROKU')))
