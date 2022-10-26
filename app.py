import streamlit as st
import numpy as np
import pandas as pd
import joblib 

rf = joblib.load('rf_bbry_tuned_model.pkl')

col = ['clonesize','osmia','AverageOfUpperTRange','AverageOfLowerTRange',
'AverageRainingDays','fruitset','fruitmass','seeds']
def prediction_yield( clonesize,osmia,AverageOfUpperTRange,AverageOfLowerTRange,AverageRainingDays,fruitset,fruitmass,seeds):

    prediction = rf.predict([[clonesize,osmia,AverageOfUpperTRange,AverageOfLowerTRange,AverageRainingDays,fruitset,fruitmass,seeds]])
    print('prediction done')
    return prediction

def main():

    st.header('Blueberry Yield Prediction App')

    clonesize = st.text_input('clonesize','clonesize value')
    osmia = st.text_input('osmia','osmia')
    AverageOfUpperTRange = st.text_input('avgutrange','avgutrange')
    AverageOfLowerTRange = st.text_input('avgltrange','avgltrange')
    AverageRainingDays= st.text_input('avgrainingdays','avgrainingdays')
    fruitset = st.text_input('fruitset','fruitset')
    fruitmass = st.text_input('fruitmass','fruitmass')
    seeds = st.text_input('seeds','seeds')
    pred=""


    if st.button('Predict Yield'):
        pred = prediction_yield(clonesize,osmia,AverageOfUpperTRange,AverageOfLowerTRange,AverageRainingDays,fruitset,fruitmass,seeds)

        st.success('The yield is {}'.format(pred))

if __name__ == '__main__':

    main()