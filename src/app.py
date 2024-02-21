# Importing packages
import streamlit as st
import pandas as pd
import joblib
import warnings 
warnings.filterwarnings("ignore")

# Setting the app title
st.title('PS/PMMA Blend Morphology Classifier')
st.write('A machine learning model that predicts the morphology of a PS/PMMA blend')

#Prediction method
def make_prediction(values):
    classifier=joblib.load('./Model/model.joblib')
    #st.write("The values you have provided after scaling: ")
    #st.write(values[0])
    #st.write(values[1])
    #st.write(values[2])
    #st.write(values[3])
    data=pd.DataFrame([values])
    prediction=classifier.predict(data)
    if prediction==0:
        prediction='Column'
    elif prediction==1:
        prediction='Hole'
    else:
        prediction='Island'
    
    #Displaying the results
    st.write('The predicted morphology for this PS/PMMA blend is: ', prediction)    

# Declare a form to receive the variables to input into the model
form = st.form(key='Input values to the model')
initialtext1=0
conc=form.number_input(label="Concentration of PS/PMMA Blend (%)", step=0.01)
comp=form.number_input(label="Composition(PS/PMMA ratio)", step=0.01)
pmmawt=form.number_input(label="PMMA Molecular Weight (Da)", step=0.01)
ssenergy=form.number_input(label="Subscrate Surface Energy (mJ/m^2)", step=0.01)

if conc == "":
    st.write(initialtext1, style="color: lightgray")
if comp == "":
    st.write(initialtext1, style="color: lightgray")
if pmmawt == "":
    st.write(initialtext1, style="color: lightgray") 
if ssenergy == "":
    st.write(initialtext1, style="color: lightgray")    

#Making necessary changes to input
pmmawt=pmmawt/10**6
ssenergy=ssenergy/100
#Submit button
submit = form.form_submit_button(label='Predict')
if submit:
    values=[conc,comp,pmmawt,ssenergy]
    if conc==0 or comp==0 or pmmawt==0 or ssenergy==0:
        st.write('<span style="font-size:18px;">One or more of the inputs is empty, please enter them</span>', unsafe_allow_html=True)
    else:
        make_prediction(values)
    

st.image('./Image/BITS_LOGO.jpg')
st.write('')
st.write('<span style="font-size:18px;">Thank you for using our model. This ML model was developed by Bishnu R under the supervision of Professor Arnab Dutta (in collaboration with Professor Nandini Bhandaru) of BITS Pilani, Hyderabad Campus. This webapp can be used to predict morphologies of PS/PMMA blends. The classes being predicted are - Column, Hole and Island.</span>', unsafe_allow_html=True)
st.write('<span style="font-size:18px;">The input requirements are as follows:</span>', unsafe_allow_html=True)
st.write('<span style="font-size:18px;">1. The concentration must be input as %</span>', unsafe_allow_html=True)
st.write('<span style="font-size:18px;">2. The composition values must lie between 0 and 1</span>', unsafe_allow_html=True)
st.write('<span style="font-size:18px;">3. The PMMA molecular weight must be input in the units of Da</span>', unsafe_allow_html=True)
st.write('<span style="font-size:18px;">4. The subscrate surface energy must be input in the units of mJ/meter squared</span>', unsafe_allow_html=True)
st.write('<span style="font-size:20px;">This webapp has been developed as a part of academic work. We take no responsibility for any damages that may result from its use.</span>', unsafe_allow_html=True)
st.write('<span style="font-size:20px;">For any queries, please send an email to - f20201934@hyderabad.bits-pilani.ac.in or arnabdutta@hyderabad.bits-pilani.ac.in</span>', unsafe_allow_html=True)

#st.caption("This ML model was developed by Bishnu R under the supervision of Professor Arnab Dutta (in collaboration with Professor Nandini Bhandaru) of BITS Pilani, Hyderabad Campus.")
#st.caption("This webapp can be used to predict morphologies of PS/PMMA blends.")
#st.caption("The classes being predicted are - Column, Hole and Island")
#st.caption("The input requirements are as follows -")
#st.caption("The concentration must be input as %")
#st.caption("The composition values must lie between 0 and 1 ")
#st.caption("The PMMA molecular weight must be input in the units of Da")
#st.caption("The subscrate surface energy must be input in the units of mJ/meter squared")
#print("")



