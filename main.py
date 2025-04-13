import os
import json
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("AI STICKY NOTES")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file_exists():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

def get_notes():
    ensure_file_exists()
    with open(NOTES_FILE, "r") as f:
        return f.read()
    
@mcp.tool()
def add_note(note: str) -> str:
    """Adds a note to the sticky notes collection
    
    Args:
        note (str): The text content to store as a note
        
    Returns:
        str: Confirmation message
    """
    ensure_file_exists()
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    return "Note added successfully"

@mcp.tool()
def read_notes() -> str:
    """Reads all notes from the sticky notes collection
    
    Returns:
        str: All notes in the collection
    """
    notes = get_notes()
    if not notes:
        return "No notes found"
    return notes

if __name__ == "__main__":
    mcp.run(port=8000)
    print(f"Server is running on port {mcp.port}")