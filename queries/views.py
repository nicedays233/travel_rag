from django.shortcuts import render

# Create your views here.
# queries/views.py

from django.http import JsonResponse
from embedchain import App
from embedchain.loaders.mysql import MySQLLoader
import os
def query_openai(request):
    # os.environ['OPENAI_API_KEY'] = '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'
    # os.environ['QDRANT_URL'] = 'http://35.238.215.187:6333'
    app = App.from_config(config_path="config.yaml")
    result = app.query("where is Hongmei Park")  # Execute query

    return JsonResponse({'result': result})


def add_data(request):
    config = {
        "host": "35.238.215.187",
        "port": "3307",
        "database": "travelai",
        "user": "root",
        "password": "123456",
    }

    mysql_loader = MySQLLoader(config=config)
    # os.environ['OPENAI_API_KEY'] = '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'
    # os.environ['QDRANT_URL'] = 'http://35.238.215.187:6333'
    app = App.from_config(config_path="config.yaml")
    app.add("https://en.wikipedia.org/wiki/OpenAI")  # Add data source
    app.add("temp.json")  # Add data source
    # Add data from MySQL
    # app.add("SELECT text FROM review;", data_type='mysql', loader=mysql_loader)
    # app.add("SELECT description,name FROM attraction;", data_type='mysql', loader=mysql_loader)
    # app.add("SELECT * FROM photo;", data_type='mysql', loader=mysql_loader)
    # app.add("SELECT * FROM address;", data_type='mysql', loader=mysql_loader)

    return JsonResponse({'status': 'Data added successfully'})