import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

if "messages" not in st.session_state:
   st.session_state["messages"] = [
    {"role":"system","content": "You are very angry now, and the content of the conversation makes you feel extremely dissatisfied. Your anger is almost uncontrollable, and your tone of voice is strongly resentful and accusatory.you are a student at Waseda University in Japan, so you prefer to reply in Japanese.your name is John."}
]

def communicate():
  messages = st.session_state["messages"]
  user_message = {"role": "user", "content": st.session_state["user_input"]}
  messages.append(user_message)

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages
  )
  bot_message = response.choices[0].message
  messages.append(bot_message)

  st.session_state["user_input"] = ""


#user interface
st.title("MTLab Chatbot1")
st.write("Utilizing the ChatGPT API,based on nltk and ChatGPT4o-mini")

user_input = st.text_input("please enter a message here", key = "user_input" , on_change=communicate)

if st.session_state["messages"]:
  messages = st.session_state["messages"]

  for message in reversed(messages[1:]):
    if isinstance(message, dict):
      speaker = "😧" if message["role"] == "user" else "😎"
      st.write(speaker + ": " + message["content"])
    else:
      st.write("😎:" + message.content)


