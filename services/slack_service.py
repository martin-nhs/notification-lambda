import os

from loguru import logger
from urllib3 import request, BaseHTTPResponse
from .template_service import TemplateService


class SlackService:
    def __init__(self):
        self._slack_webhook = os.environ["SLACK_WEBHOOK_URL"]
        self._template_service = TemplateService()

    def send_notification(self, message: str, nhs_environment: str, service_name: str):
        templated_message: str = self._template_service.get_slack_notification_template(
            message,
            nhs_environment,
            service_name
        )

        response: BaseHTTPResponse = request(method="POST",
                                             url=self._slack_webhook,
                                             body=templated_message,
                                             headers={"Content-Type": "application/json"})

        if response.status != 200:
            logger.error(f"The message failed to send to Slack with HTTP status {response.status}.")
