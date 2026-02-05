# MCP Demo Server

A simple Model Context Protocol (MCP) server built with FastMCP for testing and demonstration purposes.

## Overview

This project demonstrates how to create, test, and deploy an MCP server using FastMCP. The server provides basic calculator and random number generation tools that can be accessed via the MCP protocol.

## Features

The server exposes two tools:

- **add**: Adds two numbers together
- **random_number**: Generates a random number within a specified range (default: 1-100)

## Live Demo

The server is deployed and accessible at:
```
https://MCP-Demo-Server.fastmcp.app/mcp
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yashver025/MCP-Demo-Server.git
cd MCP-Demo-Server
```

2. Install dependencies:
```bash
pip install fastmcp
```

## Usage

### Running Locally

Run the server locally:
```bash
python main.py
```

The server will start on `http://0.0.0.0:8000`

### Testing with MCP Inspector

1. Install and open [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
2. Configure the connection:
   - **Transport Type**: Streamable HTTP
   - **URL**: `http://localhost:8000/sse`
   - **Connection Type**: Via Proxy
3. Click "Connect" to start inspecting the server

## Code Structure

```python
from fastmcp import FastMCP

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int, b:int) -> int:
    """Add two numbers"""
    return a+b

@mcp.tool
def random_number(min_val: int=1, max_val: int=100) -> int:
    """Generate a random number within a range"""
    return random.randint(min_val, max_val)
```

## Deployment

This server is deployed using FastMCP's deployment platform. To deploy your own:

1. Sign up at [fastmcp.app](https://fastmcp.app)
2. Follow the deployment instructions
3. Your server will be accessible via HTTPS

## Technologies Used

- [FastMCP](https://github.com/jlowin/fastmcp) - Framework for building MCP servers
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Protocol for AI model context sharing

---

**Note**: This is a demo project created for learning and testing MCP server development.
