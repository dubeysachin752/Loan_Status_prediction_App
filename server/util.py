# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:44:40 2020

@author: Mr. DUBEY
"""
import json
import pickle
import numpy as np
import os

__data_columns = None
__model = None

def get_estimated_loan_status(ApplicantIncome, CoapplicantIncome,
                        LoanAmount, LoanAmountTerm,
                        Gender, Married, Dependents, 
                        Education, SelfEmployed, CreditHistory,
                        PropertyArea):
    
    x = np.zeros(len(__data_columns))

    x[0] = Gender[0]
    x[1] = Married[0]
    x[2] = Dependents[0]
    x[3] = Education[0]
    x[4] = SelfEmployed[0]
    x[5] = ApplicantIncome[0]
    x[6] = CoapplicantIncome[0]
    x[7] = LoanAmount[0]
    x[8] = LoanAmountTerm[0]
    x[9] = CreditHistory[0]
    x[10] = PropertyArea
    
    response = __model.predict([x])
    if response == 1:
        response = 'Approved'
    else:
        response = 'Rejected'

    return response

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    
    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts")
    print(artifacts)
    with open(artifacts+"/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        
    global __model
    with open(artifacts+"/Loan_status_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

load_saved_artifacts()
    
#if __name__ == '__main__':
#   load_saved_artifacts()
#    print(get_estimated_loan_status(3000, 1500,
#                        500, 360,
#                       1, 1, 0, 
#                      1, 0, 1,
#                    2))           

