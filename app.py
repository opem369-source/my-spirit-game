import streamlit as st
import google.generativeai as genai
import re
import json

st.set_page_config(page_title="靈氣覺醒: 模擬器", layout="centered")

st.title("🌱 靈氣覺醒：療癒生活")
api_key = st.sidebar.text_input("輸入你的 Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "你在山腰小木屋醒來，空氣充滿靈氣。門口的琉璃葉閃爍著微光，你感覺身心舒暢。現在想做什麼？"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("輸入你的行動..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            chat = model.start_chat(history=[])
            response = chat.send_message(f"你是一個靈氣復甦背景下的療癒遊戲主持人。請用平靜、沉浸的口吻，根據玩家的行動進行敘事。玩家行動: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("請在左側邊欄輸入你的 Gemini API Key 以開始遊戲。")
