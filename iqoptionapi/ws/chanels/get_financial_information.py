from iqoptionapi.ws.chanels.base import Base

query = """"
query GetAssetProfileInfo($activeId:ActiveID!, $locale: LocaleName){
    active(id: $activeId) {
        id
        name(source: TradeRoom, locale: $locale)
        ticker
        media {
            siteBackground
        }
        charts {
            dtd { change }
            m1 { change }
            y1 { change }
            ytd { change }
        }
        index_fininfo: fininfo {
            ... on Index { description(locale: $locale) }
        }
        fininfo {
            ... on Pair {
                type
                description(locale: $locale)
                currency { name(locale: $locale) }
                base {
                    name(locale: $locale)
                    ... on Stock {
                        company {
                            country { nameShort }
                            gics {
                                sector
                                industry
                            }
                            site
                            domain
                        }
                        keyStat {
                            marketCap
                            peRatioHigh
                        }
                    }
                    ... on CryptoCurrency {
                        site
                        domain
                        coinsInCirculation
                        maxCoinsQuantity
                        volume24h
                        marketCap
                    }
                }
            }
        }
    }
}"""


class GetFinancialInformation(Base):
    name = "sendMessage"

    def __call__(self, activeId):
        data = {
            "name": "get-financial-information",
            "version": "1.0",
            "body": {
                "query": query,
                "operationName": "GetAssetProfileInfo",
                "variables": {
                    "activeId": activeId
                },
            },
        }
        self.send_websocket_request(self.name, data)
