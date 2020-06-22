import pandas as pd
import csv

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

data = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')

data.to_csv('./output_data.csv')

with open("./output_data.csv","r") as f_input:
 csv_data = csv.DictReader(f_input)
 for row in csv_data:
  state = row['State']
  State = state.replace(" ","_")
  District = row['District']
  Confirmed = row['Confirmed']
  Active = row['Active']
  Recovered = row['Recovered']
  Deceased = row['Deceased']


  db = client.India
  coll = client.India[State]

  coll.insert_one({"district": District, "confirmed": Confirmed, "active":Active, "recovered": Recovered, "deceased" :Deceased})
