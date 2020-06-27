# Trading Bot Using Alpaca

import os
import alpaca_trade_api as tradeapi


alpaca_api_key = os.environ.get('ALPACA_API')
alpaca_secret = os.environ.get('ALPACA_SECRET')
alpaca_endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret,
    alpaca_endpoint
)

# Get our account information.
account = api.get_account()
print(account)
