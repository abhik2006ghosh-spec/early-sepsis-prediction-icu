# Early Sepsis Prediction in ICU

Machine Learning and Streamlit Dashboard for early sepsis risk prediction in Intensive Care Units (ICU).

## Project Overview

This project aims to develop an AI-assisted early warning system for predicting sepsis risk in ICU patients.

The project combines machine learning, data analysis, model evaluation, explainable AI, and a clinician-facing Streamlit dashboard.

## Project Objectives

- Develop an early sepsis prediction system for ICU patients.
- Perform data preprocessing and exploratory data analysis.
- Engineer relevant features for machine learning.
- Develop and evaluate machine learning models.
- Use SHAP to explain model predictions.
- Build a Streamlit dashboard for displaying patient sepsis risk.

## Streamlit Dashboard

The dashboard is being developed as a clinician-facing interface.

Current pages:

- Home - Project introduction and dashboard overview.
- Risk Dashboard - Patient risk display, risk categories, patient information, and SHAP explanation placeholder.
- About - Project information and development status.

### Planned Risk Levels

- Low Risk
- Medium Risk
- High Risk

The final dashboard will display the predicted sepsis risk together with supporting information and model explanations.

## Project Structure

early-sepsis-prediction-icu/
|
+-- app/          - Streamlit application
+-- data/         - Project data
+-- docs/         - Project documentation
+-- models/       - Trained machine learning models
+-- notebooks/    - Jupyter notebooks
+-- outputs/      - Generated outputs
+-- src/          - Source code
+-- README.md     - Project documentation

## Current Status

### Week 1

- GitHub repository created.
- Project folder structure created.
- Streamlit environment configured.
- Initial Streamlit application created.
- Home, Risk Dashboard, and About pages created.
- Dashboard wireframe created.
- Low/Medium/High risk display planned.
- SHAP explanation section planned.
- Initial documentation created.

## How to Run the Streamlit Application

From the project directory, run:

python -m streamlit run app\app.py

The application will open in a web browser.

## Team Roles

The project is divided into the following areas:

- Member 1 - Data collection and preprocessing
- Member 2 - Exploratory data analysis and feature engineering
- Member 3 - Machine learning model development
- Member 4 - Model evaluation and SHAP explainability
- Member 5 - Streamlit deployment and documentation

## Development

The project uses Git and GitHub for version control and collaboration.

The Streamlit dashboard will later be integrated with the machine learning model and SHAP explanations.

## Disclaimer

This project is being developed for academic/project purposes. The dashboard is not intended to replace clinical judgment or professional medical decision-making.
