import requests
import pandas  as pd
link = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bitcoin&start=1&limit=1000&category=spot"
resp = requests.get(link,timeout = 5).json()
base_price = resp["data"]["marketPairs"][0]["price"]
details = [{"name":i["exchangeName"],"base":i["baseSymbol"],"quote":i["quoteSymbol"],"price_usd":i["price"],"price_quote":i["quote"],"volume_usd":i["volumeUsd"],"delta_bp": 10000*(i["price"] - base_price)/((i["price"] + base_price)/2)} for i in resp["data"]["marketPairs"]]
dets = pd.DataFrame(details)
dets_decent_vol = dets[dets["volume_usd"] > 600_000]
dets_decent_vol = dets_decent_vol.sort_values(by = "delta_bp")
dets_decent_vol["composite_rate"] = dets_decent_vol["price_quote"]/base_price
tradable_venues  = ["Binance","Kraken","Bitstamp","Coinbase Exchange","FTX"]
dets_decent_vol = dets_decent_vol[dets_decent_vol["name"].isin(tradable_venues)]