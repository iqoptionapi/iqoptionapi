from iqoptionapi.ws.chanels.base import Base

"""
{"name":"sendMessage","request_id":"356","msg":{"name":"request-leaderboard-deals-client","version":"1.0","body":{"country_id":0,"user_country_id":191,"from_position":1,"to_position":64,"near_traders_country_count":64,"near_traders_count":64,"top_country_count":64,"top_count":64,"top_type":2}}}
"""


class Leader_Board(Base):
    name = "sendMessage"

    def __call__(
        self,
        country_id,
        user_country_id,
        from_position,
        to_position,
        near_traders_country_count,
        near_traders_count,
        top_country_count,
        top_count,
        top_type,
    ):

        data = {
            "name": "request-leaderboard-deals-client",
            "version": "1.0",
            "body": {
                "country_id": country_id,
                "user_country_id": user_country_id,
                "from_position": from_position,
                "to_position": to_position,
                "near_traders_country_count": near_traders_country_count,
                "near_traders_count": near_traders_count,
                "top_country_count": top_country_count,
                "top_count": top_count,
                "top_type": top_type,
            },
        }

        self.send_websocket_request(self.name, data)
