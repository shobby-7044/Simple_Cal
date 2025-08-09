import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter the first number here:")
num2 = st.number_input("Enter the second number here:")

operation = st.selectbox("Choose operation",['Add','Subtract','Multiplication','Division'])

if st.button("Calculate"):
    if operation == 'Add':
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == 'Subtract':
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == 'Multiplication':
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == 'Division':
        if num2 or num1 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Error: Can not divided by zero")
            
                   