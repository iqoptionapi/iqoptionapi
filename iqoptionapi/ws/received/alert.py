"""Module for IQ option websocket."""

def alert(api, message):
    if message["name"] == "alerts":
        api.alerts = message["msg"]["records"]
    elif message["name"] == "alert":
        request_id = message["request_id"]
        api.alert[request_id] = message
    elif message["name"] == "alert-triggered":
        value = message["msg"]["value"]
        asset_id = message["msg"]["asset_id"]
        api.alert_triggered[value] = asset_id