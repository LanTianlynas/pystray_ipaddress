import datetime
import pandas as pd

table = pd.read_csv("global_futures.csv").to_dict(orient='records')
print(table)
# symbol_list = []
# for row in table:
#     symbol = {}
#     symbol['symbol'] = row['symbol']
#     symbol['exchange'] = row['exchange']
#     symbol['name'] = row['name']    
#     symbol["trade"] = row["trade"]
#     symbol["settlement"] = "0.00"
#     symbol["presettlement"] = "0.00"
#     symbol["open"] = row["open"]
#     symbol["high"] = row["high"]
#     symbol["low"] = row["low"]
#     symbol["close"] = "0.00"
#     symbol["bidprice1"] = row["bidprice1"]
#     symbol["askprice1"] = row["askprice1"]
#     symbol["bidvol1"] = "0.00"
#     symbol["askvol1"] = "0.00"
#     symbol["volume"] = row["volume"]
#     symbol["position"] = "0.00"
#     symbol["ticktime"] = row["ticktime"]
#     symbol["tradedate"] = datetime.datetime.now().strftime('%Y-%m-%d')
#     symbol["preclose"] = row["preclose"]
#     symbol["changepercent"] = row["changepercent"]
#     symbol["bid"] = "0.00"
#     symbol["ask"] = "0.00"
#     symbol["prevsettlement"] = "0.00"
#     symbol_list.append(symbol)

# print(symbol_list)



    
