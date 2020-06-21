from flask import Flask,render_template,url_for,request
import pandas as pd
import joblib

# load the model from disk
model = joblib.load('nlp_model.pkl')
cv = joblib.load('transform.pkl')
tf = joblib.load('tfidf_transform.pkl')
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data)
		tfidf = tf.transform(vect)
		my_prediction = model.predict(tfidf)[0]
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
