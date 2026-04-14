# Model Card: Music Recommender Simulation

## 1. Model Name

GrooveMatch 1.0

---

## 2. Intended Use

This recommender is designed to suggest songs from a small catalog that closely match a users favorite genre, mood and energy level. It assumes the user has one clear genre and mood preference. This is built for classroom exploration only, not for real users.

---

## 3. How the Model Works

The system looks at each song in the catalog and compares it to what the user told us they like. A genre match scores the highest, a mood match scores second, and then how close the energy level is adds a bit more to the total. If the user likes acoustic music, songs with higher acousticness get a small extra boost. The song with the highest total points gets recommended first, and the next four follow in order.

---

## 4. Data

The catalog has 10 songs. Genres covered include pop, lofi, rock, ambient, jazz, synthwave and indie pop. Moods in the dataset include happy, chill, intense, relaxed, focused and moody. I didnt add or remove any songs from the starter data. The catalog leans toward chill and lo fi sounds and probably reflects the taste of someone who listens to study or focus playlists a lot. Jazz, rock and ambient each only have one song, so those genres are underrepresented.

---

## 5. Strengths

The system works well for users who prefer pop or lofi since those genres have more songs in the catalog. It also performs well when the user has a very clear energy preference, like someone who wants very high energy or very low energy music. The scoring is simple enough that its easy to understand exactly why a song got reccomended, which is a real advantage over black box systems.

---

## 6. Limitations and Bias

The catalog is tiny so any genre with just one song will almost always surface that song regardless of whether the mood or energy actually matches. The model treats every user as having exactly one preferred genre and one mood, so it cant handle users who like a mix of styles. Genre matching dominates the score, meaning a ambient user who wants high energy will still mostly get ambient songs even if none of them are high energy. This could be unfair to users with niche or cross genre tastes since their profiles just dont map well to what the catalog offers.

---

## 7. Evaluation

I tested three different user profiles. A pop and happy high energy user, a lofi and chill low energy user, and a jazz and relaxed user. The pop and lofi profiles gave results that felt right, Sunrise City and Midnight Coding came out at the top where I expected. The jazz profile only had one matching song in the whole catalog, so the rest of the recommendations were basically genre mismatches filling in the gaps. I also ran the full test suite and confirmed that the pop track always ranked above the lofi track for a pop and happy user.

---

## 8. Future Work

I would add more songs to the catalog to cover genres more evenly. I would also look at adding a diversity step so the top five dont all end up being the same genre when there are options. Supporting multiple preferred genres per user would make the profiles more realistic. And factoring in tempo more directly would be useful, since some users really care about bpm when picking music for a specific activity.

---

## 9. Personal Reflection

I was surprised by how much the genre weight alone controlled the output. Even when the mood and energy were totally off, a genre match would push a song near the top. That made me think about how real apps must work a lot harder to balance all those signals and still surface something that feels right. It also changed the way I think about personalization, it sounds like it should be smart and intuitive but really at its core its just math on a few numbers. Human judgment still matters a lot when deciding which features to use in the first place, because those choices end up shaping every single recommendation the system ever makes.
