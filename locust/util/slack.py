import os
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(
    token=os.environ['SLACK_TOKEN'],
    run_async=False  # turn async mode on
)
# hardcoding the channel name for now,
# will provide provision of proving channel name later
slack_channel = "#udaan-locust-reports"


# Define this as an async function
def send_to_slack(chan,text, file_name, content):
    try:
        # Don't forget to have await as the client returns asyncio.Future
        response = client.files_upload(
            channels=chan,
            content=content,
            filename=file_name,
            filetype="csv",
            initial_comment=text
        )
        assert "ok"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print("Got an error: {e.response['error']}")
