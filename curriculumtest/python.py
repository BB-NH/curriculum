#notify.py
import requests

def send_line_notify(notification_message):
    # コピーしたトークンを貼り付けてください
    line_notify_token = 'IpoDcHQxF2JQYkSlG1vHzHLrHle7T7dWixM2KUwz9F4'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

send_line_notify("通知内容をここに渡してください")