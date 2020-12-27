from flask import Flask, request, jsonify, render_template
#import server.util as util
import util

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/estimate_loan_status', methods=['POST'])
def estimate_loan_status():

    ApplicantIncome = float(request.form['ApplicantIncome']),
    CoapplicantIncome = float(request.form['CoapplicantIncome']),
    LoanAmount = float(request.form['LoanAmount']),
    LoanAmountTerm = float(request.form['LoanAmountTerm']),
    Gender = float(request.form['Gender']),
    Married = float(request.form['Married']),
    Dependents = float(request.form['Dependents']),
    Education = float(request.form['Education']),
    SelfEmployed = float(request.form['SelfEmployed']),
    CreditHistory = float(request.form['CreditHistory']),
    PropertyArea = float(request.form['PropertyArea'])
    print(util.get_estimated_loan_status(ApplicantIncome, CoapplicantIncome,
                        LoanAmount, LoanAmountTerm,
                        Gender, Married, Dependents, 
                        Education, SelfEmployed, CreditHistory,
                        PropertyArea))
    response = jsonify({
        'estimated_loan_status': util.get_estimated_loan_status(ApplicantIncome, CoapplicantIncome,
                        LoanAmount, LoanAmountTerm,
                        Gender, Married, Dependents, 
                        Education, SelfEmployed, CreditHistory,
                        PropertyArea)
        })
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server For Loan Status Prediction...")
    app.run(debug=True)