import alpaca_trade_api as tradeapi
from alpaca import alpaca_api_key, alpaca_secret, alpaca_endpoint

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret,
    alpaca_endpoint
)

# Get our account information.
account = api.get_account()

# print(api.get_last_trade('MSFT'))
aapl = api.polygon.historic_agg_v2(
    'DOW', 1, 'day', _from='2019-01-01', to='2019-12-31').df


# Given a security, check how it did on the third day after decreasing the prior two days?
closing_values = list(aapl.get('close'))
sum_dollar = 0
sum_percent = 0

for index, value in enumerate(closing_values):
    if index < 3:
        continue
    else:
        if closing_values[index - 3] > closing_values[index - 2] > closing_values[index - 1]:
            percent = round(
                ((value - closing_values[index - 1]) / closing_values[index - 1]), 2)
            sum_percent += percent
            dollar_change = value - closing_values[index - 1]
            sum_dollar += dollar_change

# print(percent_increases)
print(sum_dollar)
print(sum_percent)
