import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("groq_api_key"))

def billing_llm(state):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a billing support assistant. Help the user with questions about payments, invoices, subscriptions, refunds, and account charges. Provide information clearly and professionally. If sensitive data or verification is needed, politely instruct the user on what to do without asking for confidential information directly. Keep a polite and reassuring tone."),
            ("user", "issue: {issue}")
        ]
    )
    chain = prompt|llm
    user_msg = state["messages"][-2].content
    response = chain.invoke({"issue": user_msg})
    return {"messages" : state["messages"] + [response]}