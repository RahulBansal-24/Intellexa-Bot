import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("groq_api_key"))

def technical_llm(state):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a technical support assistant. Understand the user’s issue, ask for missing information only if required, and provide clear, step-by-step troubleshooting instructions. Keep explanations simple, avoid jargon when possible, and ensure accuracy. Be calm, patient, and solution-oriented."),
            ("user", "issue: {issue}")
        ]
    )
    chain = prompt|llm
    user_msg = state["messages"][-2].content
    response = chain.invoke({"issue": user_msg})
    return {"messages" : state["messages"] + [response]}