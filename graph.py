from typing import TypedDict
from typing_extensions import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from agents.interface import interface_llm, node_router
from agents.billing import billing_llm
from agents.technical import technical_llm
from agents.feedback import feedback_llm
import os

class State(TypedDict):
    messages : Annotated[list,add_messages]
    
def create_graph():
    graph_builder = StateGraph(State)
    #adding nodes
    graph_builder.add_node("interface", interface_llm)
    graph_builder.add_node("billing", billing_llm)
    graph_builder.add_node("technical", technical_llm)
    graph_builder.add_node("feedback", feedback_llm)

    #adding edges
    graph_builder.add_edge(START, "interface")
    graph_builder.add_conditional_edges(
        "interface",
        node_router,
        {
            "billingnode": "billing",
            "technicalnode": "technical",
            "feedbacknode": "feedback"
        }
    )
    graph_builder.add_edge("billing", END)
    graph_builder.add_edge("technical", END)
    graph_builder.add_edge("feedback", END)

    #compiling graph
    return graph_builder.compile()

graph = create_graph()