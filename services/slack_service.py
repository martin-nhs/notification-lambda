import os

from utilities.aws_utilities import fetch_ssm_parameter
from models.structured_event import StructuredEvent
from urllib3 import request, BaseHTTPResponse
from .template_service import TemplateService
from loguru import logger


class SlackService:
    def __init__(self):
        self._slack_webhook = fetch_ssm_parameter(os.environ["SLACK_WEBHOOK_URL_SSM_PARAMETER"], True)
        self._template_service = TemplateService()

    def send_notification(self, event: StructuredEvent):
        templated_message: str = self._template_service.get_slack_notification_template(event)
        response: BaseHTTPResponse = request(method="POST",
                                             url=self._slack_webhook,
                                             body=templated_message,
                                             headers={"Content-Type": "application/json"})

        if response.status != 200:
            logger.error(f"The message failed to send to Slack with HTTP status {response.status}.")
        else:
            logger.info("The message has successfully been sent to Slack.")
