import chromadb
from datetime import datetime
import sqlite3

class Memory:
    def __init__(self, db_path="data/memory.db"):
        # Vector DB (untuk pencarian konteks)
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection("arka_memory")

        # Structured DB (untuk metadata)
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                text TEXT,
                timestamp TEXT,
                importance REAL,
                tags TEXT
            )
        """)
        self.conn.commit()

    def save_memory(self, text, importance=0.5, tags=None):
        memory_id = f"mem_{datetime.now().timestamp()}"
        timestamp = datetime.now().isoformat()

        # Simpan ke Chroma (untuk pencarian vektor)
        self.collection.add(
            documents=[text],
            metadatas=[{"timestamp": timestamp, "importance": importance}],
            ids=[memory_id]
        )

        # Simpan ke SQLite (untuk struktur)
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO memories (id, text, timestamp, importance, tags)
            VALUES (?, ?, ?, ?, ?)
        """, (memory_id, text, timestamp, importance, ",".join(tags or [])))
        self.conn.commit()

        return memory_id

    def get_relevant(self, query, n_results=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []

    def cleanup_old(self, days=90):
        from datetime import timedelta
        cutoff = datetime.now() - timedelta(days=days)
        # Di sini bisa tambah logika hapus memory lama
