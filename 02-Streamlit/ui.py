import streamlit as st
import requests

API_URL = "http://localhost:8000"

# -------------------------------
# LOGIN SYSTEM
# -------------------------------


def login_screen():
    st.title("Smart Patient Segmentation – Login")

    role = st.selectbox("Select Role", ["Admin", "Manager"])
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if password == "admin123" and role == "Admin":
            st.session_state.logged_in = True
            st.session_state.role = "Admin"
        elif password == "manager123" and role == "Manager":
            st.session_state.logged_in = True
            st.session_state.role = "Manager"
        else:
            st.error("Invalid credentials!")


# -------------------------------
# MAIN DASHBOARD
# -------------------------------
def dashboard():
    st.title("🏥 Smart Patient Segmentation Platform")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Menu", ["Add Patient", "Dashboard", "Export Data"])

    if page == "Add Patient":
        add_patient_form()

    if page == "Dashboard":
        display_dashboard()

    if page == "Export Data":
        export_ui()


# -------------------------------
# ADD PATIENT FORM
# -------------------------------
def add_patient_form():
    st.subheader("➕ Add Patient")

    name = st.text_input("Patient Name")
    heart_rate = st.number_input("Heart Rate (bpm)", 0, 200)
    systolic = st.number_input("Systolic BP", 0, 200)
    diastolic = st.number_input("Diastolic BP", 0, 200)
    temperature = st.number_input("Temperature (°C)", 30.0, 45.0)
    post_op = st.checkbox("Post-Operative Patient?")
    icu_required = st.checkbox("ICU Required?")
    mode = st.selectbox("Classification Mode", ["rule", "llm"])

    if st.button("Classify Patient"):
        payload = {
            "name": name,
            "heart_rate": heart_rate,
            "systolic": systolic,
            "diastolic": diastolic,
            "temperature": temperature,
            "post_op": post_op,
            "icu_required": icu_required,
            "mode": mode
        }

        response = requests.post(f"{API_URL}/classify", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Patient classified as **{result['category']}**")
        else:
            st.error("Error connecting to backend!")


# -------------------------------
# DASHBOARD TABLE
# -------------------------------
def display_dashboard():
    st.subheader("📊 Classified Patients")

    try:
        data = requests.get(f"{API_URL}/export/csv")  # triggers export
        with open("patient_export.csv") as f:
            import pandas as pd
            df = pd.read_csv(f)
        st.dataframe(df)
    except:
        st.error("No data found or backend not reachable.")


# -------------------------------
# EXPORT OPTIONS
# -------------------------------
def export_ui():
    st.subheader("⬇ Export Data")

    if st.button("Export CSV"):
        requests.get(f"{API_URL}/export/csv")
        st.success("CSV Exported successfully!")

    if st.button("Export PDF"):
        requests.get(f"{API_URL}/export/pdf")
        st.success("PDF Exported successfully!")


# -------------------------------
# APP ENTRY POINT
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_screen()
else:
    dashboard()
