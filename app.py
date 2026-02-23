from flask import Flask,render_template,url_for,request
import joblib
import os

# load the model from disk
model = joblib.load('nlp_model.pkl')
cv = joblib.load('transform.pkl')
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
		my_prediction = model.predict(vect)[0]
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
