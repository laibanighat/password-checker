import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔓 Password Strength Checker")
st.markdown("""
##WElcome to the ultimate password strength checker!👋
use this simple tool to check the strength of your password and get suggestion on how to make it stronger.
            we will give you helpfull tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
     feedback.append ("❌Password should be at least 8 character long.")
     
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]',password):
        score += 1 
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")

    if re.search(r'[0-9]', password):
        score += 1
    else :
        feedback.append("❌Password should contain at least  one digit.")

    if re.search(r'[!@#$%&^*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%^&*).")
    if score == 4:
        feedback.append("✅Your password is strong!🎉🎊")
    elif score == 3:
        feedback.append("🟡Your password is medium strength.It could be stronger.")
    else:
        feedback.append("🔴Your password is weak.Please make it stronger.")
    if feedback:
        st.markdown("## Improved Suggestion")    
        for tip in feedback:
            st.write(tip)
else:
    st.info ("Please enter your password to get started.")            

