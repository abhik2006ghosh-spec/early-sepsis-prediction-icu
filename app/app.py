import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Early Sepsis Prediction",
    page_icon="🏥",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("🏥 Sepsis Prediction")
st.sidebar.write("Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["Home", "Risk Dashboard", "About"]
)

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":

    st.title("Early Sepsis Prediction in ICU")

    st.write(
        "AI-assisted early warning system for sepsis risk prediction."
    )

    st.info(
        "This dashboard is designed to support early identification "
        "of patients at risk of sepsis in the ICU."
    )

    st.subheader("Dashboard Overview")

    st.write(
        "Use the navigation menu on the left to view the "
        "Risk Dashboard and project information."
    )


# -------------------------
# RISK DASHBOARD PAGE
# -------------------------
elif page == "Risk Dashboard":

    st.title("📊 Risk Dashboard")

    st.subheader("Patient Sepsis Risk")

    st.info(
        "The machine learning model will provide the patient's "
        "sepsis risk after model integration."
    )

    # Main risk display
    st.markdown("### Current Risk Level")

    risk_col1, risk_col2, risk_col3 = st.columns(3)

    with risk_col1:
        st.metric(
            label="Risk Level",
            value="Not Available"
        )

    with risk_col2:
        st.metric(
            label="Risk Score",
            value="—"
        )

    with risk_col3:
        st.metric(
            label="Prediction Status",
            value="Waiting"
        )

    # Patient information
    st.markdown("---")

    st.subheader("Patient Information")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Heart Rate", "— bpm")

    with col2:
        st.metric("Temperature", "— °C")

    with col3:
        st.metric("Blood Pressure", "— mmHg")

    with col4:
        st.metric("Respiratory Rate", "— /min")

    # Risk categories
    st.markdown("---")

    st.subheader("Risk Categories")

    low_col, medium_col, high_col = st.columns(3)

    with low_col:
        st.write("🟢 **Low Risk**")
        st.write("Lower predicted risk of sepsis.")

    with medium_col:
        st.write("🟡 **Medium Risk**")
        st.write("Moderate predicted risk of sepsis.")

    with high_col:
        st.write("🔴 **High Risk**")
        st.write("Higher predicted risk of sepsis.")

    # SHAP explanation
    st.markdown("---")

    st.subheader("🔍 SHAP Explanation")

    st.info(
        "SHAP-based model explanations will be displayed here "
        "to show which patient features contribute to the prediction."
    )

    st.write("Features increasing risk: —")

    st.write("Features decreasing risk: —")


# -------------------------
# ABOUT PAGE
# -------------------------
elif page == "About":

    st.title("ℹ️ About")

    st.subheader("Early Sepsis Prediction in ICU")

    st.write(
        "This project aims to develop an AI-assisted early warning "
        "system for predicting sepsis risk in intensive care unit "
        "patients."
    )

    st.subheader("Project Status")

    st.write(
        "The Streamlit dashboard is currently under development."
    )