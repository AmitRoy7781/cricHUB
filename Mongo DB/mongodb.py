import pymongo
client = pymongo.MongoClient()
db = client.test
db.sites.insert({"url":"http://www.cricbuzz.com","name":"Cricbuzz Website"})
site = db.sites.find_one()
print(site)
print("I like the %s and the url is %s"%(site["name"],site["url"]))
sites = db.sites.find()
