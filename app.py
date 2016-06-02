from flask import Flask, request
from graphviz import Source

app = Flask(__name__)


@app.route('/', methods=['POST'])
def graph_upload():
    return Source(request.files.values()[0].stream.read()).pipe(format='svg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
