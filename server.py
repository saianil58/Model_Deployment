# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import os
os.chdir(r'C:\Users\samu0315\Desktop\Mine\Personal\gl_aiml\7.Model Deployment\picking')
# Load the model
model = pickle.load(open('wine_model.sai','rb'))
app = Flask(__name__)
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    predict_request=[[
        data['s1'],
        data['s2'],
        data['s3'],
        data['s4'],
        data['s5'],
        data['s6'],
        data['s7'],
        data['s8'],
        data['s9'],
        data['s10'],
        data['s11'],
        data['s12'],
        data['s13']
    ]]
    predict_request=np.array(predict_request)
    print(predict_request)
    prediction = model.predict(predict_request)
    print(prediction)
    # Take the first value of prediction
    output = prediction[0]
    print(output)
    return jsonify(int(output))

if __name__ == '__main__':
    app.run(port=8111, debug=True)
