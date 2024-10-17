from flask import Flask, render_template, request

app = Flask(__name__)

vocabularies = {
    "Anarana": "Name",
    "Fianakaviana": "Family",
    "Sakafo": "Food",
    "Fitiavana": "Love",
    "Vola": "Money",
    "Trano": "House",
    "Vehivavy": "Woman",
    "Lehilahy": "Man",
    "Zaza": "Child",
    "Sekoly": "School",
    "Asa": "Work",
    "Vavaka": "Prayer",
    "Lalana": "Road",
    "Fiara": "Car",
    "Boky": "Book",
    "Fahasalamana": "Health",
    "Tsy": "No",
    "Eny": "Yes",
    "Azafady": "Sorry",
    "Misaotra": "Thank you",
    "Tsara": "Good",
    "Ratsy": "Bad",
    "Haingana": "Fast",
    "Miadana": "Slow",
    "Vehivavy": "Female",
    "Lehilahy": "Male",
    "Aiza": "Where",
    "Oviana": "When",
    "Fa": "But",
    "Rano": "Water",
    "Vary": "Rice",
    "Zavatra": "Thing",
    "Firenena": "Country",
    "Hazo": "Tree",
    "Rivotra": "Wind",
    "Tany": "Land",
    "Lohataona": "Spring",
    "Fahavaratra": "Summer",
    "Ririnina": "Winter",
    "Fararano": "Autumn",
    "Orana": "Rain",
    "Volana": "Month",
    "Taona": "Year",
    "Lalao": "Game",
    "Volana": "Moon",
    "Masina": "Holy",
    "Zo": "Right",
    "Adidy": "Duty",
    "Hery": "Strength",
    "Fitiavana": "Affection",
    "Fitsangatsanganana": "Trip",
    "Valiny": "Answer",
    "Fanontaniana": "Question",
    "Lamba": "Clothes",
    "Kiraro": "Shoes",
    "Lohan-draha": "Head",
    "Tanana": "Hand",
    "Maso": "Eye",
    "Vava": "Mouth",
    "Soavaly": "Horse",
    "Mpiara-miasa": "Colleague",
    "Mpampianatra": "Teacher",
    "Mpianatra": "Student",
    "Vehivavy": "Girl",
    "Lelako": "Tongue",
    "Fombafomba": "Custom",
    "Olona": "Person",
    "Fahasahiana": "Courage",
    "Efitra": "Room",
    "Fanadiovana": "Cleaning",
    "Fiarahabana": "Greetings",
    "Lisitry": "List",
    "Hafatra": "Message",
    "Fikambanana": "Association",
    "Fananganana": "Establishment",
    "Mividy": "Buy",
    "Mivarotra": "Sell",
    "Vola": "Money",
    "Fiainana": "Life",
    "Fahasambarana": "Happiness",
    "Fitiavana": "Kindness",
    "Neny": "Mother",
    "Dada": "Father",
    "Rahalahy": "Brother",
    "Anabavy": "Sister",
    "Zandriny": "Youngest",
    "Fandriana": "Bed",
    "Telefaonina": "Phone",
    "Loharano": "Source",
    "Voninkazo": "Flower",
    "Alina": "Night",
    "Ampitso": "Tomorrow",
    "Andro": "Day",
    "Aty": "Here",
    "Tsy": "Not",
    "Eny": "Yes",
    "Tiana": "Wanted",
    "Asakasak’izay": "Indifferent",
    "An-danitra": "Heaven",
    "Tany": "Earth",
    "Raharaha": "Affair",
    "Fisainana": "Thought",
    "Tsy rariny": "Injustice",
    "Zo": "Rights",
    "Raharaha": "Case",
    "Fitsarana": "Court",
    "Polisy": "Police",
    "Dokotera": "Doctor",
    "Mpampivelona": "Midwife",
    "Faritra": "Region",
    "Fiaraha-miasa": "Cooperation",
    "Firaisankina": "Unity",
    "Fitohizan'ny tantara": "Continuation",
    "Tranonkala": "Website",
    "Fandaharanasa": "Program",
    "Vehivavy": "Lady",
    "Rano": "Liquid",
    "Sira": "Salt",
    "Sakafo": "Meal",
    "Tsara tarehy": "Beautiful",
    "Fifaliana": "Joy",
    "Horonan-tsary": "Video",
    "Sary": "Image",
    "Gazety": "Newspaper",
    "Vaovao": "News",
    "Filazana": "Announcement",
    "Fianarana": "Learning",
    "Sekoly": "School",
    "Vehivavy": "Woman",
    "Lehilahy": "Man",
    "Zaza": "Kid",
    "Volana": "Month",
    "Taona": "Year",
    "Rano": "Water",
    "Rivotra": "Wind",
    "Vavaka": "Prayer",
    "Zavatra": "Thing",
    "Ady": "Fight",
    "Fitoniana": "Calm",
    "Manao": "Do",
    "Mampianatra": "Teach",
    "Mianatra": "Learn",
    "Fahazavana": "Light",
    "Afo": "Fire",
    "Rano": "Water",
    "Tanety": "Highland",
    "Akanjo": "Clothes",
    "Fanomezana": "Gift",
    "Vary": "Rice",
    "Fiara": "Car",
    "Zavamaniry": "Plant",
    "Zavaboary": "Nature",
    "Fandehanana": "Walking",
    "Mitondra": "Lead",
    "Masoandro": "Sun",
    "Ala": "Forest",
    "Tanàna": "Town",
    "Fambolena": "Agriculture",
    "Rano fisotro": "Drinking water",
    "Birao": "Office",
    "Fanapahan-kevitra": "Decision",
    "Fitaterana": "Transport",
    "Fahatokisana": "Trust",
    "Fanoloran-tena": "Dedication",
    "Fialamboly": "Entertainment",
    "Fianarana": "Studies",
    "Fikarohana": "Research",
    "Trano fotsy": "White house",
    "Fahaizana": "Skills",
    "Fanofanana": "Training",
    "Fikambanana": "Organization",
    "Teny": "Word",
    "Fanantenana": "Hope",
    "Fandrosoana": "Progress",
    "Lalana": "Path",
    "Sampanana": "Branch",
    "Varotra": "Market",
    "Fahasalamana": "Well-being",
    "Raharaha": "Job",
    "Hevitra": "Opinion",
    "Tombony": "Advantage",
    "Filazana": "Statement",
    "Hevitra": "Idea",
    "Fianarana": "Studies",
    "Fikarohana": "Research",
    "Trano fotsy": "White house",
    "Fahaizana": "Skills",
    "Fanofanana": "Training",
    "Fikambanana": "Organization",
    "Teny": "Word",
    "Fanantenana": "Hope",
    "Fandrosoana": "Progress",
    "Lalana": "Path",
    "Sampanana": "Branch",
    "Varotra": "Market",
    "Fahasalamana": "Well-being",
    "Raharaha": "Job",
    "Hevitra": "Opinion",
    "Tombony": "Advantage",
    "Filazana": "Statement",
    "Hevitra": "Idea",
    "Fanapahan-kevitra": "Decision",
    "Fanaporofoana": "Evidence",
    "Famoronana": "Creation",
    "Fandraisana": "Reception",
    "Fiovana": "Change",
    "Fitsapana": "Test",
    "Fiaraha-miasa": "Collaboration",
    "Fanomezana": "Gift",
    "Fankasitrahana": "Gratitude",
    "Fahafahana": "Freedom",
    "Fampiharana": "Application",
    "Fanjakana": "Government",
    "Tanàna": "City",
    "Fampianarana": "Education",
    "Fanajana": "Respect",
    "Fiarovana": "Protection",
    "Fepetra": "Condition",
    "Famerenana": "Restoration",
    "Fifandraisana": "Communication",
    "Fanadinana": "Examination",
    "Fiangonana": "Church",
    "Fahavitanana": "Completion",
    "Fahatakarana": "Understanding",
    "Fiainana": "Life",
    "Fangatahana": "Request",
    "Fanomezana-toky": "Guarantee",
    "Fiaviana": "Origin",
    "Fisorohana": "Prevention",
    "Fanentanana": "Campaign",
    "Fahatokisana": "Trust",
    "Fiaraha-monina": "Community",
    "Fampitahana": "Comparison",
    "Fihazonana": "Maintenance",
    "Fampitandremana": "Warning",
    "Fampiononana": "Comfort",
    "Fanitarana": "Expansion",
    "Fikatsahana": "Pursuit",
    "Fihetseham-po": "Emotion",
    "Fanazavana": "Explanation",
    "Fanekena": "Approval",
    "Fanombohana": "Beginning",
    "Fanatanterahana": "Execution",
    "Fanorenana": "Construction",
    "Fijerena": "Observation",
    "Fifaninanana": "Competition",
    "Fihetsehana": "Movement",
    "Fanamafisana": "Confirmation",
    "Famelàna": "Forgiveness",
    "Fanomezana-tsiny": "Blame",
    "Fampiharana": "Implementation",
    "Fanolorana": "Presentation",
    "Fivoriana": "Meeting",
    "Fanatrehana": "Attendance",
    "Fifadian-kanina": "Fasting",
    "Famakafakana": "Analysis",
    "Famoriam-bahoaka": "Assembly",
    "Fanontaniana": "Question",
    "Fanamarihana": "Remark",
    "Fanapotehina": "Destruction",
    "Fampandriana": "Accommodation",
    "Fanafody": "Medicine",
    "Fanatontoloana": "Globalization",
    "Fanekena": "Consent",
    "Fanatsarana": "Improvement",
    "Fanampiana": "Assistance",
    "Fandaminana": "Organization",
    "Fanaovana": "Implementation",
    "Fiaraha-mientana": "Solidarity",
    "Fahatapahan-kevitra": "Resolution",
    "Fanofanana": "Mentoring",
    "Fankatoavana": "Recognition",
    "Fandavana": "Refusal",
    "Fifanakalozana": "Exchange",
    "Fialam-boly": "Entertainment",
    "Fiaraha-mivavaka": "Prayer",
    "Fifanohanana": "Support",
    "Famoronana": "Innovation",
    "Fandriampahalemana": "Peace",
    "Fifanarahana": "Agreement",
    "Fisoratana anarana": "Registration",
    "Fahombiazan-tsaina": "Motivation",
    "Fanohizana": "Continuation",
    "Fandefasana": "Transmission",
    "Fanafainganana": "Acceleration",
    "Fahaizana manokana": "Expertise",
    "Fanaraha-maso": "Control",
    "Fananganana": "Establishment",
    "Famokarana": "Production",
    "Fiaraha-miasa": "Partnership",
    "Fiaraha-miory": "Sympathy",
    "Fanamarihana": "Marking",
    "Fanolorana andraikitra": "Delegation",
    "Fanazavana": "Clarification",
    "Fandaminana": "Coordination",
    "Fanekem-pinoana": "Faith declaration",
    "Fifandraisana ara-bola": "Financial relations",
    "Fanatsarana": "Optimization",
    "Fanatontosana": "Fulfillment",
    "Fihavaozana": "Renewal",
    "Fanoratana": "Writing",
    "Fahavitana": "Achievement",
    "Fisoratana anarana": "Enrollment",
    "Fanafarana": "Import",
    "Fahaterahana": "Birth",
    "Fanambadiana": "Marriage",
    "Fifankahitana": "Reunion",
    "Fanalahidy": "Key",
    "Fanantenana vaovao": "New hope",
    "Fisorohana": "Prevention",
    "Fianarana tsy tapaka": "Continuous learning",
    "Fanomezana voninahitra": "Honor",
    "Fahasoavana": "Grace",
    "Fampiroboroboana": "Promotion",
    "Fanatsarana vaovao": "Upgrade",
    "Fiainana maharitra": "Sustainability",
    "Fisoratana": "Signature",
    "Fanajana": "Respect",
    "Fanomezam-pahasoavana": "Gift of grace",
    "Fanontam-pahendrena": "Wisdom inquiry",
    "Fifaliana": "Joy",
    "Fampanantenana": "Promise",
    "Fiainana mandrakizay": "Eternal life",
    "Fahamarinan-toetra": "Integrity",
    "Fanovàna": "Transformation",
    "Fandaharan'asa": "Program",
    "Fifandraisana ara-tsosialy": "Social connections",
    "Fahatokisan-tena": "Self-confidence",
    "Fanaingoana": "Decoration",
    "Fandriana": "Bed",
    "Fanafahana": "Liberation",
    "Fandinihana": "Research",
    "Fampianarana": "Training",
    "Fiaraha-miombon'antoka": "Partnership",
    "Fifandraisana matihanina": "Professional relationship",
    "Fanoratana": "Enrollment",
    "Famaritana": "Definition",
    "Fiainana mandrakizay": "Eternal life",
    "Fampitomboana": "Increase",
    "Fanaovana asa": "Work accomplishment",
    "Fanohizana": "Continuation",
    "Fanohanana ara-bola": "Financial support",
    "Fanitsiana": "Correction",
    "Fihazonana andraikitra": "Responsibility holding",
    "Fanomezana andraikitra": "Delegation"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    result = vocabularies.get(query.capitalize(), "Word not found")
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
