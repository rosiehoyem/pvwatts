#!/usr/local/bin/python
import json
from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pvwatts.html', methods=['GET', 'POST'])
def pvwatts():
  if request.method == 'GET':
    abort(404)
  latitude = request.form['lat']
  longitude = request.form['lon']
  return render_template('pvwatts.html',latitude=latitude,longitude=longitude)

@app.route('/results.html', methods=['GET', 'POST'])
def results():
  if request.method == 'GET':
    abort(404)
  jsn = json.loads(request.form['json'])
  table = createTable(jsn['outputs'])
  return render_template('results.html', table=table)

def createTable(object):
  table = '<table id=data>'
  for key in object:
    table += '<tr><th>%s</th>' % key
    try:
      for i in object[key]:
        table += '<td>$%.2f</td>' % i
    except TypeError:
      table += '<td>$%.2f</td>' % object[key]
    table += '</tr>'
  return table

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
