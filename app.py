#!/usr/bin/env python3
from flask import Flask, request, send_file
from graphviz import Source
from base64 import urlsafe_b64encode, urlsafe_b64decode
import pydot
import zlib

app = Flask(__name__)


@app.route('/', methods=['POST'])
def graph_upload():
    file_vals = next(request.files.values())
    file_contents = file_vals.stream.read().decode('utf-8')
    return Source(file_contents).pipe(format='svg')


@app.route('/get-page', methods=['POST'])
def graph_to_page():
    file_vals = next(request.files.values())
    file_contents = file_vals.stream.read().decode('utf-8')
    file_contents = pydot.graph_from_dot_data(file_contents).to_string()
    compressed = zlib.compress(file_contents.encode('utf-8'), 9)
    encoded = urlsafe_b64encode(compressed)
    return request.host_url + "view?s=" + encoded.decode('utf-8')


@app.route('/view', methods=['GET'])
def view():
    source = urlsafe_b64decode(request.args['s'])
    source = zlib.decompress(source)
    source = source.decode('utf-8')
    return Source(source).pipe(format='svg')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file_vals = next(request.files.values())
        file_contents = file_vals.stream.read().decode('utf-8')
        return Source(file_contents).pipe(format='svg')
    else:
        return send_file('upload.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
