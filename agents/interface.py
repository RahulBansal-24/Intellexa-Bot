import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("groq_api_key"))

def interface_llm(state):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a customer care bot, tell me whether the given problem is based on Billing issue, Technical issue or Feedback."),
            ("user", "issue: {issue}")
        ]
    )
    chain = prompt|llm
    user_msg = state["messages"][-1].content
    response = chain.invoke({"issue": user_msg})
    return {"messages" : state["messages"] + [response]}

def node_router(state):
    classification = state['messages'][-1].content.lower().strip()
    
    if "billing" in classification:
        return "billingnode"
    elif "technical" in classification:
        return "technicalnode"
    elif "feedback" in classification:
        return "feedbacknode"
    else:
        return "feedbacknode"