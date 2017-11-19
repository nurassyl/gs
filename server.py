from flask import Flask
from flask import request, abort, render_template, jsonify, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import uuid
from gs.converter import *

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(os.environ["_MYSQL_USER"], os.environ["_MYSQL_PASSWORD"], os.environ["_MYSQL_HOST"], os.environ["_MYSQL_PORT"], os.environ["_APP_NAME"].lower()), echo=int(os.environ["FLASK_DEBUG"]))
Session = sessionmaker(bind=engine)
app = Flask(os.environ["_APP_NAME"])
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		# return jsonify({'message': 'Hello!'})
		return render_template('index.html', uuid=str(uuid.uuid4()), env=os.environ)
	elif request.method == 'POST':
		Input = request.form.to_dict()['input'][:7000]
		Converter = request.form.to_dict()['converter']
		Output = ''

		if Converter == 'cyrillic-latin':
			Output = convert_cyrillic_to_latin(Input)
		elif Converter == 'cyrillic-tote':
			Output = convert_cyrillic_to_tote(Input)
		elif Converter == 'latin-cyrillic':
			Output = convert_latin_to_cyrillic(Input)
		elif Converter == 'latin-tote':
			Output = convert_latin_to_tote(Input)
		elif Converter == 'tote-latin':
			Output = convert_tote_to_latin(Input)
		elif Converter == 'tote-cyrillic':
			Output = convert_tote_to_cyrillic(Input)

		return Response(response=Output, status=200, mimetype='text/plain')
	else:
		abort(404)
		# render_template('page_not_found.html'), 404

app.run(host=str(os.environ["_HTTP_HOST"]), port=int(os.environ["_HTTP_PORT"]))
