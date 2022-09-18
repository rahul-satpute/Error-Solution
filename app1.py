import joblib
from flask import Flask, request, render_template




app = Flask(__name__)

#load model
UScustoms_Model = joblib.load('UScustom_Model_Steps.sav')


@app.route('/')
def my_form():
    return render_template('form1.html')

@app.route('/', methods=['POST'])
def getSuggestions():
    error_message = request.form['error_message']
    X_val = error_message
    X_val = [X_val]

    Y_Classification = UScustoms_Model.predict(X_val)
    
    #return processed_text
    return render_template('form1.html',text=error_message, result = Y_Classification)

# main driver function
if __name__ == '__main__':
    app.run(debug=True)