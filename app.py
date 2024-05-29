import streamlit as st
import pandas as pd
import joblib

# Define the login page
def login_page():
    """Creates a login page with username and password."""
    st.title("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button('Login'):
        # Replace the following placeholder with your actual authentication logic
        if username == "admin" and password == "admin":
            st.session_state["authenticated"] = True
            st.success("You are logged in!")
            st.rerun()
        elif username and password:
            st.error("Invalid username or password")

# Load the pre-trained model (replace with your actual model)
def load_model():
    model_path = "Models.pkl"  # Verify the correct path
    try:
        model = joblib.load("C:\\Users\\Bunmi\\Documents\\Financial Inclusion\\model.pkl")
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Define the prediction page
def predict():
    model = load_model()  # Load the model when the user selects the "Prediction" page
    st.title("Financial Inclusion Prediction")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)

        data = data[['location_type', 'cellphone_access', 'household_size',
       'age_of_respondent', 'gender_of_respondent', 'relationship_with_head',
       'marital_status', 'education_level', 'job_type']]
        
        # Encoding categorical variables
        from sklearn.preprocessing import LabelEncoder

        label_encoder = LabelEncoder()
        data['location_type'] = label_encoder.fit_transform(data['location_type'])
        data['cellphone_access'] = label_encoder.fit_transform(data['cellphone_access'])
        data['gender_of_respondent'] = label_encoder.fit_transform(data['gender_of_respondent'])
        data['relationship_with_head'] = label_encoder.fit_transform(data['relationship_with_head'])
        data['marital_status'] = label_encoder.fit_transform(data['marital_status'])
        data['education_level'] = label_encoder.fit_transform(data['education_level'])
        data['job_type'] = label_encoder.fit_transform(data['job_type'])
        
        # Make predictions
        financial = model.predict(data) # Get probability of churn
        # Add churn probabilities as a new column to the DataFrame
        data['financial_inclusion'] = financial
        # Display the updated DataFrame
        st.dataframe(data)

        # Save predicted data with churn probability (optional)
        if st.button("Download Results"):
            data.to_csv("financial.csv", index=False)
            st.success("Prediction results downloaded!")

def main():
    """Main application structure."""
    if "authenticated" not in st.session_state:
        st.title("Financial Prediction App")
        login_page()
        return

    st.title("Financial Inclusion Prediction")
    st.write("Financial Inclusion ")

    page = st.sidebar.selectbox("Select a page", ["Home", "Prediction"])

    if page == "Home":
        st.header("About")
        st.write(
            "Financial Inclusion "
        )

    if page == "Prediction":
        predict()

if __name__ == "__main__":
    main()