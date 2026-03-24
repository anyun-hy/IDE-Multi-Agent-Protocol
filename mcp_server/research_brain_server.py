#!/opt/anaconda3/bin/python
"""
research_brain_server.py
Antigravity 全局 MCP 插件 —— 持久化记忆与上下文接力

位置：~/.agent/mcp/（全局，不绑定任何项目）
依赖：mcp（已装）, sqlite3（Python 内置）
外部 API：无
"""

import json
import sqlite3
import os
from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# ── 全局数据目录 ──
DATA_DIR = Path(os.path.expanduser("~/.agent/mcp/data"))
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "brain.db"

mcp = FastMCP("research-brain")


def get_db():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                type TEXT DEFAULT 'general',
                project TEXT DEFAULT '',
                timestamp TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_snapshots (
                role_name TEXT PRIMARY KEY,
                current_task TEXT NOT NULL,
                context_summary TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                name TEXT PRIMARY KEY,
                phase TEXT NOT NULL,
                next_todo TEXT DEFAULT '',
                notes TEXT DEFAULT '',
                updated_at TEXT NOT NULL
            )
        """)
    conn.close()


init_db()


# =====================================================================
# 上下文接力棒
# =====================================================================

@mcp.tool()
def save_context(role_name: str, current_task: str,
                 context_summary: str) -> str:
    """对话过长需要关闭重开时，保存当前角色的快照。"""
    conn = get_db()
    now = datetime.now().isoformat()
    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO agent_snapshots "
            "(role_name, current_task, context_summary, updated_at) "
            "VALUES (?, ?, ?, ?)",
            (role_name, current_task, context_summary, now)
        )
    conn.close()
    return f"✅ [{role_name}] 快照已保存。可以安全关闭当前会话。"


@mcp.tool()
def load_context(role_name: str) -> str:
    """新开对话时，读取指定角色的快照，恢复上下文。"""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM agent_snapshots WHERE role_name = ?",
        (role_name,)
    ).fetchone()
    conn.close()
    if not row:
        return f"⚠️ 未找到 [{role_name}] 的存档。"
    return (
        f"✅ 已恢复 [{role_name}] 存档\n"
        f"· 存档时间: {row['updated_at']}\n"
        f"· 未完任务: {row['current_task']}\n"
        f"· 上下文摘要:\n{row['context_summary']}"
    )


# =====================================================================
# 全局记忆（跨角色、跨项目共享）
# =====================================================================

@mcp.tool()
def record_decision(decision: str, reason: str,
                    project: str = "") -> str:
    """记录关键决策。任何会话都能检索到。"""
    conn = get_db()
    now = datetime.now().isoformat()
    with conn:
        conn.execute(
            "INSERT INTO memories (content, type, project, timestamp) "
            "VALUES (?, 'decision', ?, ?)",
            (f"{decision} | 原因: {reason}", project, now)
        )
    conn.close()
    return f"✅ 决策已记录: {decision}"


@mcp.tool()
def recall_memories(keyword: str = "", limit: int = 10) -> str:
    """检索历史记忆。可按关键词过滤。"""
    conn = get_db()
    if keyword:
        rows = conn.execute(
            "SELECT content, type, project, timestamp FROM memories "
            "WHERE content LIKE ? ORDER BY id DESC LIMIT ?",
            (f"%{keyword}%", limit)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT content, type, project, timestamp FROM memories "
            "ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
    conn.close()
    if not rows:
        return "🧠 未找到相关记忆。"
    lines = [f"🧠 找到 {len(rows)} 条记忆:"]
    for r in rows:
        proj = f" [{r['project']}]" if r['project'] else ""
        lines.append(
            f"- [{r['type']}]{proj} {r['content']} ({r['timestamp'][:10]})"
        )
    return "\n".join(lines)


# =====================================================================
# 项目状态
# =====================================================================

@mcp.tool()
def get_project_status(project: str) -> str:
    """获取项目当前状态。"""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM projects WHERE name = ?", (project,)
    ).fetchone()
    conn.close()
    if not row:
        return f"⚠️ 项目 '{project}' 暂无记录。"
    return json.dumps(dict(row), ensure_ascii=False, indent=2)


@mcp.tool()
def update_project_status(project: str, phase: str,
                          next_todo: str = "",
                          notes: str = "") -> str:
    """更新项目进度。"""
    conn = get_db()
    now = datetime.now().isoformat()
    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO projects "
            "(name, phase, next_todo, notes, updated_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (project, phase, next_todo, notes, now)
        )
    conn.close()
    return f"✅ 项目 '{project}' 状态已更新: {phase}"


# ── 启动 ──
if __name__ == "__main__":
    mcp.run(transport="stdio")
