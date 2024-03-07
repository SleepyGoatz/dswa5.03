from datetime import datetime
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identification_page(nome, prontuario, instituicao):
    return render_template('user.html', nome=nome, prontuario=prontuario, instituicao=instituicao)


@app.route('/request-context/<nome>')
def request_context_page(nome):
    user_agent = request.headers.get('User-Agent')
    remote_addr = request.remote_addr
    host = request.host

    return render_template('request_context.html', nome=nome, user_agent=user_agent, remote_addr=remote_addr, host=host)
