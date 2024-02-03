import streamlit as st
from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import joblib

model = joblib.load('score2.joblib')
st.title('Will you survive if you were among Titanic passengers or not :ship:')

hour =  st.number_input("“Input Hours Study In Day”",step=1.,format="%.2f")
practice =  st.number_input("“Input Hours practice In Day”",step=1.,format="%.2f")
teamwork =  st.number_input("“Input Hours TeamWork In Day”",step=1.,format="%.2f")
score = st.number_input("Input Score Estimate", 0,100) 


def predict(): 
    row = np.array([hour,practice,teamwork]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    st.write(prediction)
trigger = st.button('Predict', on_click=predict)

email='alikaku@yahoo.com'
