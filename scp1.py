# -*- coding: utf-8 -*-

from selenium.webdriver import chrome
driver=chrome()

url1="https://www.google.com/maps/search"


msg=[]

while True:
    
    url2=input("請輸入關鍵字")
    
    if url2=="end":
        break
        
    else:
        urls=url1+url2
        msg.append(url2)
        
        driver.get(urls)
    
for items in msg:
    
    print("已查詢字串:"+items)
    print("\n")
    
print("共"+str(len(msg))+"筆！")

    
