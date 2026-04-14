# Music Recommender Simulation

## Project Summary

This system loads a small catalog of songs from a csv file and scores each one based on how well it matches a users genre, mood and energy preferences. The top five scoring songs get returned as reccomendations. I built it using a simple point system where genre and mood matches give the biggest boost and energy closeness adds a little extra to the total score.

---

## How The System Works

Each song has the following features, genre, mood, energy, tempo bpm, valence, danceability and acousticness, where genre and mood are the main ones used in scoring and energy plays a secondary role. The user profile stores a favorite genre, a favorite mood, a target energy level between 0 and 1, and a boolean for whether the user likes acoustic music. The recommender scores each song by adding 3 points for a genre match, 2 points for a mood match, up to 2 points based on how close the energy is, and a small acousticness bonus depending on user preference, then sorts all songs from highest to lowest and returns the top k, defaulting to 5.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

When I lowered the genre weight from 3.0 to 1.0, mood and energy started driving the results more and sometimes surfaced lofi songs for a pop user which felt a bit off. Adding the acousticness bonus made a noticeable diffrence for chill user profiles, Library Rain and Spacewalk Thoughts started showing up much more consistently for users who prefer acoustic music. Testing with a high energy intense user profile gave very clear results, Gym Hero and Storm Runner always came out at the top which felt about right and the system seemed to reward energy alignment well when genre was not a factor.

---

## Limitations and Risks

The catalog only has 10 songs so the results are pretty limited no matter what profile you use, and it doesnt look at lyrics or language at all so a sad song with high energy would still get recommended to a happy user if the genre matched. The genre weight is also high enough that it can dominate the score, meaning a user with an unusual combo like ambient and high energy might still get ambient songs even if none of them match the energy at all.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this made me realize how much a single feature like genre can control the output of a recommender, just changing the genre weight shifted the whole ranking pretty drastically which surprised me, and I started thinking more about how real apps like Spotify probably balance way more signals to avoid the kind of overfitting I saw. The bias part was interesting too, my dataset doesnt have much genre variety so users who prefer jazz or ambient only get one or two real matches in the whole catalog, and in a real product that kind of imbalance could mean whole groups of listeners feel like the app doesnt understand their taste at all, which is a genuine fairness problem.
