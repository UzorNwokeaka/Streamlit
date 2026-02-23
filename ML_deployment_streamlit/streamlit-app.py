###
# Code originally written by Harry Wang (https://github.com/harrywang/mini-ml/)
# It was modified for the purpose of teaching how to deploy a machine learning 
# model using Streamlit.
###

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import joblib

# # load your machine learning model
# tree_clf = joblib.load(r"C:\Users\USER\OneDrive\Documents\Streamlit\ML_deployment_streamlit\model_dt.pickle")

# ### Streamnlit app code starts here

# st.title('Titanic Survival Prediction')
# st.markdown('**Please provide passenger information**:')  # you can use markdown like this

# # get inputs
# sex = st.selectbox('Sex', ['female', 'male'])
# age = int(st.number_input('Age:', min_value=0, max_value=100, value=20))
# sib_sp = int(st.number_input('# of siblings / spouses aboard:', min_value=0, max_value=100, value=0))
# pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
# fare = int(st.number_input('# of parents / children aboard:', min_value=0, max_value=1000, value=0))

# # this is how to dynamically change text
# prediction_state = st.markdown('calculating...')

# ### Now the inference part starts here

# passenger = pd.DataFrame(
#     {
#         'Pclass': [pclass],
#         'Sex': [sex], 
#         'Age': [age],
#         'SibSp': [sib_sp],
#         'Fare': [fare]
#     }
# )

# y_pred = tree_clf.predict(passenger)

# # Preparing the message to be displayed based on the prediction
# if y_pred[0] == 0:
#     msg = 'This passenger is predicted to be: **died**'
# else:
#     msg = 'This passenger is predicted to be: **survived**'

# ### Now add the prediction result to the Streamlit app

# prediction_state.markdown(msg)


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import joblib

# # load your machine learning model
# tree_clf = joblib.load(r"C:\Users\USER\OneDrive\Documents\Streamlit\ML_deployment_streamlit\model_dt.pickle")

# ### Streamlit app code starts here
# st.title('Titanic Survival Predictor')
# st.markdown('**Please provide passenger information**:')

# # Use a form to prevent constant reruns
# with st.form('inputs'):
#     sex = st.selectbox('Sex', ['female', 'male'])
#     age = int(st.number_input('Age:', min_value=0, max_value=100, value=20))
#     sib_sp = int(st.number_input('# of siblings / spouses aboard:', min_value=0, max_value=100, value=0))
#     pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
#     fare = int(st.number_input('# of parents / children aboard:', min_value=0, max_value=1000, value=0))

#     submitted = st.form_submit_button('Predict')

# # Only run inference when the user clicks Predict
# if submitted:
#     passenger = pd.DataFrame(
#         {
#             'Pclass': [pclass],
#             'Sex': [sex],
#             'Age': [age],
#             'SibSp': [sib_sp],
#             'Fare': [fare]
#         }
#     )

#     y_pred = tree_clf.predict(passenger)

#     if y_pred[0] == 0:
#         st.success('This passenger is predicted to be: **died**')
#     else:
#         st.success('This passenger is predicted to be: **survived**')
# else:
#     st.info("Fill in the inputs and click **Predict** to see the result.")



# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import joblib

# # load your machine learning model
# tree_clf = joblib.load(r"C:\Users\USER\OneDrive\Documents\Streamlit\ML_deployment_streamlit\model_dt.pickle")

# ### Streamlit app code starts here
# st.title('Titanic Survival Predictor - by Uzor Nwokeaka')
# st.markdown('**Please provide passenger information**:')

# # Form (prevents auto rerun)
# with st.form('inputs'):
#     sex = st.selectbox('Sex', ['female', 'male'])
#     age = int(st.number_input('Age:', min_value=0, max_value=100, value=20))
#     sib_sp = int(st.number_input('# of siblings / spouses aboard:', min_value=0, max_value=100, value=0))
#     pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
#     fare = int(st.number_input('# of parents / children aboard:', min_value=0, max_value=1000, value=0))

#     submitted = st.form_submit_button('Predict')

