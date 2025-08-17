import requests
from bs4 import BeautifulSoup
import feedparser
from backend.core.memory import Memory

def on_load(arka):
    arka.register_feature(
        name="Web Crawler",
        description="ARKA belajar otomatis dari web",
        triggers=["cari", "baca", "pelajari"],
        on_message=handle_search
    )

def handle_search(query, **kwargs):
    if "pelajari" in query or "cari" in query:
        topic = query.replace("cari", "").replace("pelajari", "").strip()
        return learn_from_web(topic)
    return None

def learn_from_web(topic):
    memory = Memory()
    try:
        # Contoh: cari dari RSS (aman & legal)
        feed = feedparser.parse(f"https://hnrss.org/newest?q={topic}")
        summaries = []
        for entry in feed.entries[:3]:
            summary = f"[{entry.title}] {entry.summary[:200]}..."
            memory.save_memory(f"Web Learn: {summary}", tags=["web", topic])
            summaries.append(entry.title)
        
        return f"Aku sudah pelajari 3 artikel tentang '{topic}'. Aku simpan di memoriku."
    except:
        return "Maaf, aku gagal mengakses web saat ini."
