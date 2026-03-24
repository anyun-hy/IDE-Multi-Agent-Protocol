#!/bin/bash
# Install script for IDE-Multi-Agent-Protocol
# This script sets up the local environment required for the IDE agent handoff protocol.

echo "============================================"
echo "🚀 IDE-Multi-Agent-Protocol 一键安装脚本 🚀"
echo "============================================"
echo ""

# 1. 创建核心依赖目录
echo "[+] 正在创建底层结构 (~/.agent/ 和 ~/.gemini/)"
mkdir -p ~/.agent/mcp/data
mkdir -p ~/.agent/skills/{academic,java-engineer,office,research}
mkdir -p ~/.gemini/antigravity/global_workflows

# 2. 拷贝关键文件
echo "[+] 正在分发模块资产..."
cp -n ./mcp_server/research_brain_server.py ~/.agent/mcp/
cp -n ./global_workflows/*.md ~/.gemini/antigravity/global_workflows/
cp -n ./skills_template/academic/SKILL.md ~/.agent/skills/academic/
cp -n ./skills_template/java-engineer/SKILL.md ~/.agent/skills/java-engineer/
cp -n ./skills_template/office/SKILL.md ~/.agent/skills/office/
cp -n ./skills_template/research/SKILL.md ~/.agent/skills/research/

# 3. 环境配置 - MCP
echo "[+] 配置持久层 MCP Server (SQLite)..."
if ! python3 -c "import mcp" > /dev/null 2>&1; then
    echo "    -> 安装 mcp 协议包..."
    pip3 install "mcp[cli]" --break-system-packages
fi

# 4. 生成 MCP Config (Antigravity 用)
echo "[+] 正在注册 MCP Config..."
PYTHON_PATH=$(which python3)
cat <<EOF > ~/.gemini/antigravity/mcp_config.json
{
  "mcpServers": {
    "research-brain": {
      "command": "$PYTHON_PATH",
      "args": [
        "$(eval echo ~/.agent/mcp/research_brain_server.py)"
      ]
    }
  }
}
EOF

echo ""
echo "============================================"
echo "🎉 安装完成！"
echo "👉 请打开 Antigravity，将本项目中的 Global_Rule_Template.md 的内容粘贴进 Global Rule 设置。"
echo "👉 彻底重启 Antigravity IDE 以加载全局配置。"
echo "============================================"
