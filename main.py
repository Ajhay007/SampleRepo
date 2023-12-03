import flask
from flask import Flask, request, render_template, render_template_string, redirect
import CurrencyConv, json


app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/data')


@app.route('/data')
def CC():
    data=json.loads(CurrencyConv.conv())
    return json.dumps({'from':data['from'],
                'to':data['to'],
            'amount':data['amount']})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7770)