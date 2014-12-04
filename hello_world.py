from flask import Flask
from flask import Flask, request
from flask import jsonify
import decimal
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    start_id = int(request.args.get('start_id', ''))
    count = int(request.args.get('count', ''))
    end_count = start_id + count
    processed_statement = []
    if end_count < 1000000:
        for x in range(start_id, end_count):
        	required_statement = {"id": x,"url":"fb","popularity":2637017,"appln_id":284882215,"appln_name":"1.0"}
        	processed_statement += [required_statement]
        return str(processed_statement)
    else:
        return  jsonify(result='false', error='You have already retrieved the desired number of records')

@app.route("/personagraph/optout/<dynamic_id>")
def error_response(dynamic_id):
    return  jsonify(error=1402, error_description='Access token expired: %s' % dynamic_id)    
if __name__ == "__main__":
    app.run(debug=True)
