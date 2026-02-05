from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int, b:int) -> int:
    """Add two numbers"""
    return a+b

@mcp.tool
def random_number(min_val: int=1, max_val: int=100) -> int:
    """Generate a random number within a range"""
    return random.randint(min_val, max_val)



if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)