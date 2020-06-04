import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Classifier.model','rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	form_features = [float(x) for x in request.form.values()]
	final_features = [np.array(form_features)]
	prediction = model.predict(final_features)

	if prediction[0] == 0:
		return render_template('index.html', prediction_text = 'This Transaction Is A Genuine Transaction')
	else:
		return render_template('index.html', prediction_text = 'This Transaction Is A Fraudulent Transaction')

if __name__ == '__main__':
	app.run(debug=True)