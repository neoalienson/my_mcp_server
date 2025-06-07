import argparse
from fastmcp import FastMCP
import tools

def create_mcp_server():
    """Create and configure the MCP server with prompts"""
    mcp = FastMCP(name="PromptServer")

    # Basic prompt returning a string (converted to user message automatically)
    @mcp.prompt
    def ask_about_topic(topic: str) -> str:
        """Generates a user message asking for an explanation of a topic."""
        return f"Can you please explain the concept of '{topic}'?"
    
    @mcp.tool
    def greet(name: str) -> str:
        return tools.greet(name)

    @mcp.tool(
        description="Roll n_dice 6-sided dice and return results",
    )
    def roll_dice(n_dice: int) -> list[int]:
        return tools.roll_dice()
    
    @mcp.tool(
        description="Generate lottery numbers for Mark Six in Hong Kong. Generate 6 unique random numbers between 1 and 49",
    )
    def generate_lottery_numbers() -> list[int]:
        return tools.generate_lottery_numbers()
    
    return mcp

def main():
    parser = argparse.ArgumentParser(description='MCP Prompt Server')
    parser.add_argument('-s', '--sse', action='store_true', 
                       help='Run in SSE mode instead of stdio')
    args = parser.parse_args()

    server = create_mcp_server()
    
    if args.sse:
        # Run in SSE mode on port 8000
        server.run(transport="streamable-http")
        print("MCP Prompt Server running in SSE mode on port 8000")
    else:
        # Default to stdio mode
        server.run()
        print("MCP Prompt Server running in stdio mode")

if __name__ == "__main__":
    main()
