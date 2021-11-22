# Running the flask server
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, template_folder='C:/Users/notar/Desktop/ProjectsDataScience/Diabetes/Web_app')

model = pickle.load(open('model.pkl', 'rb')) # rb reading binary in Windows

@app.route('/') # root page or home page
def home():
    return render_template('Index.html')

@app.route('/predict',methods=['POST']) # POST method where in we will be providing some features to the model.pkl file so that it will take those inputs and give the output

def predict(): # This is a web API
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction
    


    my_dict = {1: 'Positive', 0: 'Negative'}
    output = np.vectorize(my_dict.get)(prediction[0])
    #output = prediction[0]

    return render_template('Index.html', prediction_text='Your result is  {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
