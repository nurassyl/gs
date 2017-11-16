from flask import Flask
from flask import request, abort, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(os.environ["_MYSQL_USER"], os.environ["_MYSQL_PASSWORD"], os.environ["_MYSQL_HOST"], os.environ["_MYSQL_PORT"], os.environ["_APP_NAME"].lower()), echo=int(os.environ["FLASK_DEBUG"]))
Session = sessionmaker(bind=engine)
app = Flask(os.environ["_APP_NAME"])
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return jsonify({'message': 'Hello!'})
    else:
        abort(404)
        # render_template('page_not_found.html'), 404

app.run(host=str(os.environ["_HTTP_HOST"]), port=int(os.environ["_HTTP_PORT"]))
