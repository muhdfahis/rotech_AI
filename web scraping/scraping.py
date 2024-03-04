import requests
import pandas as pd

cookie = "osano_consentmanager_uuid=4d3bac53-4f82-4de2-a2d9-d5ccc812b3a1; osano_consentmanager=ky7ara8EiINlqyuvzdKN9CuyKnqdqeWUP2tmoWfAfNW-45E1KlmIjC1lYjEWuQGbxtSEjd7VEryG8EfD8mFDHLApL1mtwGwGcAuUtnOzrrtVO7Y7hmCybWHfDqR7l2_hG3yvObUC8cUVGMKTQxEG8IcPnCnDC4A6gt74186F9OV230c5sgY-4Bp0lt9ApqS-GsF67jk1K9HWCHP5CJVZfy8K_nDLg2SrWq3-Q2fJc7lQc6HrVR5dwPnwsttxY0M-BRjjewJnFIECM5euJrdlMR3LK7SKS9bpREtRCQ==; _gcl_au=1.1.35412247.1706764222; fw_se={%22value%22:%22fws2.4e2cccdd-3c43-4da6-b8f7-f8ee53c4f990.1.1706764221974%22%2C%22createTime%22:%222024-02-01T05:10:21.974Z%22}; _gid=GA1.2.2133731474.1706764222; _fbp=fb.1.1706764222798.1856152528; _pin_unauth=dWlkPU9UQXlNek0zT0dNdE9HTmxOUzAwTnpsbUxUazFOR1F0WkdVMlpHWTJaamRtT0RFMw; _uetsid=339cf0f0c0c011eeac968d7fb21f4a2e; _uetvid=339d4d40c0c011ee98120b37d99d5b6e; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-02-01T05:10:30.309Z%22}; _ga_EMDXDP2N4W=GS1.2.1706764222.1.1.1706764231.51.0.0; __cf_bm=XahkUzvIxbmi4NNr5x.eI_9yf4TJ8vlJIPu5kT5THu4-1706764233-1-AVqOuN8vlV6btc+mL+x7nmucPC9d3aO3m73kgASTKh4m66J/4xvDS4mdO/kiCJQ1gwV1OrlUUetucSuiQxP5KCI=; ajs_anonymous_id=8f07fd39-1a22-4d72-9da2-071358a37a1f; __stripe_mid=a4b4de33-fd76-4e3c-9627-88e07dbdb80b73397b; __stripe_sid=1064c9d1-58b3-404c-b705-51c7b5582fab64a774; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-02-01T05:11:56.689Z%22}; fw_uid={%22value%22:%2213da95ae-a1ac-41ac-854e-517c01598d97%22%2C%22createTime%22:%222024-02-01T05:11:56.699Z%22}; _gat_UA-000000000-1=1; session-prd-tfm=.eJxNyctygjAYQOF3ydrpkChW2Fmo-DOSVKsgbBgCYQw3HYIX0um7l2UXZ_OdH5SWvVAXZJdZo8QMpTfRt1knugHZQ3-fRAml5LVLh2stOmQjMfoX7uWSSR9OGjCVvvU2Ic5JOE7pnDQP3li3xIElVPt54oYti4L57hi_YgIDdQ-SOsaCeYB3USiD6lBRN35SDZo5oKALdXL2yyzaS1adRuZ-TtXmzvEviYdv_P9vTcy9p4J2c-fENHlk4XyEZbH1cfL9lFm0MaC6vqheE6pjI6gCXO7f-JHFhbl2thiHoDVQL9TvH1-4JmeriGXtHHrDfZQNEQs0Q3cl-lQWyDbJCpOVZf3-AYmqZxM.GJy5nA.K7tK_c2liydoaCtLYSMpR6wMCh8; _dd_s=rum=0&expire=1706765216924; _ga=GA1.1.1194549165.1706764222; _ga_2NZ40CS25B=GS1.1.1706764222.1.1.1706764317.58.0.0"
HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}
# searchinput = input("enter the items to search :")

df_fhs_mart= pd.read_excel("fhs_mart.xlsx",sheet_name="Sheet1")

for i in range (0,len()):
    print(data['items'][i]['name']),print(data['items'][i]['base_price'])
    
    URL = "https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=5&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=true&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false"
    responses = requests.get(URL,headers=HEADERS)
    data = responses.json()


    items= data['items']
    df_items= pd.DataFrame(items)
    df_clean = df_items[['name','base_price','display_uom','average_weight',]]
    df_clean.to_excel(f"scraped_items/{searchinput}.xlsx",index=False)
# df_clean.to_csv('item.csv',index=False)

# df_clean.to_json('item.json',index=False)
# df_clean.to_html('item.html',index=False)
# df_clean.to_excel('item.xlsx',index=False)


# df_fhs_mart= pd.read_excel("fhs_mart.xlsx",sheet_name="Sheet1")
# searchitem=fhs_mart.loc[0]
# print(searchitem)
