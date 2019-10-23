import os
import json

from twilio.rest import Client


def send_sms(receiving_number: str, message: str) -> None:
    script_dir = os.path.dirname(__file__)
    rel_path = "../creds.json"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, "r") as f:
        creds = json.load(f)

    account_sid = creds["ACCOUNT_SID"]
    auth_token = creds["ACCOUNT_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=creds["PHONE_NUMBER"],
        to=receiving_number
    )

    print(f'Message has been sent: {message.sid}')
