# ticket-bot
## 1.搭配資源：
```
  1.python
  2.Selenium套件
  3.chromedriver(搭配當前google chrome版本下載)：https://developer.chrome.com/docs/chromedriver/downloads
```

## 2.說明：
  在```driver.get("")```函數中的引號內放上連結。
  使用f12編輯介面在網頁中找到該欄位的"xpath"並使用函數```driver.find_element("xpath", "該欄位的xpath")```按照執行順序執行程式。
  ### examples:
    acc = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    acc.clear()
    acc.send_keys("account")

    password = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    password.clear()
    password.send_keys("password")
  

## 3.動作函數：
```
  1. findElement() -- 定位欄位
  2. click() -- 向指定欄位點擊
  3. send_keys() -- 向指定欄位輸入文字
  4. clear() -- 清除指定欄位
```

參考資料來源：
https://tonidata.medium.com/%E8%87%AA%E5%8B%95%E6%90%B6%E7%A5%A8%E7%A8%8B%E5%BC%8F-%E7%94%A8python%E6%90%B6%E7%86%B1%E8%B3%A3%E5%95%86%E5%93%81-1f542f50c395
