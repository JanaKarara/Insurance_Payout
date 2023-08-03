import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

insurance = pd.read_csv('insurance.csv')

st.header("Insurance Payout Analysis")
st.subheader('Data was analyised to figure out how different client cases affect the charges payed for insurance ')

st.divider()  



col1,col2 = st.columns(2)

with col1:
    st.markdown('This graph shows the health status of our insurance clients , which shows that most of our clients are obesie')
    

with col2:
    st.write(px.bar(insurance,x='bmi_categ',title="Clients status"))

    
st.markdown('CHOOSE THE ASPECT THAT WILL SHOW HOW IT AFFECTS THE CHARGES PAYED')
    

    
BMI_Category, Region, Age, Gender, Smoking_Status = st.tabs(["BMI Category", "Region", "Age", "Gender", "Smoking Status" ])

with BMI_Category:
    choosen = st.selectbox('choose the type of graph you want to see', ["Violin plot","Bar plot"])
    col1,col2 = BMI_Category.columns(2)
    with col1:
        st.markdown("It is shown that obesie clients are the ones who pay more insurance charges and the least paying client is the                                                underweight one.")
        if choosen =="Violin plot":
            with col2:
                st.write( px.violin(insurance, x='bmi_categ', y='charges', box=True,title='How BMI category affect the charges paid'))
        else:
            with col2:
                 st.write( px.bar(insurance,x='bmi_categ',y='charges',title="Charges based on category"))
    
       
with Region:
    
    choosen = st.selectbox('choose the type of graph you want to see', ["Strip plot","Histogram "])
    col1,col2 = Region.columns(2)
    with col1:
        st.markdown("It is shown that Northeast region pay the highest insurance charges unlike the other regions. Also it is shown that                                  Southeast and Southwest regions pay closer charges ")
        if choosen =="Strip plot":
            with col2:
                 st.write(px.strip(insurance, x="region", y="charges",title='how the region affect the charges'))        
        else:
            with col2:
                 st.write(px.histogram(insurance, x="region", y="charges",title='how the region affect the charges'))
    

with Age:
    col1,col2 = Age.columns(2)
    age_insurance_avg = insurance.groupby('age')[['charges']].mean().reset_index().rename(columns={'age': 'age', 'charges':                                  'Average charges'})    
    with col1:
        st.write('The graph shows that the younger the client is the higher the charges they pay')
    with col2:    
        st.write(px.line(age_insurance_avg, x= 'age', y = 'Average charges'))
    
    

with Gender:
    col1,col2 = Gender.columns(2)
    with col1:
        st.markdown("Insurance payout has no gender discrimination as shown through the graph where both femaale and male pay equally                                according  to simialr cases not gender")
    with col2:
        
        st.write(st.write( px.bar(insurance, x="sex", y="charges",color='smoker', barmode='group',height=400)))
        
       


        
with Smoking_Status:
    col1,col2 = Smoking_Status.columns(2)
    smoking_insurance_avg = insurance.groupby('smoker')[['charges']].mean().reset_index().rename(columns={'smoker': 'smoker', 'charges':                                  'Average charges'})    
    with col1:
        st.write('The graph shows that smokers are used to pay higher insurance payout than non-smokers')
        
    with col2:
        st.write(px.histogram(smoking_insurance_avg, x= 'smoker', y = 'Average charges'))
        
        
        
        
        
        
        
        

       
            

    