from models.structured_event import StructuredEvent
from jinja2 import Environment, FileSystemLoader


class TemplateService:
    def __init__(self):
        self._template_loader = FileSystemLoader("./templates")
        self._environment = Environment(loader=self._template_loader)

    def get_slack_notification_template(self, event: StructuredEvent) -> str:
        template = self._environment.get_template("slack_notification.jinja")

        return template.render({
            "message": event.message,
            "nhs_environment": event.nhs_environment,
            "service_name": event.service_name
        })
