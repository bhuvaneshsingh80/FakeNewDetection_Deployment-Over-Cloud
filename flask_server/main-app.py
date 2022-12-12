import numpy as np
from flask import Flask, request, render_template
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import pad_sequences

app = Flask(__name__)
model = load_model('rnn_model_fake_real_text_classification.hdf5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():    

    tok = Tokenizer(num_words=100)
    input_text = request.form.values()
    input_sequences = tok.texts_to_sequences(input_text)
    input_sequences_matrix = keras.utils.pad_sequences(input_sequences,maxlen=100)
    prediction = model.predict(input_sequences_matrix,0)
    if prediction < 0.5
        prediction_text='Fake'
    else 
        prediction_text='Real'

    return render_template('index.html', output='As per the model the statement is :{}'.prediction_text)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    #app.run(debug=True)
    
    
    

    