# # Run prediction only when button is clicked
# if submitted:
#     passenger = pd.DataFrame(
#         {
#             'Pclass': [pclass],
#             'Sex': [sex],
#             'Age': [age],
#             'SibSp': [sib_sp],
#             'Fare': [fare]
#         }
#     )

#     # Prediction
#     y_pred = tree_clf.predict(passenger)

#     # Probability (only if model supports it)
#     try:
#         proba = tree_clf.predict_proba(passenger)

#         # Message
#         if y_pred[0] == 0:
#             msg = 'This passenger is predicted to be: **died**'
#         else:
#             msg = 'This passenger is predicted to be: **survived**'

#         st.success(msg)

#         # Show probability of survival (class 1)
#         st.markdown(f'The survival probability: **{proba[0][1]:.2f}**')

#     except:
#         st.warning("This model does not support probability prediction.")

# else:
#     st.info("Fill in the inputs and click **Predict** to see the result.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# ----------------------------
# Simple login (password gate)
# ----------------------------
APP_PASSWORD = "titanic123"  # <-- change this to your own password

def check_password() -> bool:
    """Returns True if the user entered the correct password."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.title("Login")
    pw = st.text_input("Enter password to access the app", type="password")
    if st.button("Login"):
        if pw == APP_PASSWORD:
            st.session_state.authenticated = True
            st.success("Login successful.")
            st.rerun()
        else:
            st.error("Incorrect password. Try again.")
    st.stop()


check_password()

# ----------------------------
# Load model
# ----------------------------
tree_clf = joblib.load(
    r"C:\Users\USER\OneDrive\Documents\Streamlit\ML_deployment_streamlit\model_dt.pickle"
)

# ----------------------------
# App UI
# ----------------------------
st.title("Titanic Survival Predictor App")
st.markdown("<h2>Developed by Uzor Nwokeaka</h4>", unsafe_allow_html=True)
st.markdown("**Please provide passenger information**:")

with st.form("inputs"):
    sex = st.selectbox("Sex", ["female", "male"])
    age = int(st.number_input("Age:", min_value=0, max_value=100, value=20))
    sib_sp = int(
        st.number_input("# of siblings / spouses aboard:", min_value=0, max_value=100, value=0)
    )
    pclass = st.selectbox("Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
    fare = int(st.number_input("Fare:", min_value=0, max_value=1000, value=32))

    submitted = st.form_submit_button("Predict")

# ----------------------------
# Prediction + probability
# ----------------------------
if submitted:
    passenger = pd.DataFrame(
        {
            "Pclass": [pclass],
            "Sex": [sex],
            "Age": [age],
            "SibSp": [sib_sp],
            "Fare": [fare],
        }
    )

    y_pred = tree_clf.predict(passenger)

    # Message
    if y_pred[0] == 0:
        msg = "This passenger is predicted to be: **died**"
    else:
        msg = "This passenger is predicted to be: **survived**"

    st.success(msg)

    # Probability (if supported)
    try:
        proba = tree_clf.predict_proba(passenger)
        st.markdown(f"The survival probability: **{proba[0][1]:.2f}**")
    except Exception:
        st.warning("This model does not support probability prediction (predict_proba).")
else:
    st.info("Fill in the inputs and click **Predict** to see the result.")

# ----------------------------
# About the model section
# ----------------------------
with st.expander("About the model"):
    st.markdown(
        """
**Training data size:** ~891 rows (Titanic training dataset)

**Target:** Survived (0 = No, 1 = Yes)

**Features used in this app:**
- Pclass (ticket class)
- Sex
- Age
- SibSp (siblings/spouses aboard)
- Fare

**Last training date: February 23, 2026

** Version of Model : v1.5

**Potential limitations:**
- Titanic dataset is small and may not generalize beyond that specific historical context.
- Missing values (e.g., Age) may be imputed; this can affect predictions.
- Model performance depends on the preprocessing used during training (encoding, imputation, etc.).
- Inputs outside the range seen in training data can lead to unreliable predictions.
"""
    )