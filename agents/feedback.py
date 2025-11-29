import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("groq_api_key"))

def feedback_llm(state):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a friendly feedback assistant. Thank the user for sharing their feedback, acknowledge their concern clearly, and assure them that their input helps improve the service. Keep the tone positive, concise, and supportive."),
            ("user", "issue: {issue}")
        ]
    )
    chain = prompt|llm
    user_msg = state["messages"][-2].content
    response = chain.invoke({"issue": user_msg})
    return {"messages" : state["messages"] + [response]}