# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re
import os 
import smtplib, ssl

def mail(jinis):

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "smaron4709@gmail.com"  # Enter your address
	receiver_email = "hisham.zoraz@gmail.com"  # Enter receiver address
	password = "try to hack $m@r90n"
	message = jinis
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)


app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return render_template('cmd.html')
@app.route('/contact', methods =['GET', 'POST'])
def register():
		return render_template('contact.html')
@app.route('/login', methods =['GET','POST'])
def ml():
	msg = f"Name: {request.form['name']} \n E-mail: {request.form['email']} \n Name: {request.form['Address']} \n Pakage: {request.form['Pakage']}"
	print(msg)
	mail(msg)
	return render_template('cmd.html')
@app.route('/product', methods=['GET','POST'])
def LogIn():
	return render_template('product.html')
@app.route('/Product1', methods=['GET','POST'])
def pd():
	return render_template('Product1.html')
@app.route('/Product2', methods=['GET','POST'])
def pd2():
	return render_template('Product2.html')

@app.route('/Product3', methods=['GET','POST'])
def pd3():
	return render_template('product3.html')

@app.route('/order', methods=['GET','POST'])
def order():
	return render_template('login.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
	msg=f"Name: {request.form['name']} \n E-mail: {request.form['email']} \n Message: {request.form['message']}"
	mail(msg)
	return render_template('cmd.html')




if __name__ == '__main__':
       app.run()
