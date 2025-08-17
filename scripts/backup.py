import os
import subprocess
from datetime import datetime

def backup_to_github():
    try:
        # Tambah semua perubahan
        subprocess.run(["git", "add", "data/"], check=True)
        
        # Commit
        commit_msg = f"Auto-backup: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        
        # Push
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("✅ Backup berhasil")
    except subprocess.CalledProcessError:
        print("⚠️ Tidak ada perubahan atau gagal push")

if __name__ == "__main__":
    backup_to_github()
