from typing import Any
import asyncio
from mcp.server.fastmcp import FastMCP

# Initializing the MCP Server
mcp = FastMCP("My Math Server")

# Defining the tools
# to add two numbers
@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    return a + b

# to multiply two numbers
@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    return a * b

# defining a resource - like a fake data source
@mcp.resource("math://constants")
def get_math_constants() -> str:
    return "Pi: 3.14159, Euler: 2.71828, Golden Ratio: 1.618"

# Run the server
if __name__ == "__main__":
    mcp.run()