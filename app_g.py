from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as gn

gn.configure(api_key=os.getenv("make_api"))


# load gemini model
model = gn.GenerativeModel("gemini-pro")

def gemini_res(que):
    res = model.generate_content(que)
    return res.text


st.set_page_config(page_title="gemini chat")
st.header("Chat bot using gemini LLM")

input=st.text_input("Input: ", key="input")
submit = st.button("Ask me any question")


if submit:
    res = gemini_res(input)
    st.subheader(res)
    st.write(res)

else:
    st.write("something went wrong")
