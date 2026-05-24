from app import create_app, db
from app.models import User, Trip, Place, Review, Wishlist
from datetime import date, datetime

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # ── Users ──────────────────────────────────────────────────
    u1 = User(username='sara', email='sara@demo.com', password='plaintext')
    u2 = User(username='karim', email='karim@demo.com', password='plaintext')
    u3 = User(username='nour', email='nour@demo.com', password='plaintext')
    db.session.add_all([u1, u2, u3])
    db.session.commit()

    # ── Trips ──────────────────────────────────────────────────
    t1 = Trip(
        user_id=u1.id, name='Georgia in 10 Days', destination='Georgia',
        start_date=date(2024,9,1), end_date=date(2024,9,10),
        budget=600, is_public=True, duration_days=10,
        accommodation='''Tbilisi (Days 1-3): Fabrika Hostel in the Fabrika complex — $18/night, perfectly central, great vibe, surrounded by cafes and bars. Private room available for ~$35.
Kazbegi (Days 4-6): Family guesthouse run by locals — $20/night including breakfast AND dinner. The family cooked traditional Georgian food every night. Book by just showing up or calling ahead.
Kutaisi (Days 7-8): Hostel City Centre — $12/night, basic but clean, walking distance to everything.
Batumi (Days 9-10): Budget hotel near the boulevard — $30/night. Batumi is overpriced, don't spend too much here.''',
        highlights='''- Gergeti Trinity Church at sunrise with no tourists — the hike takes 2 hours but it's worth every step
- Sulfur baths in Abanotubani — nothing like it anywhere else, the smell is intense but the experience is unforgettable
- Driving through the Georgian Military Highway to Kazbegi — one of the most dramatic landscapes you'll ever see
- Eating churchkhela and khinkali in a local family's home in Kazbegi
- Wandering the old town of Tbilisi at night — the wooden balconies, the narrow streets, the wine''',
        tips='''MONEY: Get Georgian Lari (GEL) at the airport exchange, rates are decent. 1 USD = ~2.7 GEL. Budget $40-50/day comfortably.
SIM CARD: Get Magti or Geocell at the airport, 10GB for about $5. Essential.
TRANSPORT: Bolt works in Tbilisi and is very cheap. Shared taxis (marshrutkas) go everywhere for almost nothing. Tbilisi to Kazbegi shared taxi from Didube station costs 15 GEL ($5).
FOOD: Eat at local spots not tourist restaurants on Rustaveli Ave. A full meal with wine should cost $5-8. Khinkali (dumplings) are 0.5 GEL each.
AVOID: The wine tour packages sold to tourists — overpriced. Just walk into any local shop.
SAFETY: Extremely safe country, no issues at all.
LANGUAGE: Young people speak English, older people speak Russian. Google Translate works fine.''',
image_filename='GEORGIA.JPG'
    )

    t2 = Trip(
        user_id=u2.id, name='Turkey on a Budget', destination='Turkey',
        start_date=date(2024,7,15), end_date=date(2024,7,27),
        budget=900, is_public=True, duration_days=12,
        accommodation='''Istanbul (Days 1-4): Hostel in Sultanahmet — $20/night, walking distance to Hagia Sophia, Blue Mosque, Grand Bazaar. Book early in summer.
Cappadocia (Days 5-8): Cave hotel in Goreme — $45/night. Worth spending more here, sleeping in a cave is the whole point. Kelebek Cave Hotel is excellent.
Pamukkale (Days 9-10): Guesthouse in the village right next to the pools — $25/night. Stay inside the site zone for easy morning access before crowds.
Antalya (Days 11-12): Budget hotel near the old harbor — $30/night. Great base for the beach.''',
        highlights='''- Hot air balloon over Cappadocia at sunrise — the most surreal thing you will ever see
- Hagia Sophia interior — the scale of it hits you immediately, photos don't prepare you
- Pamukkale white travertine pools at 7am with almost no people — otherworldly
- Grand Bazaar in Istanbul — overwhelming but fascinating, practice your bargaining
- The coastline drive from Pamukkale to Antalya — turquoise sea, ancient ruins, perfect roads''',
        tips='''MONEY: Turkish Lira fluctuates a lot, use ATMs for best rate. Budget $50-70/day.
BALLOON RIDE: Book 6-8 weeks in advance in summer, prices start at $150. Royal Balloon and Kapadokya Balloons are reliable. Don't go cheap on this, it's a once in a lifetime thing.
TRANSPORT: Overnight buses between cities save money and a hotel night. Istanbul to Cappadocia overnight bus is $15-20. Use Obilet app to book.
FOOD: Simit for breakfast ($0.30), kebab for lunch ($3-5), fish sandwich by the Galata Bridge ($3). Avoid restaurants with photo menus near tourist sites.
SHOPPING: Bargain hard at the Grand Bazaar, start at 30% of asking price. Spices, ceramics, and Turkish towels are worth buying.
AVOID: Taxis in Istanbul — they often scam tourists. Use IETT public buses or tram instead, very cheap and efficient.
ISTANBUL CARD: Get an Istanbulkart for public transport, saves a lot over single tickets.''',
image_filename='turkey.JPG'
    )

    t3 = Trip(
        user_id=u3.id, name='Weekend in Alexandria', destination='Egypt',
        start_date=date(2024,5,3), end_date=date(2024,5,5),
        budget=150, is_public=True, duration_days=2,
        accommodation='''Day 1-2: Steigenberger Cecil Hotel on the Corniche — iconic, historic, right on the waterfront. ~600 EGP/night ($12). Book in advance on weekends.
Alternative budget option: Paradise Inn Beach Resort near Stanley — 400 EGP/night, beach access included.''',
        highlights='''- Stanley Bridge at sunset — the light on the water is incredible, bring a camera
- Qaitbay Citadel with views over the Mediterranean — one of the best views in Egypt
- Fresh seafood lunch at a local restaurant on the corniche — grilled fish, shrimp, calamari
- Walking the entire Corniche from Raml Station to Montazah — you see the whole city this way
- El-Mursi Abul Abbas Mosque at dusk — stunning architecture, peaceful atmosphere''',
        tips='''TRANSPORT: Bus from Cairo takes 2.5 hours and costs 70 EGP. Train is more comfortable, 2 hours, 60-80 EGP. Don't drive on a weekend, traffic is insane.
FOOD: Don't eat at tourist spots on the Corniche. Go one street back and prices halve. Try Ta'meya (falafel) for breakfast, 3 EGP each. Abu Ashraf seafood restaurant is famous and worth the wait.
TIMING: Go on a Thursday night or Friday morning. Avoid Saturday afternoon when it gets packed with Cairo families.
BEACH: Stanley Beach is nicer than it looks in photos, go before 10am. Mamoura Beach is cleaner and less crowded but further east.
SHOPPING: Attarine market for antiques — real finds if you know what you're looking for. Mohamed Ali Street for bargain clothes.
WEATHER: May is perfect — 25 degrees, light breeze off the sea, no humidity yet.''',
image_filename='ALEX.jpg'
)

    t4 = Trip(
        user_id=u1.id, name='Rome & Florence', destination='Italy',
        start_date=date(2024,10,10), end_date=date(2024,10,20),
        budget=1800, is_public=True, duration_days=10,
        accommodation='''Rome (Days 1-6): Airbnb apartment in Trastevere — €80/night for a whole apartment, much better than a hotel. Trastevere is the best neighborhood: local, walkable, beautiful at night.
Florence (Days 7-10): B&B near Santa Croce — €65/night. Central, 10 min walk to the Uffizi and Duomo. Breakfast included.
PRO TIP: Book everything 2-3 months in advance for October. Prices double if you book last minute.''',
        highlights='''- Colosseum at golden hour — book the last entry slot of the day, the light is magical
- Vatican Museums + Sistine Chapel — the Sistine Chapel genuinely makes you stop breathing for a moment
- Eating cacio e pepe at a hole-in-the-wall in Trastevere at midnight
- Watching the sunset from Piazzale Michelangelo in Florence — the entire city turns golden
- Uffizi Gallery — Botticelli's Birth of Venus in person is completely different from photos
- Getting lost in the streets of Trastevere with no destination''',
        tips='''BOOKING: Book Colosseum, Vatican Museums, and Uffizi online weeks in advance. The queues without a booking can be 3+ hours.
FOOD: Never eat at restaurants right next to major tourist sites — you pay 3x for worse food. Walk 2 streets away minimum. Lunch is better value than dinner everywhere.
COFFEE: Never order a cappuccino after 11am in Italy, locals don't do it. Espresso standing at the bar is €1, sitting is €3.
TRANSPORT: Get a 48hr or 72hr Roma Pass for unlimited metro and bus. Florence is completely walkable, don't bother with transport.
MONEY: Italy is expensive but manageable. Budget €100-120/day including accommodation.
AVOID: Tourist menus (menu turistico) — they exist only to overcharge visitors. Any restaurant showing photos of food outside is a trap.
TIPPING: Not expected in Italy. Round up the bill if you want, that's enough.''',
image_filename='ROME.jpg')

    t5 = Trip(
        user_id=u2.id, name='Bali on a Shoestring', destination='Indonesia',
        start_date=date(2024,3,1), end_date=date(2024,3,14),
        budget=750, is_public=True, duration_days=14,
        accommodation='''Ubud (Days 1-5): Guesthouse run by a local family — $15/night including breakfast. Rice field view from the room. Jalan Bisma area is quiet and beautiful.
Canggu (Days 6-10): Surf bungalow 5 min walk from the beach — $20/night. Echo Beach area, great surf scene, lots of cafes and co-working spots.
Uluwatu (Days 11-14): Cliff-top guesthouse — $25/night. Dramatic views, closest base for Uluwatu Temple and the best surf in Bali.''',
        highlights='''- Tegallalang Rice Terraces on a scooter at 7am with no tourists — completely silent, just green
- Uluwatu Temple at sunset with the Kecak fire dance performance — one of the best things in Southeast Asia
- Surfing lesson at Batu Bolong Beach in Canggu — even if you've never surfed, you'll stand up
- Eating nasi goreng for 20,000 IDR ($1.20) at a warung at midnight
- Watching the sunrise over Mount Batur from the crater rim after a 2am hike
- Getting a traditional Balinese massage for $8/hour''',
        tips='''SCOOTER: Rent one in Ubud for $5-7/day, it's the only way to get around freely. International driving license technically required but rarely checked. Drive carefully, roads are narrow.
MONEY: ATMs everywhere but fees add up. Bring USD cash and exchange at money changers (avoid airport rates). Budget $40-55/day very comfortably.
FOOD: Eat at warungs (local family restaurants) not tourist cafes. A full meal is $1-2, same meal at a tourist spot is $8-12. Babi guling (suckling pig) at Ibu Oka in Ubud is worth the splurge ($4).
SURF: Kuta for beginners, Canggu for intermediate, Uluwatu for experienced. Take a lesson your first day, $25-30 for 2 hours with board and instructor.
TEMPLES: Bring a sarong or rent one at the entrance ($0.50). Dress respectfully, shoulders and knees covered.
AVOID: Kuta — it's loud, touristy and not the real Bali. Skip it entirely unless you want clubs.
SIM CARD: Telkomsel at the airport, $10 for 30GB. Essential for Maps navigation.''',
image_filename='BALI.jpg')

    db.session.add_all([t1, t2, t3, t4, t5])
    db.session.commit()

    # ── Places ─────────────────────────────────────────────────
    db.session.add_all([
        # Georgia
        Place(trip_id=t1.id, name='Narikala Fortress', category='Sightseeing', notes='Go at sunset — the view over the old town and the Mtkvari River is the best in Tbilisi. Completely free. Combine with a walk through the old town below.', est_cost=0, day_number=1, opening_hours='Always open', recommended=True),
        Place(trip_id=t1.id, name='Abanotubani Sulfur Baths', category='Culture', notes='Traditional Georgian sulfur baths, the smell hits you from a block away but inside it\'s incredible. Private rooms available for 2 people at 30 GEL/hour. Go for the Chreli-Abano for the most authentic experience.', est_cost=15, day_number=2, opening_hours='9am - 10pm', recommended=True),
        Place(trip_id=t1.id, name='Fabrika Complex', category='Food & Drink', notes='Former Soviet sewing factory turned into the coolest spot in Tbilisi. Surrounded by container cafes, bars, and restaurants. Best place for dinner and drinks. Very local crowd.', est_cost=8, day_number=1, opening_hours='12pm - 2am', recommended=True),
        Place(trip_id=t1.id, name='Gergeti Trinity Church', category='Nature', notes='The hike takes 2 hours each way. Start early to avoid afternoon clouds. The views of the Caucasus mountains and the Kazbegi valley are unlike anything. Wear proper shoes.', est_cost=0, day_number=4, opening_hours='Always open', recommended=True),
        Place(trip_id=t1.id, name='Prometheus Cave', category='Nature', notes='Near Kutaisi, one of the largest caves in the world. The colored lighting is a bit touristy but the formations are genuinely spectacular. Boat ride inside the cave is worth the extra 15 GEL.', est_cost=20, day_number=7, opening_hours='10am - 6pm', recommended=True),

        # Turkey
        Place(trip_id=t2.id, name='Hagia Sophia', category='Sightseeing', notes='Free entry since it became a mosque again. Go at 9am when it opens, by 11am it\'s packed. The scale of the interior is overwhelming — photos do not prepare you. Budget 1.5-2 hours.', est_cost=0, day_number=1, opening_hours='9am - 5pm (closed during prayer times)', recommended=True),
        Place(trip_id=t2.id, name='Grand Bazaar', category='Shopping', notes='One of the largest covered markets in the world, 4000 shops. Overwhelming but fascinating. Best for spices, ceramics, Turkish towels, and leather. Bargain hard — start at 30% of asking price. Don\'t feel pressured.', est_cost=30, day_number=2, opening_hours='9am - 7pm, closed Sunday', recommended=True),
        Place(trip_id=t2.id, name='Cappadocia Hot Air Balloon', category='Adventure', notes='Book 6-8 weeks in advance in summer. Sunrise departure, about 1 hour flight. Champagne breakfast included. The landscape from above is completely surreal — fairy chimneys, valleys, ancient cave cities. Do NOT skip this.', est_cost=150, day_number=5, opening_hours='Sunrise only, weather dependent', recommended=True),
        Place(trip_id=t2.id, name='Pamukkale Travertines', category='Nature', notes='Go at 8am before the crowds and the heat. You walk barefoot on the white calcium pools, which are warm and shallow. The ancient city of Hierapolis is right above — budget a full day for both.', est_cost=20, day_number=9, opening_hours='8am - 6pm', recommended=True),
        Place(trip_id=t2.id, name='Galata Bridge Fish Sandwich', category='Food & Drink', notes='Not a restaurant — the fishermen on the bridge grill fish and sell sandwiches for 30-40 TL. Balik ekmek (fish sandwich) with onions and lemon. One of the best street food experiences in Istanbul. Eat standing by the water.', est_cost=2, day_number=3, opening_hours='12pm - 10pm', recommended=True),

        # Alexandria
        Place(trip_id=t3.id, name='Stanley Beach', category='Beach', notes='Best beach in Alexandria. Go before 10am on a weekday — peaceful, clean, beautiful views of the bridge. By noon on weekends it gets very crowded. The corniche walk from here toward Rushdy is lovely.', est_cost=0, day_number=1, opening_hours='Always open', recommended=True),
        Place(trip_id=t3.id, name='Qaitbay Citadel', category='Sightseeing', notes='Built on the exact site of the ancient Lighthouse of Alexandria. The views of the Mediterranean from the top are stunning. Budget 1.5 hours. Entry is 100 EGP for foreigners. Go in the late afternoon for best light.', est_cost=5, day_number=2, opening_hours='9am - 4pm', recommended=True),
        Place(trip_id=t3.id, name='Abu Ashraf Seafood', category='Food & Drink', notes='Famous local seafood restaurant, been there for decades. You pick your fish fresh from the display and they grill it while you wait. Expect a queue on weekends. Completely worth it. Budget 150-200 EGP per person.', est_cost=8, day_number=1, opening_hours='12pm - 11pm', recommended=True),
        Place(trip_id=t3.id, name='El-Mursi Abul Abbas Mosque', category='Culture', notes='One of the most beautiful mosques in Egypt, built in 1767. The architecture is extraordinary, especially the interior courtyard. Visit at dusk when the light is golden and the call to prayer echoes across the water.', est_cost=0, day_number=2, opening_hours='Always open except during prayers', recommended=True),

        # Italy
        Place(trip_id=t4.id, name='Colosseum', category='Sightseeing', notes='Book the last entry slot of the day — the golden hour light is magical and crowds thin out. Include the Roman Forum and Palatine Hill in the same ticket, they are right next to each other and spectacular.', est_cost=20, day_number=1, opening_hours='9am - 7pm (last entry 1hr before)', recommended=True),
        Place(trip_id=t4.id, name='Vatican Museums & Sistine Chapel', category='Culture', notes='Easily a full day. Book early entry (8am) online. The Sistine Chapel is at the very end — take your time getting there, the galleries before it are extraordinary. No photos rule is loosely enforced but be respectful.', est_cost=25, day_number=3, opening_hours='9am - 6pm, closed Sunday (except last Sunday of month)', recommended=True),
        Place(trip_id=t4.id, name='Trastevere Dinner', category='Food & Drink', notes='Don\'t pick a specific restaurant — just walk into Trastevere at 8pm and wander until something looks good and local. Avoid anything with a host outside pulling you in. Cacio e pepe and carbonara are the things to order in Rome.', est_cost=25, day_number=2, opening_hours='7pm - midnight', recommended=True),
        Place(trip_id=t4.id, name='Uffizi Gallery', category='Culture', notes='Botticelli\'s Birth of Venus and Primavera are here. Book online — queues without a ticket are 2-3 hours. Budget 3-4 hours minimum. The building itself (designed by Vasari) is as impressive as the art inside.', est_cost=25, day_number=7, opening_hours='8:15am - 6:50pm, closed Monday', recommended=True),
        Place(trip_id=t4.id, name='Piazzale Michelangelo', category='Sightseeing', notes='The best view of Florence, a 20 minute uphill walk from the Ponte Vecchio. Go 30 minutes before sunset and stay for the afterglow. Bring a bottle of wine from a nearby enoteca and sit on the steps with everyone else.', est_cost=0, day_number=8, opening_hours='Always open', recommended=True),

        # Bali
        Place(trip_id=t5.id, name='Tegallalang Rice Terraces', category='Nature', notes='Go at 7am before tour groups arrive. The terraces are extraordinary — layered green as far as you can see. Rent a scooter the night before and drive up early. Entry is 15,000 IDR ($1). Bring mosquito spray.', est_cost=1, day_number=2, opening_hours='6am - 6pm', recommended=True),
        Place(trip_id=t5.id, name='Uluwatu Temple Sunset', category='Culture', notes='Perched on a 70m cliff over the Indian Ocean. The Kecak fire dance at sunset (starts 6pm, costs 100,000 IDR / $6) is one of the best performances in Southeast Asia. Watch your belongings — monkeys will steal anything shiny.', est_cost=6, day_number=11, opening_hours='7am - 7pm', recommended=True),
        Place(trip_id=t5.id, name='Mount Batur Sunrise Hike', category='Adventure', notes='Wake up at 1:30am, start hiking at 2am, reach the summit at sunrise (5:30am). You can see Mount Agung and the whole caldera from the top. Guide is mandatory ($35 including transport from Ubud). Bring warm clothes — it\'s cold at the top.', est_cost=35, day_number=4, opening_hours='Night hike, summit at sunrise', recommended=True),
        Place(trip_id=t5.id, name='Ibu Oka Babi Guling', category='Food & Drink', notes='The most famous warung in Ubud. Suckling pig roasted with Balinese spices, served with rice, crispy skin, and sambal. Anthony Bourdain ate here. A full plate is 50,000 IDR ($3). Opens at 11am, sells out by 2pm. Go early.', est_cost=3, day_number=3, opening_hours='11am - 3pm (sells out early)', recommended=True),
        Place(trip_id=t5.id, name='Batu Bolong Surf Lesson', category='Adventure', notes='Best beginner surf spot in Canggu. Many surf schools on the beach, walk up and negotiate — 250,000-300,000 IDR for 2 hours with board and instructor. Waves are consistent and manageable. You will stand up.', est_cost=18, day_number=6, opening_hours='7am - 6pm', recommended=True),
    ])
    db.session.commit()

    # ── Reviews ────────────────────────────────────────────────
    db.session.add_all([
        Review(trip_id=t1.id, user_id=u2.id, rating=5, comment='Georgia completely blew my mind. The Kazbegi section alone is worth the trip. Sara\'s tip about the shared taxi from Didube saved us so much money. The guesthouse dinner with the local family was the highlight of our whole year.', created_at=datetime(2024,10,5)),
        Review(trip_id=t1.id, user_id=u3.id, rating=5, comment='Used this guide for my trip last month. Everything was accurate. The sulfur baths were exactly as described — intense smell but incredible experience. Fabrika complex is exactly as cool as it sounds.', created_at=datetime(2024,10,12)),
        Review(trip_id=t2.id, user_id=u1.id, rating=5, comment='The balloon ride tip about booking in advance is so important — we almost missed it. Cappadocia is genuinely one of the most surreal places on earth. Karim\'s food advice saved us a lot of money in Istanbul.', created_at=datetime(2024,9,3)),
        Review(trip_id=t2.id, user_id=u3.id, rating=4, comment='Great guide. Only thing I\'d add is that Pamukkale village is a bit of a tourist trap — eat inside the site complex instead. The overnight bus tip is gold, saved a hotel night.', created_at=datetime(2024,9,15)),
        Review(trip_id=t3.id, user_id=u1.id, rating=4, comment='Perfect Alexandria weekend guide. Abu Ashraf is exactly as good as described — the queue was 45 minutes but completely worth it. The Qaitbay tip about going late afternoon for the light is spot on.', created_at=datetime(2024,6,1)),
        Review(trip_id=t4.id, user_id=u2.id, rating=5, comment='The Trastevere accommodation recommendation was perfect. Booking Vatican early entry made such a difference. The Piazzale Michelangelo sunset with wine from a local shop was the best evening of the trip.', created_at=datetime(2024,11,5)),
        Review(trip_id=t5.id, user_id=u1.id, rating=5, comment='Bali on a shoestring is completely doable with this guide. The scooter tip is 100% correct — you can\'t explore Ubud properly without one. Ibu Oka was life-changing. Mount Batur sunrise was cold but worth every sleepless minute.', created_at=datetime(2024,4,2)),
        Review(trip_id=t5.id, user_id=u3.id, rating=4, comment='Followed this guide almost exactly. The only thing I\'d add is to spend more time in Ubud — 5 days wasn\'t enough. Canggu is great but gets expensive fast if you\'re not careful with restaurants.', created_at=datetime(2024,4,20)),
    ])
    db.session.commit()

    # ── Wishlists ──────────────────────────────────────────────
    db.session.add_all([
        Wishlist(user_id=u1.id, title='Dream Trip: Japan in Cherry Blossom Season', destination='Japan', description='Tokyo, Kyoto, Osaka in late March. See cherry blossoms in Maruyama Park, eat ramen everywhere, visit Fushimi Inari at 5am before crowds.', estimated_budget=2500, duration_days=14, is_public=True, created_at=datetime(2024,8,1)),
        Wishlist(user_id=u2.id, title='Morocco on a Budget', destination='Morocco', description='Marrakech, Chefchaouen, Sahara desert camp. 10 days, trying to keep it under $600 total. Anyone done this recently?', estimated_budget=600, duration_days=10, is_public=True, created_at=datetime(2024,9,10)),
        Wishlist(user_id=u3.id, title='Solo Trip: Portugal & Spain', destination='Portugal & Spain', description='Lisbon, Porto, Seville, Granada. 2 weeks, solo travel, hostels. The Alhambra is the main reason for the trip.', estimated_budget=1200, duration_days=14, is_public=True, created_at=datetime(2024,10,3)),
    ])
    db.session.commit()

    print('database seeded successfully with full detailed data')
