from bottle import run,get,route,template
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
# you can also connect to Atlas database by passing the connetion string https://docs.atlas.mongodb.com/driver-connection/


def html_mongo():
 html =  '''
 <h1> Hello world </h1>
 <h4><a href='/covid'> click here </a> for Covid-19 Data</h4>
 '''
 return html

@route('/covid')
def covid():
 collection = client.India.list_collection_names()
 collection.sort()
 return template("show_data",data=collection,database="India")

@route('/India/<State>')
def show_data(State):
 coll = client.India[State].find({},{"_id":0,"district":1,"confirmed":1,"active":1,"recovered":1,"deceased":1})
 return template("show_stats",data=coll,database=State)
 

@get('/')
def home():
 return html_mongo()

run(host="localhost",port=8080,reloader = True)
