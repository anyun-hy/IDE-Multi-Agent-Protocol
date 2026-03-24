# IDE Multi-Agent Protocol (IMAP)

**Zero-Dependency, Fully Local, Context-Persistent Multi-Agent Architecture for IDEs.**

Are you tired of your IDE AI Agent losing context during long coding sessions? Do you hate passing API keys to heavy frameworks like `CrewAI` or `Mem0` just to simulate multi-agent collaboration? 

**IMAP** (IDE Multi-Agent Protocol) is a lightweight, zero-API architecture designed explicitly for native IDE Agents (like Antigravity / Cursor / Copilot). It uses a "Token Handoff" mechanism back by a local MCP SQLite database to achieve immortal memory and robust persona switching.

---

## 🌟 Core Features

1. **Zero External APIs**: No OpenAI keys, no Anthropic keys. It purely leverages your IDE's built-in conversational models for reasoning, using Python's standard `sqlite3` and the open-source `mcp` protocol for state management.
2. **Context Continuity (Immortality)**: Solves the "context length limit" problem. When your chat gets too long, trigger `/handoff`. The agent summarizes its state, saves it to the SQLite brain, and gives you a `[Token]`. Paste the token into a fresh chat window, and it literally "wakes up" exactly where it left off, retaining 100% of its persona and project context.
3. **True Separation of Concerns**: Unbloats the "Global Prompt". We split the AI into three physical layers:
   - **Layer 3 (Router)**: Global Manager Rule analyzing intent.
   - **Layer 2 (Agents)**: Project-agnostic `SKILL` folders containing distinct personas (e.g., Writer, Engineer).
   - **Layer 1 (Memory)**: A persistent background MCP server tracking global decisions.

---

## 🏗️ Architecture

```mermaid
graph TD;
    User[👶 User] -- "/dispatch" --> Manager[🧠 Layer 3: Manager / Router (Global Rule)]
    Manager -- Generates --> Token[🎫 Hand-off Token]
    Token -. User pastes into new chat .-> NewChat[💬 New IDE Chat Window]
    NewChat -- "/switch" --> Persona[🎭 Layer 2: Expert Persona loaded from Skills/]
    Persona -- "load_context()" --> MCP[(💾 Layer 1: Persistent MCP Brain / SQLite)]
    MCP -- Recalls State --> Persona
    Persona -- "/handoff" --> MCP
```

---

## ⚡ Quick Start

### 1. Auto-Install (Mac/Linux)
Clone this repo and run the setup script to instantly configure your `~/.agent` and `~/.gemini` directories:

```bash
git clone https://github.com/yourusername/IDE-Multi-Agent-Protocol.git
cd IDE-Multi-Agent-Protocol
chmod +x install.sh
./install.sh
```

### 2. Manual Configuration
Append the contents of `Global_Rule_Template.md` into your IDE's system/global prompt interface.

### 3. Usage Loop
1. Open your IDE Chat. Say: _"I want to write an academic paper about deep learning."_
2. The Agent (acting as Manager) will evaluate, and tell you to run `/dispatch`.
3. It will generate a **Token** for the `Writer` persona.
4. **Physically close the chat window**, open a new one (refreshing token usage).
5. Paste the Token and run `/switch`. The Agent transforms into the `Writer`, loading all specialized tools and historical memory.

---

## 🛠 Directory Structure

- `mcp_server/`: The Python daemon bridging the IDE with local SQLite.
- `global_workflows/`: `/dispatch`, `/switch`, `/handoff`, `/status` logic.
- `skills_template/`: Pre-configured expert personas (Academic Writer, Research Coder, Java Engineer, Office Automator). Update these markdown files to inject your own expert knowledge!

## 📜 License
MIT License. Built by builders, for builders.
