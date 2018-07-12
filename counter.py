from flask import Flask, request, jsonify
import pickle
import os.path
import sys 
import time, datetime
import json

app = Flask(__name__)

import sys 
if len (sys.argv) != 2 : 
    print("Usage: python counter.py <urlMap.json> ")
    sys.exit (1) 

file_name=sys.argv[1]
urlMap = {}


def save_obj(obj, name ):
    with open( name, 'wb') as f:
        json.dump(obj, f)

def load_obj(name):
    with open( name, 'rb') as f:
        return json.load(f)

@app.route("/")
def help():
    return jsonify(urlMap)

@app.route("/reset")
def reset():
    global urlMap
    urlMap = {}
    save_obj(urlMap, file_name)
    return "Reset complete"

@app.route("/api/<prefix>")
def main(prefix):
    global urlMap
    key = prefix
    if prefix in urlMap:
        urlMap[prefix] = urlMap[prefix] + 1 
        save_obj(urlMap, file_name)
        return '{0:03d}'.format(urlMap[prefix])
    else:
        urlMap[prefix] = 1 
        save_obj(urlMap, file_name)
        return '{0:03d}'.format(urlMap[prefix])
    return "Prefix: %s" % prefix

@app.route("/api/<prefix>/reset")
def reset_key(prefix):
    global urlMap
    key = prefix
    if prefix in urlMap:
        urlMap[prefix] = 0
    return '{0:03d}'.format(urlMap[prefix])

@app.route("/who")
def reportevent():
    with open('report.log', 'a') as f:
        f.write("Address: " + str(request.remote_addr) + " Time: " + datetime.datetime.now().strftime("%y-%m-%d %H:%M") )

    return "success"

if os.path.isfile(file_name):
    urlMap = load_obj(file_name)

app.run('0.0.0.0', 5000)
