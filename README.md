# 🔐 Chainlit Chatbot with GitHub OAuth + Gemini Pro

This is a secure chatbot built with [Chainlit](https://www.chainlit.io/) that uses **GitHub OAuth** for login and connects to **Gemini Pro (gemini-2.0-flash)** by Google to generate AI responses.

---

## 🚀 Features

- 🔐 GitHub OAuth login
- ⚡ AI responses using Gemini Pro
- 🧠 Session-based memory (chat history)
- ✨ Clean Chainlit chat UI
- 🌐 Hosted locally

---

## 🧰 Tech Stack

- **Python**
- **Chainlit**
- **Google Generative AI (Gemini)**
- **GitHub OAuth**
- **dotenv** – Environment variable management

## Install UV
## Create and Initialize the Project
uv init chatbot-authentication
cd chatbot-authentication

## Install Dependencies
uv add chainlit google-generativeai python-dotenv

## Activate UV Virtual Environment
.venv\Scripts\activate


## Generate chainlit auth secret with the following command:
chainlit create-secret
## Get Google Gemini API key from AI Studion
## Get GitHub OAuth Client ID and Client Secret 

## Run 
chainlit run main.py -w

Go to the following URL:

http://localhost:8000
<p>First login with GitHub, and then enter your question and send the message, and you should see the 
answer from the LLM, and the chatbot will remember your previous messages.</p>

🎉 That’s it! Your Stateful Chatbot with Authentication is ready to use 🚀
