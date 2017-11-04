# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:18:52 2017

@author: stefan
"""

import json
import requests

"  Get all available asset pairs
response = requests.get("https://hft-service-dev.lykkex.net/api/AssetPairs").json()

"  Check if API is working
requests.get("https://hft-service-dev.lykkex.net/api/IsAlive").json()

" Get order book (BTCUSD)
pair = 'BTCUSD'
ob = requests.get("https://hft-service-dev.lykkex.net/api/OrderBooks/"+pair).json()
sellprice = ob[0]['Prices'][0]['Price']
buyprice = ob[1]['Prices'][-1]['Price']

