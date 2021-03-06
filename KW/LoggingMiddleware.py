from django.utils.deprecation import MiddlewareMixin
from rest_framework_tracking.mixins import LoggingMixin
import logging
logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        import traceback
        print(traceback.format_exc())

    def handle_log(self):
        self.log['response'] = None
        logger.info(self.log)


class RequestAndResponseLoggingMixin(LoggingMixin):
    pass


class RequestLoggingMixin(LoggingMixin):
    def should_log(self, request, response):
        return response.status_code // 100 == 2 or response.status_code // 300 == 3

    def handle_log(self):
        logger.info("{}".format(self.log))
