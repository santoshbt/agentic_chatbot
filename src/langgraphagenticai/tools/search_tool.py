from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tavily_search = TavilySearch(max_results=2)
    tools = [tavily_search]
    return tools

def create_tool_node(tools):
    """
    Creates and returns the tool node for the graph
    """
    return ToolNode(tools=tools)