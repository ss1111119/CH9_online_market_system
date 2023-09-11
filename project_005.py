import json
import math

# 引入會員資料
global user_data
with open('user_data.json','r') as f:
    user_data = json.load(f)
    
      
# 引入商品資料
global product_list
with open('product.json','r') as f:
    product_list = json.load(f)

global login_status
login_status = False

global cart
cart = []