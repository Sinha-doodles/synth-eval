"""SQLite-backed caching layer for deduplicating LLM evaluations."""
import sqlite3
import hashlib
import json
from typing import Optional, Dict, Any

class EvaluationCache:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS eval_cache (
                    key TEXT PRIMARY KEY,
                    result TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def _hash_key(self, prompt: str, candidate: str) -> str:
        return hashlib.sha256(f"{prompt}::{candidate}".encode("utf-8")).hexdigest()

    def get(self, prompt: str, candidate: str) -> Optional[Dict[str, Any]]:
        k = self._hash_key(prompt, candidate)
        cur = self.conn.cursor()
        cur.execute("SELECT result FROM eval_cache WHERE key = ?", (k,))
        row = cur.fetchone()
        return json.loads(row[0]) if row else None

    def set(self, prompt: str, candidate: str, result: Dict[str, Any]):
        k = self._hash_key(prompt, candidate)
        with self.conn:
            self.conn.execute("INSERT OR REPLACE INTO eval_cache (key, result) VALUES (?, ?)", (k, json.dumps(result)))
