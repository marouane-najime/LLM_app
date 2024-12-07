import os
from dotenv import load_dotenv
import streamlit as st
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI LLM with the API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

chat_model = ChatOpenAI(api_key=api_key, model_name="gpt-4o-mini")

def create_prompt(user_input):
    template = """
    You are a helpful assistant.

    User: {user_input}
    Assistant:

    Format the output as JSON with the following keys:
    answer
    """
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template=template,
    )
    return prompt.format(user_input=user_input)

def main():
    st.title("ChatGPT Interface with Prompt Template")
    user_input = st.text_input("You:")
    if user_input:
        final_prompt = create_prompt(user_input)
        response = chat_model.invoke(final_prompt)
        st.write("Assistant:", response.content)

if __name__ == "__main__":
    main()