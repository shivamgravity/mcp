# MCP Math Tools Server

This project demonstrates a Python implementation of the **Model Context Protocol (MCP)**. It builds a functional MCP Server that exposes mathematical capabilities (Tools) and static data (Resources) to MCP Clients, such as AI assistants or the MCP Inspector.

## Project Overview

The goal of this project is to create a standardized server that bridges the gap between an AI model and local computational logic.

**Key Features:**
* **Tools:** Exposes executable functions (`add_numbers`, `multiply_numbers`) that an AI can call to perform calculations.
* **Resources:** Exposes structured data (`math://constants`) that an AI can read as context.
* **Architecture:** Built using the official `mcp` Python SDK and tested using the generic MCP Inspector.

## Prerequisites

* **Python 3.10+**
* **Node.js & NPM** (Required only to run the MCP Inspector for testing)

## Setup & Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/shivamgravity/mcp
    cd mcp
    ```

2.  **Set Up Virtual Environment**
    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    # Create venv
    python -m venv venv

    # Activate venv (Windows)
    venv\Scripts\activate

    # Activate venv (Mac/Linux)
    source venv/bin/activate

    # To deactivate the virtual environment, run this command
    deactivate
    ```

3.  **Install Dependencies**
    Install the official Python SDK for MCP.
    ```bash
    pip install mcp
    ```

## How to Run (Testing with Inspector)

Since this is a protocol server, it needs a client to interact with. We use the official **MCP Inspector** web interface for testing.

1.  **Start the Server via Inspector:**
    Run the following command in your terminal (ensure your venv is active):
    ```bash
    npx @modelcontextprotocol/inspector python server.py
    ```

2.  **Access the UI:**
    Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:6274` or `http://localhost:5173`).

3.  **Connect & Test:**
    * Click **Connect**.
    * **Tools Tab:** Select `add_numbers`, enter arguments (e.g., `a=10, b=5`), and click "Run Tool" to see the result.
    * **Resources Tab:** Click on the `math://constants` resource to read the structured JSON data.

## Solution Architecture

This project follows the **Model Context Protocol** standard:

* **Server (`server.py`):**
    * Uses the `FastMCP` class to initialize the server instance.
    * **Tools:** Functions decorated with `@mcp.tool()` are exposed as executable logic. The server handles the JSON-RPC communication to receive arguments and return results.
    * **Resources:** Functions decorated with `@mcp.resource()` act as data endpoints. They return structured JSON data (MIME type `application/json`) representing math constants.

* **Communication:**
    * The server communicates over `stdio` (Standard Input/Output), allowing it to be easily piped into any MCP-compliant client (like Claude Desktop or the MCP Inspector).