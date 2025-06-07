# Personal MCP Server

This is a personal implementation of a Model Context Protocol (MCP) server that provides custom tools through a FastMCP interface.

## Features
- Greeting tool: Returns personalized greetings
- Dice rolling: Simulates rolling multiple 6-sided dice
- Lottery number generator: Creates Mark Six lottery numbers (6 unique numbers between 1-49)

## Setup
1. Clone this repository
2. Install Python dependencies (FastMCP)
3. Run the server: `python my_mcp_server.py`

### Running Options
- Default stdio mode: `python my_mcp_server.py`
- SSE mode (port 8000): `python my_mcp_server.py --sse`

## Testing
Tests are available in `test_tools.py`. Run with:
```bash
python -m unittest test_tools.py
