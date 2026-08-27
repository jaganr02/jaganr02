# LangChain Researcher Agent

A beginner-friendly console-based AI Agent built using **Python, LangChain, and Groq LLM**.

This project is created mainly for learning and understanding how **LangChain Agents, LLMs, Tools, and console-based interaction** work together.

---

## 📌 Project Overview

The LangChain Researcher Agent is a simple console application where the user can enter a question or topic.

The application sends the user's input to a Groq-powered Large Language Model through LangChain and generates a response.

The main purpose of this project is to understand the fundamentals of building an AI Agent using LangChain.

---

## 🎯 Purpose of the Project

This project is created for:

- Learning LangChain
- Understanding LLM integration
- Understanding LangChain Agents
- Understanding how tools are connected to agents
- Learning how user input is handled in a console application
- Understanding the flow between User → Agent → LLM → Response
- Practicing Python project structure
- Learning how to manage API keys securely
- Understanding how AI applications are built step by step

---

## 🛠️ Technologies Used

- Python
- LangChain
- LangChain Groq
- Groq API
- Python-dotenv
- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```text
LangchainAgent/
│
├── venv/
│   └── Python virtual environment
│
├── .env
│   └── Stores the Groq API key
│
├── .gitignore
│   └── Files and folders excluded from Git
│
├── main.py
│   └── Console application entry point
│
├── agent.py
│   └── Creates and configures the LangChain Agent
│
├── tools.py
│   └── Contains tools available to the Agent
│
├── requirements.txt
│   └── Required Python packages
│
└── README.md
    └── Project documentation
