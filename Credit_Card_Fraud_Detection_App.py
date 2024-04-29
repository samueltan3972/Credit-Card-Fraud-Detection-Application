import pickle
import pandas as pd
import streamlit as st
import webbrowser as wb

from random import random, randrange
from sklearn.preprocessing import StandardScaler
from streamlit_javascript import st_javascript

filename = {
    "lr": "models/logistic_regression.sav",
    "rf": "models/random_forest.sav",
    "svm": "models/SVM.sav"
}

# max and min value based on dataset
max_val = [1.016482,-0.007194, 2.496266,-0.083724, 1.702777, 2.324816, 0.892615, 0.049100, 1.049921, 1.258025, 0.140107, 1.564246, 1.853521, 0.796567, 3.069025, 1.018496, 0.886526, 2.178616, 0.445316, 0.361652, 0.620676, 0.729727, 0.945045, 2.248754, 1.182503, 1.071126, 0.066681, 0.419117]
min_val = [-0.260648,-0.949385, 0.425786,-1.090178, 0.074062, 0.332371, 0.406466,-0.908409,-0.261297, 0.437518,-1.735016, 0.293438,-0.941386, 0.176637,-0.697664,-0.577514, 0.112419,-0.032928,-2.366079,-0.390343,-0.203634,-0.920426,-0.227779,-1.893131,-0.742075,-0.929738,-1.382522,-2.748268]

# utils function
def load_logistic_regression():
    return pickle.load(open(filename["lr"], "rb"))

def load_random_forest():
    return pickle.load(open(filename["rf"], "rb"))

def load_svm():
    return pickle.load(open(filename["svm"], "rb"))

def generate_random_input():
    """
    Generate random input for detection.
    
    Returns:
        pd.DataFrame: generated input
    """

    input = {f"V{i+1}":[random() * (max_val[i]-min_val[i]) + min_val[i]] for i in range(28)}
    input["Amount"] = [randrange(100, 9999999) / 100]
    
    return pd.DataFrame(data=input)

def generate_model_result(x=None):
    """
    Run the full pipeline of detection from generate input to getting model prediction.
    
    Args:
        x (pd.DataFrame, optional): input data. Defaults to None.

    Returns:
        dict: generated input and result of inference
    """

    lr_model = load_logistic_regression()
    rf_model = load_random_forest()
    svm_model = load_svm()

    x = x if x is not None else generate_random_input()

    # Data Preprocess
    sc = StandardScaler()
    x_scaled = sc.fit_transform(x) 
    x_scaled_df = pd.DataFrame(x_scaled, columns=x.columns)

    # Run inference
    lr_result = lr_model.predict(x_scaled_df)[0]
    rf_result = rf_model.predict(x_scaled_df)[0]
    svm_result = svm_model.predict(x_scaled_df)[0]
    
    return {"input": x, "lr_result": lr_result, "rf_result": rf_result, "svm_result":svm_result}


# Generate UI for application

st.title("Credit Card Fraud Detection")
st.text("This website is to show case the model trained for credit card fraud detection.")
st.image("img/scam_is_everywhere.png")

# Button Workflow
st.subheader("1. Generate Random Input")

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i, x=None):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Generate', on_click=set_state, args=[1])

# 1. Generate Random Input
if st.session_state.stage >= 1:
    if st.session_state.stage == 1:
        x = generate_random_input()
        st.session_state.x = x
    
    x = st.session_state.x
    st.dataframe(x)
    st.button('Generate', on_click=set_state, args=[1])

    st.subheader("2. Detect whether is Fraud")

    st.button('Detect', on_click=set_state, args=[2])

# 2. Inference
if st.session_state.stage >= 2:
    x = st.session_state.x
    result = generate_model_result(x)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(height=100):
            st.subheader("Logistic Regression")
        
        if result["lr_result"]:
            st.error('Alert! It may be a Fraud!', icon="❗")
        else:
            st.success('It is not Fraud', icon="✅")

    with col2:
        with st.container(height=100):
            st.subheader("Random Forest")
        
        if result["rf_result"]:
            st.error('Alert! It may be a Fraud!', icon="❗")
        else:
            st.success('It is not Fraud', icon="✅")

    with col3:
        with st.container(height=100):
            st.subheader("SVM")

        if result["svm_result"]:
            st.error('Alert! It may be a Fraud!', icon="❗")
        else:
            st.success('It is not Fraud', icon="✅")
    
    st.subheader("3. Start Over")

    if st.session_state.stage == 2:
        st.button('Start Over', on_click=set_state, args=[3, x])

# 3. Start Over
if st.session_state.stage >= 3:
    js = f'window.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "_blank").then(r => window.location.href);'
    st_javascript(js)

    st.image("img/scam.jpg")
    st.button('I TOLD YOU!', on_click=set_state, args=[0])