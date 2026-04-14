import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _compute_score(self, user: UserProfile, song: Song) -> float:
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 3.0
        if song.mood == user.favorite_mood:
            score += 2.0
        energy_diff = abs(song.energy - user.target_energy)
        score += (1.0 - energy_diff) * 2.0
        if user.likes_acoustic:
            score += song.acousticness * 1.5
        else:
            score += (1.0 - song.acousticness) * 0.5
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = sorted(self.songs, key=lambda s: self._compute_score(user, s), reverse=True)
        return scored[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"genre matches your preference for {song.genre}")
        if song.mood == user.favorite_mood:
            reasons.append(f"mood is {song.mood} which fits what you enjoy")
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.25:
            reasons.append("energy level is close to what you prefer")
        if user.likes_acoustic and song.acousticness > 0.6:
            reasons.append("acoustic feel matches your taste")
        if not reasons:
            return "this song has some features that align with your profile"
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    import pandas as pd
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []
    if song.get("genre") == user_prefs.get("genre"):
        score += 3.0
        reasons.append(f"genre matches {song['genre']}")
    if song.get("mood") == user_prefs.get("mood"):
        score += 2.0
        reasons.append(f"mood matches {song['mood']}")
    energy_diff = abs(float(song.get("energy", 0.5)) - float(user_prefs.get("energy", 0.5)))
    score += (1.0 - energy_diff) * 2.0
    if energy_diff < 0.2:
        reasons.append("energy level is close")
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "general match"
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
