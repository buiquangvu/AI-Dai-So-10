# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:40:43 2026

@author: Admin
"""

from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) or st.secrets.get("OPENAI_API_KEY")

def ask_ai(system, mode="hint"):
    prompt = f"Hệ bất phương trình: {system}"

    if mode == "hint":
        prompt += "\nGợi ý từng bước giải."
    elif mode == "short":
        prompt += "\nGiải ngắn gọn."
    elif mode == "detail":
        prompt += "\nGiải chi tiết."
    elif mode == "mistake":
        prompt += "\nCác sai lầm thường gặp."

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content