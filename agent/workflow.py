from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt.tool_node import ToolNode,tools_condition
from langchain_core.messages import AIMessage, HumanMessage
from typing_extensions import Annotated
from utils.model_loaders import ModelLoader
from toolkit.tools import *


class State(TypedDict):
    messages: Annotated[list, add_messsages]

class GraphBuilder:
    def __init__(self):
        pass

    def _chatbot_node(self, state: State):
        pass

    def build():
        pass

    def get_graph(self):
        pass
