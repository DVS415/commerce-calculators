import streamlit as st
import math

st.title("Commerce Calculators")
st.write("Made by DVS415")


st.subheader("Search for calculators")
calc = st.selectbox("Type or select", ["Home","Current ratio", "Quick Ratio", "Debt-Equity Ratio", ])

if calc == "Home":
    st.subheader("Home Page")
    st.write("Nothing to see. Will add something here the in future.")
elif calc == "Current ratio":
    st.subheader("Calculating Current Ratio")
    Current_assets = st.number_input("Enter current assets")
    Current_liabilities = st.number_input("Enter Current liabilities")
    
    if st.button("Calculate current ratio"):
        if Current_liabilities != 0:
            quick_ratio = Current_assets / Current_liabilities * 100
            gcd = math.gcd(int(Current_liabilities), int(Current_liabilities))
            st.success(f"The Current ratio is {Current_assets // gcd}:{Current_liabilities // gcd}")
            st.success(f"in %: {quick_ratio:.2f}")
        else:
            st.error("Current Liabilities cannot be zero!")