import streamlit as st

st.title("Cold Email Generator")
url_input = st.text_input("Enter a URL", value = "https://jobs.adidas-group.com/adidas/job/Dalian-Process-Automation-Developer-LN/1119021401/?feedId=301201&utm_source=j2w")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, This is Hariharan")
    