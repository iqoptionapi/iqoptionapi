# python
check_websocket_if_connect = None
# try fix ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2361)
ssl_Mutual_exclusion = False  # mutex read write
# if false websocket can sent self.websocket.send(data)
# else can not sent self.websocket.send(data)
ssl_Mutual_exclusion_write = False  # if thread wirite

SSID = None

check_websocket_if_error = False
websocket_error_reason = None

balance_id = None
