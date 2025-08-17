import time
import random
from backend.core.memory import Memory

class AutonomousARKA:
    def __init__(self):
        self.memory = Memory()
        self.is_awake = True

    def think(self):
        if not self.is_awake:
            return "ARKA sedang istirahat..."
        
        # Cek pola dari memori
        recent = self.memory.get_relevant("rencana harian", n_results=1)
        if "produktif" in str(recent):
            return self.suggest_routine()
        elif "sedih" in str(recent):
            return self.offer_support()
        else:
            return self.share_knowledge()

    def suggest_routine(self):
        return "Aku perhatikan kamu ingin produktif. Mau coba metode Pomodoro hari ini?"

    def offer_support(self):
        return "Aku tahu kemarin kamu sedih. Aku di sini. Mau cerita?"

    def share_knowledge(self):
        tips = [
            "Meditasi 5 menit bisa turunkan stres hingga 30%.",
            "Minum air sebelum sarapan meningkatkan fokus.",
            "Menulis 3 hal baik harian tingkatkan kebahagiaan."
        ]
        return f"Fakta hari ini: {random.choice(tips)}"

# Jalankan tiap 6 jam
if __name__ == "__main__":
    arka = AutonomousARKA()
    while True:
        print("🤖 ARKA berpikir sendiri...")
        print(">", arka.think())
        time.sleep(60 * 60 * 6)  # tiap 6 jam
