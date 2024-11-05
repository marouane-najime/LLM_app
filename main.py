import os
from dotenv import load_dotenv
import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI LLM with the API key
api_key = os.getenv('OPENAI_API_KEY')
chat_model = ChatOpenAI(api_key=api_key, model_name="gpt-4o-mini")

# Define the prompt template
template = """
Speak to me in darija

User: {user_input}
Assistant:
"""

prompt = PromptTemplate(
    input_variables=["user_input"],
    template=template,
)

# Streamlit app
st.title("ChatGPT Interface with Prompt Template")

user_input = st.text_input("You:")

if user_input:
    final_prompt = prompt.format(user_input=user_input)
    response = chat_model.invoke(final_prompt)  # Use invoke method for chat model
    st.write("Assistant:", response)