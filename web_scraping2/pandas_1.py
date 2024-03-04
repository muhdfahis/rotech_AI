import pandas as pd

data={
    'name':['apple','ice cream','carrot','mango','onion','ginger'],
    'price':['$1','$23','$24','$12','$32','$13'],
    'unit':['lb','kg','lb','lb','lb','lb'],
    'category':['fruits','frozen','vegetable','fruits','vegetable','vegetable']
    
    
}
df=pd.DataFrame(data)

df.to_csv("sample.csv",index=False)

