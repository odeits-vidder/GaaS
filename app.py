#!/usr/bin/env python3
from flask import Flask, request
from graphviz import Source

app = Flask(__name__)


@app.route('/', methods=['POST'])
def graph_upload():
    file_vals = next(request.files.values())
    file_contents = file_vals.stream.read().decode('utf-8')
    return Source(file_contents).pipe(format='svg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
