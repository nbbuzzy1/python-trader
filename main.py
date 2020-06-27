import alpaca_trade_api as tradeapi
from alpaca import alpaca_api_key, alpaca_secret, alpaca_endpoint

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret,
    alpaca_endpoint
)

# Get our account information.
account = api.get_account()

print(api.get_last_trade('MSFT'))
aapl = api.polygon.historic_agg_v2(
    'AAPL', 1, 'day', _from='2019-01-01', to='2019-02-01').df
print(aapl)
