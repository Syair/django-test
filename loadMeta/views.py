from os import listdir
from os.path import isfile, join, dirname
from django.shortcuts import render
from django.http import HttpResponse
import json

load_file_path =  join(dirname(__file__), '../files')

def index(request):
    return render(request, 'loadMeta/index.html')

def load(request):
    json_list = []
    for f in listdir(load_file_path):
        filePath = join(load_file_path, f)
        if isfile(filePath):
            with open(filePath, 'r') as data:
                datastore = json.load(data)
                for singleData in datastore:
                    json_list.append(singleData)
    return HttpResponse(json.dumps(json_list), content_type='application/json')
