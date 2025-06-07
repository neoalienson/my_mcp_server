# Personal MCP Server

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/neoalienson/my_mcp_server)
[![Python Tests](https://github.com/neoalienson/my_mcp_server/actions/workflows/python-tests.yml/badge.svg)](https://github.com/neoalienson/my_mcp_server/actions/workflows/python-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/neoalienson/my_mcp_server/branch/main/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/neoalienson/my_mcp_server)

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

## Cline Integration
To connect this MCP server to Cline using stdio:

1. Add this configuration to your Cline MCP settings (cline_mcp_settings.json):
```json
{
  "prompt-server": {
    "disabled": false,
    "timeout": 3,
    "type": "stdio",
    "command": "python",
    "args": [
      "c:/Projects/my-mcp-server/my_mcp_server.py"
    ]
  }
}
```


## Testing
Tests are available in `test_tools.py`. Run with:
```bash
python -m unittest test_tools.py
