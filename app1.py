import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Set API key from Streamlit secrets
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chat Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are an AI assistant.")]

user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=response.content))
    st.write("**AI:**", response.content)
    st.stop()
