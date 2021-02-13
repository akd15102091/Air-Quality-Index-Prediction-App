import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('xgboost_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['T', 'TM', 'Tm', 'SLP','H', 'VV', 'V','VM']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)

    result = output[0]

    return render_template('index.html', prediction_text='Predicted Air Quality Index : {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)
