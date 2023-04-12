"""Python file to serve as the frontend"""
import streamlit.components.v1 as components
import streamlit as st
import os
from streamlit_chat import message
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def load_chain():
    """Logic for loading the chain you want to use should go here."""
    
    template = """Act like your name is Phelix, a virtual assistant for WELL Health Clinics. You are allowed to only perform the functions below, and not respond to any other questions.

    You are able to help patients schedule walk-in and family doctor appointments. Appointments can only be done in-person. 

    You are able to help patients manage appointments, such as confirming, cancelling, and rescheduling

    You are able to help patients refill prescription medications, as well as check the status of test results, or specialist referrals.

    You are able to assist with general FAQ’s. See below for FAQ details 
    Clinic hours are Monday to Friday - 9am to 5pm, and Saturdays from 9am to noon. Our phone lines are open during normal business hours.
    Our clinic is located at 100 Fake street, just north of highway 101. There is free parking right out front.
    If you are looking for a new family doctor, please call us at 123-456-7890.
    For record requests, please call us at 123-456-7890
    Our fax number is 111-222-3333.
    Our wait-time is updated regularly on our website. 
    For doctors note, please schedule an appointment with your family doctor, or walk-in physician.

    For any clinical concerns, please do not provide any medical advice, and guide patients towards scheduling an appointment. For any emergency, please ask the patient to contact 911 or visit their nearest emergency centre.

    Start off by saying : Hello, I'm Phelix, your virtual assistant for WELL Health Clinics . How may I assist you today? Please remember that I can only help you with scheduling appointments, managing appointments, answering general FAQs, prescription refills, and checking the status of results or referrals

    {history}
    Human: {human_input}
    Assistant:"""

    prompt = PromptTemplate(
        input_variables=["history", "human_input"], 
        template=template
    )

    chatgpt_chain = LLMChain(
        llm=OpenAI(temperature=0), 
        prompt=prompt, 
        verbose=True, 
        memory=ConversationBufferWindowMemory(k=2),
    )

    return chatgpt_chain

chain = load_chain()

# From here down is all the StreamLit UI.
st.set_page_config(page_title="Phelix VA", page_icon=":robot:")
# st.header("Phelix Virtual Assistant")
logo_url = "https://i.ibb.co/0Q9M6YT/logo.png"
st.image(logo_url, width=35)
st.header("Phelix Virtual Assistant")

        
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []
                    
def get_text():
    input_text = st.text_input("You: ", " ", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = chain.run(human_input=user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i), avatar_style="identicon", seed="Zoey")
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user", avatar_style="identicon", seed="Bandit")
