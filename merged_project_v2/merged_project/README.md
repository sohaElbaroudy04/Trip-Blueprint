#  TripBlueprint

TripBlueprint is a Flask web application that lets travelers share and learn from real trip experiences. Browse detailed itineraries from people who've already been where you want to go, use their plans as a blueprint, and adapt them to fit your own trip. Add places, track budgets, and contribute your own experiences back to the community.
---

##  Getting Started

### Run Normally (without Docker)

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python run.py
```

Open: http://localhost:5000

---

### 🐳 Run with Docker

**Option 1 — Docker Compose (easiest)**

```bash
docker-compose up
```

Open: http://localhost:5000

To stop:
```bash
docker-compose down
```

**Option 2 — Docker manually**

```bash
# Build the image
docker build -t tripblueprint .

# Run the container
docker run -p 5000:5000 tripblueprint
```

---

## 🔌 Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Home page |
| GET/POST | `/register` | Register |
| GET/POST | `/login` | Login |
| GET | `/logout` | Logout |
| GET | `/trips` | My trips |
| GET/POST | `/trips/new` | Create trip |
| GET | `/trips/<id>` | Trip detail |
| POST | `/trips/<id>/delete` | Delete trip |
| POST | `/trips/<id>/places` | Add place |
| POST | `/places/<id>/delete` | Delete place |
| GET | `/search` | Search trips |
| GET | `/filter` | Filter by budget |
| GET | `/community` | Community wishlists |
| GET/POST | `/community/new` | Share wishlist |
| GET | `/community/<id>` | Wishlist detail |

---

## 🗄️ Database Tables

| Table | Fields |
|-------|--------|
| `user` | id, username, email, password_hash |
| `trip` | id, user_id, name, destination, budget, is_public |
| `place` | id, trip_id, name, category, est_cost |
| `wishlist` | id, user_id, title, destination, description |

---

## 👥 Team

| Name | GitHub | 
|------|--------|
| Ann Akram | @AnnAkram *(update username)* | 
| Maya Ahmed | [@MayaKandil](https://github.com/MayaKandil) | 
| Jasmine Mahmoud | [@JasmineM9](https://github.com/JasmineM9) | 
| Soha Elbaroudy | [@sohaElbaroudy04](https://github.com/sohaElbaroudy04) |
