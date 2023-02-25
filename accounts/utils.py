import requests
from django.conf import settings


def send_email(recipient, subject, body):
    """Send an email to the recipient."""
    basic = requests.auth.HTTPBasicAuth(
        settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY
    )
    try:
        response = requests.post(
            settings.MAILJECT_SEND_URL,
            json={
                "FromEmail": settings.MAILJET_USER,
                "FromName": "Ifihan from Shomolu",
                "Subject": subject,
                "Text-part": body,
                "Recipients": recipient,
            },
        )
    except requests.exceptions.RequestException as e:
        return False, str(e)

    if response.status_code != 200:
        return False, response.text

    response_body = response.json()

    if (
        response_body[0]["Email"] != settings.MAILJET_USER
        and "MessageID" not in response_body[0]
    ):
        return False, "Invalid response"
    return True, ""


# figure out how to send email
