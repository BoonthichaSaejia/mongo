import requests
import bs4
import json
from datetime import datetime
from pymongo import MongoClient

URI = "mongodb+srv://user1:B6210503667mui@cluster0.aahd4.gcp.mongodb.net/test"
client = MongoClient(URI)

r=requests.get("https://www.thairath.co.th/news/foreign")
html_document =bs4.BeautifulSoup(r.content,"html.parser")
html_elements=html_document.select_one("script#__NEXT_DATA__")

data=json.loads(html_elements.string)
path=data["props"]["initialState"]["news"]["data"]["items"]["lastestNews"]

collection = client.foreignNews.News
#query={"category":"ต่างประเทศ"}
#collection.delete_many(query)
keys=["account_id","title","publish_date","desc","tags","cover_img","news_url","category"]
for lst in path:
  date_time_str=lst["publishTime"]
  date_time_obj=datetime.strptime(date_time_str[:19], '%Y-%m-%dT%H:%M:%S')
  values=[lst["id"],lst["title"],date_time_obj,lst["abstract"],lst["tags"],lst["image"],lst["canonical"],lst["topic"]]
  db_document = dict(zip(keys, values))
  query={"account_id":lst["id"]}
  cursor=collection.find(query)
  if cursor.count()==0:
    collection.insert_one(db_document)

print("Finish")