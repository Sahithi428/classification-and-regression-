import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Student GPA Prediction", page_icon="🎓", layout="centered")

with open("model_regression.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler_regression.pkl", "rb") as file:
    scaler = pickle.load(file)

st.title("🎓 Student GPA Prediction")
st.write("Enter the student's details to predict GPA.")

age = st.number_input("Age", min_value=15, max_value=18, value=16)
gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
ethnicity = st.selectbox("Ethnicity", [0, 1, 2, 3])
parental_education = st.selectbox("Parental Education", [0, 1, 2, 3, 4])
study_time = st.number_input("Study Time Weekly (hours)", min_value=0.0, max_value=20.0, value=10.0)
absences = st.number_input("Absences", min_value=0, max_value=30, value=5)
tutoring = st.selectbox("Tutoring", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
parental_support = st.selectbox("Parental Support", [0, 1, 2, 3, 4])
extracurricular = st.selectbox("Extracurricular", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
sports = st.selectbox("Sports", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
music = st.selectbox("Music", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
volunteering = st.selectbox("Volunteering", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

if st.button("Predict GPA"):
    input_data = pd.DataFrame([[
        age, gender, ethnicity, parental_education, study_time, absences,
        tutoring, parental_support, extracurricular, sports, music, volunteering
    ]], columns=[
        "Age", "Gender", "Ethnicity", "ParentalEducation",
        "StudyTimeWeekly", "Absences", "Tutoring", "ParentalSupport",
        "Extracurricular", "Sports", "Music", "Volunteering"
    ])

    input_scaled = scaler.transform(input_data)
    prediction = float(model.predict(input_scaled)[0])
    prediction = max(0.0, min(4.0, prediction))

    st.success(f"Predicted GPA: {prediction:.2f} / 4.00")
