import streamlit as st
import requests

st.title('💱 Currency Converter')

amount=st.number_input('Enter your number:',min_value=0.0)
from_currency=st.selectbox("From currency :",["USD", "EUR", "GBP", "INR"])
to_currency=st.selectbox('TO Currency:',["USD", "EUR", "GBP", "INR"])

if st.button("Convert"):
    if from_currency==to_currency:
        st.info("Same currency selected")
        st.write(f"Convert Amount :{amount:.2f} {to_currency}")
    else:
         url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
         response = requests.get(url)    
         if response.status_code==200:
             
          data=response.json()
          rate=data['rates'][to_currency]
          converted=amount*rate
          st.success(f"{amount:.2f} {from_currency}=={converted:.2f} {to_currency}")
         else:
             st.error("Failed to fetch") 