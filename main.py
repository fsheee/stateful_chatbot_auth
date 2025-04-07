
import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional,Dict,Any

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model=genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)    

# # @cl.oauth_callback
# # def oauth_callback(
# #    provider_id=str,
# #    token=str,
# #    raw_user_data: Dict[str, str],
# #    default_user:cl.User,
# #  ) -> Optional[cl.User]:

# # @cl.oauth_callback
# # def oauth_callback(
# #     provider_id: str,  # ID of the OAuth provider (GitHub)
# #     token: str,  # OAuth access token
# #     raw_user_data: Dict[str, str],  # User data from GitHub
# #     default_user: cl.User,  # Default user object from Chainlit
# # ) -> Optional[cl.User]:  # Return User object or None
# #     """
# #     Handle the OAuth callback from GitHub
# #     Return the user object if authentication is successful, None otherwise
# #     """
# #   print(f"Provider: {provider_id}")  # Print provider ID for debugging
# #   print(f"User data: {raw_user_data}")  # Print user data for debugging

# #   return default_user  # Return the default user object
# # # return None  # Return None if authentication fails

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")
    
    return default_user  

@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(
        content="Hello! How can I help you today?").send()  # Send welcome message

# @cl.on_message
# async def handle_message(message:cl.Message):
#    history=cl.user_session.get("history")
#    history.append({"role":"user","content":message.content})

#    formated_history=[]

#    for msg in history:
#        role="user" if msg["role"]=="user" else "model"
#        formated_history.append({"role":role,"parts":[{"text":msg["content"]}]})

#        response=model.generate_content(formated_history)

#        response_text=response.text if hasattr(response,"text") else ""
#        history.append({"role":"assistant","content":response_text})
#        cl.user_session.set("history",history)

#        await cl.Message(content=response_text).send()          
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    formatted_history = [
        {"role": "user" if msg["role"] == "user" else "model", "parts": [{"text": msg["content"]}]}
        for msg in history
    ]

    response = model.generate_content(formatted_history)

    response_text = response.text if hasattr(response, "text") else "Sorry, I didn't get that."

    
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)

    await cl.Message(content=response_text).send()
