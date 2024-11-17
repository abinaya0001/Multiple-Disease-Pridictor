import os
import pickle
import streamlit as st
import streamlit_option_menu as som

# Set page configuration
st.set_page_config(
    page_title="Heart Cure 💉",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the saved models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f"{working_dir}/saved_models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open(f"{working_dir}/saved_models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open(f"{working_dir}/saved_models/parkinsons_model.sav", "rb"))

# Sidebar for navigation
with st.sidebar:
    st.title("Heart Cure 🩺")
    selected = som.option_menu(
        "Disease Prediction",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        menu_icon="hospital",
        icons=["activity", "heart", "person"],  # Use built-in Streamlit icons
        default_index=0,
    )

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("🩸 Diabetes Prediction using ML")
    st.write("Fill in the details below to predict if the person has diabetes.")
    st.markdown("---")

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0, step=0.1)
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value", min_value=0.0, step=0.1)
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value=0.0, step=0.1)
    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0.0, step=0.1)
    with col3:
        BMI = st.number_input("BMI Value", min_value=0.0, step=0.1)
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value", min_value=0.0, step=0.1)
    with col2:
        Age = st.number_input("Age of the Person", min_value=0, step=1)

    # Prediction logic
    if st.button("Diabetes Test Result 🔍"):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = "📢 The person is diabetic" if diab_prediction[0] == 1 else "🎉 The person is not diabetic"
            st.success(diab_diagnosis)
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("❤️ Heart Disease Prediction using ML")
    st.write("Provide the following information to predict heart disease.")
    st.markdown("---")

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=0, step=1)
    with col2:
        sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
    with col3:
        cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0, step=0.1)
    with col2:
        chol = st.number_input("Serum Cholesterol in mg/dl", min_value=0.0, step=0.1)
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
    with col1:
        restecg = st.selectbox("Resting Electrocardiographic Results (0-2)", [0, 1, 2])
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0.0, step=0.1)
    with col3:
        exang = st.selectbox("Exercise-Induced Angina (1 = Yes, 0 = No)", [0, 1])
    with col1:
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, step=0.1)
    with col2:
        slope = st.selectbox("Slope of the Peak Exercise ST Segment (0-2)", [0, 1, 2])
    with col3:
        ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4, step=1)
    with col1:
        thal = st.selectbox("Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)", [0, 1, 2])

    # Prediction logic
    if st.button("Heart Disease Test Result 🔍"):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = "📢 The person has heart disease" if heart_prediction[0] == 1 else "🎉 The person does not have heart disease"
            st.success(heart_diagnosis)
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.title("🧠 Parkinson's Disease Prediction using ML")
    st.write("Enter the required details to check for Parkinson's disease.")
    st.markdown("---")

    # Input fields
    cols = st.columns(5)
    parkinsons_fields = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
        "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]
    user_input = []

    for i, field in enumerate(parkinsons_fields):
        with cols[i % 5]:
            user_input.append(st.number_input(field, value=0.0, step=0.1))

    # Prediction logic
    if st.button("Parkinson's Test Result 🔍"):
        try:
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = "📢 The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "🎉 The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
