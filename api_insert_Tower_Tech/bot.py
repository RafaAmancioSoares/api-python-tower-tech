from credentials import token
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError



client = WebClient(token=token)

def mensagem(texto):
    try:
        response = client.chat_postMessage(channel='C02HTK4PNH0', text=texto)
        assert response["message"]["text"] == texto
    except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

