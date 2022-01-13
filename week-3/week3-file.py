#引入內建功能模組
import urllib.request as req
import json
#開啟並以json方式讀取
with req.urlopen("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json") as response:
    data=json.load(response)
#開始析資料
clist=data["result"]["results"] #抓出所需核心資料-景點資訊，是list包字典格式
info=""
for x in clist:
    imgurls = x["file"]
    imgurlsList=imgurls.split("https")  
    info=info+x["stitle"]+","+x["address"][5:8]+","+x["longitude"]+","+x["latitude"]+","+"https"+imgurlsList[1]+"\n"
#寫入檔案
with open("data.csv",mode="w",encoding="utf-8") as file:
    file.write(info)    
   
