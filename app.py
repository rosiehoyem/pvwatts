#!/usr/local/bin/python

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
  json = request.form['json']
  return render_template('results.html', json=json)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
