from loguru import logger
from services.slack_service import SlackService
from models.structured_event import StructuredEvent


def notification_handler(event, context) -> dict:
    logger.info("Successfully initiated the notification lambda, processing request.")

    structured_event: StructuredEvent = StructuredEvent(
        event["message"],
        event["nhs_environment"],
        event["service_name"]
    )

    # Instantiate services.
    slack_service = SlackService()

    # Send messages.
    slack_service.send_notification(structured_event)

    return {
        "status": 200,
        "result": "success"
    }
