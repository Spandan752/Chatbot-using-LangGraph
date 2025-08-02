import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}
# Testing the chatbot with Streamlit
# with st.chat_message("user"):
#     st.text("Hello!")

# with st.chat_message("assitant"):
#     st.text("Hi there! How can I assist you today?")


# user_input = st.chat_input("Type here...")

# if user_input:
#     with st.chat_message("user"):
#         st.text(user_input)

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_input = st.chat_input("Type here...")

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.text(message['content'])

if user_input:
    # saving the user input to chat history
    st.session_state['messages'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # saving the user input to chat history - this is for dummy chatbot response
    # st.session_state['messages'].append({'role': 'assistant', 'content': user_input})
    # with st.chat_message("assistant"):
    #     st.text(user_input)

    # invoking the chatbot
    response = chatbot.invoke({"messages": [HumanMessage(content=user_input,)]},config=CONFIG)
    ai_message = response['messages'][-1].content

    st.session_state['messages'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message("assistant"):
        st.text(ai_message)

