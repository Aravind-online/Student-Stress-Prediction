import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Student Depression Prediction",
    page_icon="🧠"
)

st.title("🧠 Student Depression Prediction")
st.write("Enter student details to predict depression risk.")

# Inputs
age = st.slider("Age", 16, 35, 20)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

financial_stress = st.slider(
    "Financial Stress",
    0,
    5,
    2
)

work_pressure = st.slider(
    "Work Pressure",
    0,
    5,
    2
)

anxiety = st.selectbox(
    "Anxiety",
    ["No", "Yes"]
)

insomnia = st.selectbox(
    "Insomnia",
    ["No", "Yes"]
)

# Predict Button
if st.button("Predict"):

    # Create 30 features (same count used during training)
    data = [0] * 30

    # Fill a few important features
    data[0] = age

    data[1] = 1 if gender == "Male" else 0

    data[10] = financial_stress

    data[15] = work_pressure

    data[20] = 1 if anxiety == "Yes" else 0

    data[25] = 1 if insomnia == "Yes" else 0

    prediction = model.predict([data])

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ High Depression Risk")

        st.markdown("""
### Recommendations

✅ Get proper sleep

✅ Exercise regularly

✅ Reduce academic pressure

✅ Talk with friends and family

✅ Seek professional help if needed
""")

    else:
        st.success("✅ Low Depression Risk")

        st.markdown("""
### Healthy Habits

✅ Maintain good sleep

✅ Stay active

✅ Keep social connections

✅ Manage stress properly
""")