import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
url = 'https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=10'
r = requests.get(url)
r.encoding = 'utf-8'
if r.status_code == 200:
    soup = bs(r.content, 'xml')
    exchange_rates = []
    exrates = soup.find_all('Exrate')
    for exrate in exrates:
        currency_code = exrate.get('CurrencyCode', 'N/A')
        currency_name = exrate.get('CurrencyName', 'N/A')
        buy_cash = exrate.get('Buy', 'N/A') 
        transfer = exrate.get('Transfer', 'N/A') 
        sell = exrate.get('Sell', 'N/A')  
        exchange_rates.append({
            'Mã ngoại tệ': currency_code,
            'Tên ngoại tệ': currency_name,
            'Mua tiền mặt': buy_cash,
            'Mua chuyển khoản': transfer,
            'Bán': sell
        })
    df = pd.DataFrame(exchange_rates)
    # df.insert(0, 'STT', range(0, len(df) + 1))
    # df = df.replace('-', pd.NA)
    # df = df.dropna(subset=['Mua tiền mặt', 'Mua chuyển khoản', 'Bán'], how='any') 
    # df = df.sort_values('Mã ngoại tệ')  
    # df = df.sort_values('Bán', ascending=False) 
    print(f"TỶ GIÁ NGOẠI TỆ VIETCOMBANK: ")
    print(df.to_string(index=False))
    df.to_csv('tygia_vietcombank.csv', index=False, encoding='utf-8-sig')
    df.to_excel('tygia_vietcombank.xlsx', index=False, engine='openpyxl')
else:
    print("Get Error!")