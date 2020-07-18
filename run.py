from flaskblog import create_app


app = create_app()
if __name__ == '__main__':
	app.run(debug=True)











#running flask
'''
export FLASK_APP=flaskblog.py
export FLASK_DEBUG=1
flask run

or

if __name__ == '__main__':
	app.run()

and on the terminal : python3 flaskbog.py
'''
