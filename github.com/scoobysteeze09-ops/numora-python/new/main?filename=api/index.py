from flask import Flask
app = Flask(__name__)
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def h(path): return '<h1>Numora Works! USA Jobs</h1><p>Support $18/hr - Data Entry $22/hr</p>'