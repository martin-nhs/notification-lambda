from jinja2 import Environment, FileSystemLoader, TemplateError


class TemplateService:
    def __init__(self):
        self._template_loader = FileSystemLoader("./templates")
        self._environment = Environment(loader=self._template_loader)

    def get_slack_notification_template(self, message: str, nhs_environment: str, service_name: str) -> str:
        try:
            template = self._environment.get_template("slack_notification.jinja")

            return template.render({
                service_name,
                nhs_environment,
                message
            })
        except TemplateError as error:
            pass
