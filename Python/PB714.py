# BMI Calculator App
# Take user inputs:
# - Weight (kg) (number input)
# - Height (cm) (number input)
# On button click, calculate BMI = weight / (height/100)^2.
# - Display:
# - BMI Value
# - A health category (Underweight, Normal, Overweight, Obese)
# - Show results in colored messages (st.success(), st.warning(), st.error()).
import streamlit as st
st.title("BMI calculator")
w=st.number_input("Enter your weight (in kgs):")
h=st.number_input("Enter your height (in cms):")
if st.button("Get BMI value"):
    if h>0:
        bmi=w/(h/100)**2
        st.write(f"BMI:{bmi}")
        if bmi<18.5:
            st.error("Underweight")
        elif bmi>=18.5 and bmi<=24.9:
            st.success("Normal")
        elif bmi>=25 and bmi<=29.9:
            st.warning("Overweight")
        elif bmi>=30:
            st.error("Obese")
    else:
        st.error("Enter valid numeric values!")
