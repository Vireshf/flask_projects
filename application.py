from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import datetime

@app.route('/home')
@app.route('/')
def index():
	return "<h1>hello world</h1>"

@app.route('/user')
@app.route('/user/<name>')
def query_strings(name='chinnu'):
	return 'you have entered user is {}'.format(name)


@app.route('/number')
@app.route('/number/<int:num>')
def query_strings1(num = 0):
	return 'you have entered user is {}'.format(num)

@app.route('/text')
@app.route('/text/<string:num>')
def query_strings2(num = 'puttu'):
	return 'you have entered user is {}'.format(num)


@app.route('/temp')
def query_strings3():

	movie_dict={'Kanasugara' : 180,
				'Kotigobba2' : 200,
				'KGF': 179,
				'Maja' : 150}
	return render_template('hello.html',movies = movie_dict)

@app.route('/macro')
def macros():
	movie_dict={'Kanasugara' : 250,
				'Kotigobba2' : 200,
				'KGF': 179,
				'Maja' : 150}
	return render_template('using_macro.html',movies = movie_dict)

@app.route('/filters')
def sorting():
	movie_dict={'Kanasugara' : 250,
				'kotigobba2' : 200,
				'KGF': 179,
				'Nalla':100,
				'Maja' : 150}
	return render_template('filter.html',movies=movie_dict,name=None)

app.config.update(
	SECRET_KEY = "1234",
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/sample"
	)

db = SQLAlchemy(app)

class Publication(db.Model):
	__tablename__ = 'publication'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80),nullable = False)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return 'id is {} and name is {}'.format(self.id,self.name)

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(80),nullable = False, index = True)
	author = db.Column(db.String(80))
	avg_rating = db.Column(db.Float)
	format = db.Column(db.String(80))
	image = db.Column(db.String(80),unique = True)
	num_pages = db.Column(db.Integer)
	pub_date = db.Column(db.DateTime,default=datetime.datetime.utcnow())

	#foreign key
	pub_id = db.Column(db.Integer,db.ForeignKey('publication.id'))


	def __init__(self,title,author,avg_rating,format,image,num_pages,pub_id):
		self.title = title
		self.author = author
		self.avg_rating = avg_rating
		self.format = format
		self.image = image
		self.num_pages = num_pages
		self.pub_id = pub_id

	def __repr__(self):
		return 'title: {} and author : {}'.format(self.title,self.author)
		
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)