import os
import pandas as pd
import json
from collections import defaultdict

def handle_uploaded_file(f):
    filename = "app/data/file.csv".format(id)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename

def convert(csv):
    print("Reading CSV File...")
    df = pd.read_csv(csv, sep='\t', header=None)
    print("CSV File Imported\n")
    cols = df.iloc[:, [1, 3]]
    #totals = {"Date": [], "Calories": [], "Carbs": [], "Fat": [], "Protein": [], "Sodium": [], "Sugar": []}
    totals = defaultdict(list)
    for i in range(len(cols)):
        nutrition = cols.loc[i, 3]
        datestring = cols.loc[i, 1] + " 00:00:00"
        totals["Date"].append(datestring)
        data = json.loads(nutrition)
        js = pd.json_normalize(data['total'])
        keys = {"calories", "carbs", "fat", "protein", "sodium", "sugar"}
        for i in range(len(js)):
            if js.loc[i]['name'].lower() in keys:
                totals[js.loc[i]['name']].append(js.loc[i]['value'])

    totals = pd.DataFrame(totals)
    #print(totals)
    totals.to_csv(csv, mode='w+')
