import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from joblib import dump, load
from models import Diseases

def LSTM_Aditya():
    diseases=Diseases.query.all()
    print(diseases)
    #model = load_model()
    print("In LSTM")
    
def MLP_Aditya():
    #Add model loading based on disease
    clf = load('MLModels/MLP_Diarrhea.joblib')
    features=[44,44,44,45,45,45,45,47,48,49,50,54,55,56,57,57,56,57,57,58]
    labels=[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    pred=clf.predict(features)
    print(pred)
    #Add pred to db
    print("In MLP")