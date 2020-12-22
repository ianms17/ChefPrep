from twilio.rest import Client

account_sid = "AC4157c6a3350d28f5f501fd02e64e496b"
auth_token = "6621fa871edb37a1f26494d6f383d33e"


def send_message(client_number, text_message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        from_="+15077246171",
        to = client_number,
        body = text_message
    )
