text="iamfahisfrommalappuram"
result_list= [0]*26



for alphabet in text:
    ascii_value=97
    while(ascii_value):
        if alphabet == chr(ascii_value):
            result_list[ascii_value-97]=result_list[ascii_value-97]+1
            break
        ascii_value=ascii_value+1
print(result_list)
        
        

        