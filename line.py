import requests
import json


def message_broadcast(message, line_notify_token):
    # エンドポイント
    url = "https://api.line.me/v2/bot/message/broadcast"
    # 内容を作成
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {line_notify_token}",
    }
    data = {
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    #メッセージをポスト
    r = requests.post(
        url,
        headers=headers,
        data=json.dumps(data)
    )
