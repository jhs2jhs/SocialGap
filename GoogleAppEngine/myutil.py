import logging

logging.getLogger().setLevel(logging.DEBUG)

def debug(msg):
    logging.debug('DEBUG:'+str(msg))
