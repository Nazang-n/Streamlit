import streamlit as st 
st.title('Calculate App 007')
num1 = st.number_input('Enter your first number: ')
option = st.selectbox("Select Operator", ["+", "-", "*", "/" , "^"])
num2 = st.number_input('Enter your sec number: ')
# total = number1 + number2



if st.button("Calculate your number hear :"):
    if option == "+":
        result = num1 + num2
    elif option == "-":
        result = num1 - num2
    elif option == "*":
        result = num1 * num2
    elif option == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error"
    elif option == "^":
        result = num1 ** num2

    st.write(f"### Youe result is : {result}")
# if total:
#     st.success(f'Here is your result {total}')