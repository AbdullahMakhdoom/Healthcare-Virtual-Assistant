# Felix Healthcare Virtual Assistant

 This repository contains the development of an MVP for a Virtual Assistant named Felix, who will assist patients in their checkup journey. 
 Felix can help patients with the following tasks:

- Schedule walk-in and family doctor appointments.
- Manage appointments, such as confirming, cancelling and rescheduling.
- Answer general FAQs such as hours of operations, parking, or other inquiries.
- Assist with prescription refills for patients.
- Check the status of results or referrals.

## Tools & Technologies Used
- OpenAI's ChatGPT-3.5 API to generate responses.
- Langchain to keep a chat history of patient's previous chats. 
- Streamlit to create and deploying web application of the chatbot.

## Setup

- Create a new python3 virtual environment and activate it.

  ```
  python3 -m venv env
  source env/bin/activate
  ```

- Install necessary packages.

  ```
  pip install -r requirements.txt
  ```

- Add `OPENAI_API_KEY` as a secret environment variable in `.streamlit/secrets.toml` file:-

  ```
  OPENAI_API_KEY="<\YOUR-OPENAI-API-KEY\>"
  ```

- Run the Streamlit app locally using the following command:

  ```
  streamlit run main.py
  ```

## Deploy on Streamlit

Felix is easily deployable on the Streamlit platform.
Note that when setting up your StreamLit app you should make sure to add `OPENAI_API_KEY` as a secret environment variable.

## Follow-up tasks

- Clear input field for users once `Enter` is pressed.
- Extract and store patient's full name, date of birth, family doctor's name, preferred date and time for the appointment.
- Reply back with the available slots of appointment, doctors' availability, name and date of birth confirmation.
