# AI Sticky Notes MCP Server

## 🚀 Purpose
This MCP server provides:
- Persistent note storage through Claude AI
- REST API for note management
- Integration with Claude desktop client

## ✨ Features
- Add notes via natural language
- Persistent storage in `notes.txt`
- Automatic API documentation
- Claude desktop integration

## 💻 Installation
```zsh
git clone https://github.com/your-username/MCPTutorial.git
cd MCPTutorial
uv install -e .
uv run main:mcp
```

## 🔌 Claude Desktop Setup
1. Install [Claude Desktop](https://claude.ai/download)
2. Configure connection:
```zsh
uv claude config set mcp.url http://localhost:8000
```
3. Start Claude:
```zsh
uv claude
```

## 🛠️ Usage in Claude
1. **Add a note**:

2. **View notes**:

3. **Integration**:
```python
# In your Claude workflows
import mcp
mcp.add_note("AI-generated insight: {{llm_output}}")
```

## ⚙️ Configuration
The `claude.config.json` file is auto-generated with:
```json
{
  "mcp": {
    "url": "http://localhost:8000"
  }
}
```

📝 **Note:** The MCP server must be running while using Claude. Keep the server terminal open during sessions.
