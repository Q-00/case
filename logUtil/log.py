import logging

class loggr:
    def log(self):
        logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(message)s-%(funcName)s')
        self.log = logging.getLogger(__name__)
        self.log.info('start log')

        return self.log