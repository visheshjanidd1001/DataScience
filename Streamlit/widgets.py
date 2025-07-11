import streamlit as st
import pandas as pd

st.title("Streamlit text input")


name = st.text_input("Enter your name:")


age = st.slider("Select your age: ,o,100,25")

st.write(f"Your age is {age}.")

options = ['Python','java','C++',"Javascript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}.")


if name:
    st.write(f"Hello, {name}")
    
data = {
    "Name": ['John','Jane','Jake','Jill'],
    "Age" : [28,24,25,34],
    "City" : ['New York','Los Angeles',"Chicago","Houston"]
    
}    

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
