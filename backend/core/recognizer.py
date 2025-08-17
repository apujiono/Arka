import hashlib

class UserRecognizer:
    def __init__(self):
        self.profiles = {}

    def extract_features(self, text):
        return {
            "length": len(text),
            "questions": text.count("?"),
            "excitement": text.count("!") + text.count("..."),
            "emotion": "positive" if any(w in text.lower() for w in ["senang", "hebat", "cinta"]) else "neutral"
        }

    def identify_user(self, text):
        features = self.extract_features(text)
        fingerprint = hashlib.md5(str(features).encode()).hexdigest()[:10]

        for uid, profile in self.profiles.items():
            if profile["fingerprint"] == fingerprint:
                return uid, profile["name"]

        new_id = len(self.profiles) + 1
        name = f"User {new_id}"
        self.profiles[new_id] = {
            "name": name,
            "fingerprint": fingerprint,
            "features": features
        }
        return new_id, name
