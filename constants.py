# Auto-generated constants from simulator.py

import typing

PREFECTURE_NAMES = [
    "Hokkaido", "Aomori", "Iwate", "Miyagi", "Akita", "Yamagata", "Fukushima", "Ibaraki", "Tochigi", "Gunma",
    "Saitama", "Chiba", "Tokyo", "Kanagawa", "Niigata", "Toyama", "Ishikawa", "Fukui", "Yamanashi", "Nagano",
    "Gifu", "Shizuoka", "Aichi", "Mie", "Shiga", "Kyoto", "Osaka", "Hyogo", "Nara", "Wakayama", "Tottori",
    "Shimane", "Okayama", "Hiroshima", "Yamaguchi", "Tokushima", "Kagawa", "Ehime", "Kochi", "Fukuoka",
    "Saga", "Nagasaki", "Kumamoto", "Oita", "Miyazaki", "Kagoshima", "Okinawa"
]

# Placeholder GDP data (e.g., in Billions USD) - From previous step
PREFECTURE_GDP_PLACEHOLDERS = {
    "Tokyo": 1000, "Osaka": 400, "Aichi": 380, "Kanagawa": 350, "Saitama": 230, "Chiba": 210, "Hyogo": 200,
    "Fukuoka": 190, "Hokkaido": 180, "Shizuoka": 170, "Ibaraki": 130, "Hiroshima": 120, "Kyoto": 110,
    "Niigata": 100, "Miyagi": 95, "Gunma": 90, "Tochigi": 88, "Okayama": 85, "Gifu": 80, "Nagano": 78,
    "Mie": 75, "Fukushima": 70, "Shiga": 68, "Yamaguchi": 65, "Kumamoto": 60, "Ehime": 58, "Kagoshima": 55,
    "Toyama": 53, "Ishikawa": 52, "Wakayama": 50, "Oita": 48, "Yamagata": 46, "Nagasaki": 45, "Yamanashi": 44,
    "Aomori": 43, "Iwate": 42, "Akita": 40, "Miyazaki": 38, "Fukui": 37, "Kagawa": 36, "Tokushima": 35,
    "Saga": 34, "Nara": 33, "Okinawa": 32, "Kochi": 30, "Shimane": 28, "Tottori": 25
}

# ** NEW: Placeholder Population Growth Rates (% per year) **
# Based on general trends (Tokyo/Okinawa positive, many rural negative) - Needs real data
PREFECTURE_GROWTH_RATES = {
    "Tokyo": 0.4, "Kanagawa": 0.1, "Saitama": 0.05, "Chiba": 0.0, "Aichi": 0.0, "Osaka": -0.1, "Fukuoka": 0.05,
    "Okinawa": 0.3, "Shiga": 0.0,
    # Most others slightly negative or more significantly negative
    "Hokkaido": -0.5, "Aomori": -1.0, "Iwate": -0.9, "Miyagi": -0.3, "Akita": -1.5, "Yamagata": -1.1, "Fukushima": -0.8,
    "Ibaraki": -0.4, "Tochigi": -0.5, "Gunma": -0.6, "Niigata": -0.9, "Toyama": -0.7, "Ishikawa": -0.6, "Fukui": -0.7,
    "Yamanashi": -0.6, "Nagano": -0.7, "Gifu": -0.5, "Shizuoka": -0.4, "Mie": -0.6, "Kyoto": -0.3, "Hyogo": -0.3,
    "Nara": -0.7, "Wakayama": -1.0, "Tottori": -0.9, "Shimane": -1.1, "Okayama": -0.3, "Hiroshima": -0.2, "Yamaguchi": -0.8,
    "Tokushima": -1.0, "Kagawa": -0.6, "Ehime": -0.9, "Kochi": -1.1, "Saga": -0.7, "Nagasaki": -1.0, "Kumamoto": -0.5,
    "Oita": -0.8, "Miyazaki": -0.9, "Kagoshima": -0.8
}

# ** NEW: Population data parsed from Wikipedia search results (Oct 1, 2022 figures) **
PREFECTURE_POPULATIONS = {
    'Tokyo': 14038167, 'Kanagawa': 9232489, 'Osaka': 8782484, 'Aichi': 7495171,
    'Saitama': 7337089, 'Chiba': 6265975, 'Hyogo': 5402493, 'Hokkaido': 5140354,
    'Fukuoka': 5116046, 'Shizuoka': 3582297, 'Ibaraki': 2839555, 'Hiroshima': 2759500,
    'Kyoto': 2549749, 'Miyagi': 2279977, 'Niigata': 2152693, 'Nagano': 2019993,
    'Gifu': 1945763, 'Gunma': 1913254, 'Tochigi': 1908821, 'Okayama': 1862317,
    'Fukushima': 1790181, 'Mie': 1742174, 'Kumamoto': 1718327, 'Kagoshima': 1562662,
    'Okinawa': 1468318, 'Shiga': 1408931, 'Yamaguchi': 1313403, 'Ehime': 1306486,
    'Nara': 1305812, 'Nagasaki': 1283128, 'Aomori': 1204392, 'Iwate': 1180595,
    'Ishikawa': 1117637, 'Oita': 1106831, 'Miyazaki': 1052338, 'Yamagata': 1041025,
    'Toyama': 1016534, 'Kagawa': 934060, 'Akita': 929901, 'Wakayama': 903265,
    'Yamanashi': 801874, 'Saga': 800787, 'Fukui': 752855, 'Tokushima': 703852,
    'Kochi': 675705, 'Shimane': 657909, 'Tottori': 543620
}

PREFECTURE_GDP_PLACEHOLDERS = {
    "Tokyo": 1000, "Osaka": 400, "Aichi": 380, "Kanagawa": 350, "Saitama": 230, "Chiba": 210, "Hyogo": 200,
    "Fukuoka": 190, "Hokkaido": 180, "Shizuoka": 170, "Ibaraki": 130, "Hiroshima": 120, "Kyoto": 110,
    "Niigata": 100, "Miyagi": 95, "Gunma": 90, "Tochigi": 88, "Okayama": 85, "Gifu": 80, "Nagano": 78,
    "Mie": 75, "Fukushima": 70, "Shiga": 68, "Yamaguchi": 65, "Kumamoto": 60, "Ehime": 58, "Kagoshima": 55,
    "Toyama": 53, "Ishikawa": 52, "Wakayama": 50, "Oita": 48, "Yamagata": 46, "Nagasaki": 45, "Yamanashi": 44,
    "Aomori": 43, "Iwate": 42, "Akita": 40, "Miyazaki": 38, "Fukui": 37, "Kagawa": 36, "Tokushima": 35,
    "Saga": 34, "Nara": 33, "Okinawa": 32, "Kochi": 30, "Shimane": 28, "Tottori": 25
}

# ** NEW: Placeholder Population Growth Rates (% per year) **
# Based on general trends (Tokyo/Okinawa positive, many rural negative) - Needs real data
PREFECTURE_GROWTH_RATES = {
    "Tokyo": 0.4, "Kanagawa": 0.1, "Saitama": 0.05, "Chiba": 0.0, "Aichi": 0.0, "Osaka": -0.1, "Fukuoka": 0.05,
    "Okinawa": 0.3, "Shiga": 0.0,
    # Most others slightly negative or more significantly negative
    "Hokkaido": -0.5, "Aomori": -1.0, "Iwate": -0.9, "Miyagi": -0.3, "Akita": -1.5, "Yamagata": -1.1, "Fukushima": -0.8,
    "Ibaraki": -0.4, "Tochigi": -0.5, "Gunma": -0.6, "Niigata": -0.9, "Toyama": -0.7, "Ishikawa": -0.6, "Fukui": -0.7,
    "Yamanashi": -0.6, "Nagano": -0.7, "Gifu": -0.5, "Shizuoka": -0.4, "Mie": -0.6, "Kyoto": -0.3, "Hyogo": -0.3,
    "Nara": -0.7, "Wakayama": -1.0, "Tottori": -0.9, "Shimane": -1.1, "Okayama": -0.3, "Hiroshima": -0.2, "Yamaguchi": -0.8,
    "Tokushima": -1.0, "Kagawa": -0.6, "Ehime": -0.9, "Kochi": -1.1, "Saga": -0.7, "Nagasaki": -1.0, "Kumamoto": -0.5,
    "Oita": -0.8, "Miyazaki": -0.9, "Kagoshima": -0.8
}

# ** NEW: Population data parsed from Wikipedia search results (Oct 1, 2022 figures) **
PREFECTURE_POPULATIONS = {
    'Tokyo': 14038167, 'Kanagawa': 9232489, 'Osaka': 8782484, 'Aichi': 7495171,
    'Saitama': 7337089, 'Chiba': 6265975, 'Hyogo': 5402493, 'Hokkaido': 5140354,
    'Fukuoka': 5116046, 'Shizuoka': 3582297, 'Ibaraki': 2839555, 'Hiroshima': 2759500,
    'Kyoto': 2549749, 'Miyagi': 2279977, 'Niigata': 2152693, 'Nagano': 2019993,
    'Gifu': 1945763, 'Gunma': 1913254, 'Tochigi': 1908821, 'Okayama': 1862317,
    'Fukushima': 1790181, 'Mie': 1742174, 'Kumamoto': 1718327, 'Kagoshima': 1562662,
    'Okinawa': 1468318, 'Shiga': 1408931, 'Yamaguchi': 1313403, 'Ehime': 1306486,
    'Nara': 1305812, 'Nagasaki': 1283128, 'Aomori': 1204392, 'Iwate': 1180595,
    'Ishikawa': 1117637, 'Oita': 1106831, 'Miyazaki': 1052338, 'Yamagata': 1041025,
    'Toyama': 1016534, 'Kagawa': 934060, 'Akita': 929901, 'Wakayama': 903265,
    'Yamanashi': 801874, 'Saga': 800787, 'Fukui': 752855, 'Tokushima': 703852,
    'Kochi': 675705, 'Shimane': 657909, 'Tottori': 543620
}

PREFECTURE_GROWTH_RATES = {
    "Tokyo": 0.4, "Kanagawa": 0.1, "Saitama": 0.05, "Chiba": 0.0, "Aichi": 0.0, "Osaka": -0.1, "Fukuoka": 0.05,
    "Okinawa": 0.3, "Shiga": 0.0,
    # Most others slightly negative or more significantly negative
    "Hokkaido": -0.5, "Aomori": -1.0, "Iwate": -0.9, "Miyagi": -0.3, "Akita": -1.5, "Yamagata": -1.1, "Fukushima": -0.8,
    "Ibaraki": -0.4, "Tochigi": -0.5, "Gunma": -0.6, "Niigata": -0.9, "Toyama": -0.7, "Ishikawa": -0.6, "Fukui": -0.7,
    "Yamanashi": -0.6, "Nagano": -0.7, "Gifu": -0.5, "Shizuoka": -0.4, "Mie": -0.6, "Kyoto": -0.3, "Hyogo": -0.3,
    "Nara": -0.7, "Wakayama": -1.0, "Tottori": -0.9, "Shimane": -1.1, "Okayama": -0.3, "Hiroshima": -0.2, "Yamaguchi": -0.8,
    "Tokushima": -1.0, "Kagawa": -0.6, "Ehime": -0.9, "Kochi": -1.1, "Saga": -0.7, "Nagasaki": -1.0, "Kumamoto": -0.5,
    "Oita": -0.8, "Miyazaki": -0.9, "Kagoshima": -0.8
}

# ** NEW: Population data parsed from Wikipedia search results (Oct 1, 2022 figures) **
PREFECTURE_POPULATIONS = {
    'Tokyo': 14038167, 'Kanagawa': 9232489, 'Osaka': 8782484, 'Aichi': 7495171,
    'Saitama': 7337089, 'Chiba': 6265975, 'Hyogo': 5402493, 'Hokkaido': 5140354,
    'Fukuoka': 5116046, 'Shizuoka': 3582297, 'Ibaraki': 2839555, 'Hiroshima': 2759500,
    'Kyoto': 2549749, 'Miyagi': 2279977, 'Niigata': 2152693, 'Nagano': 2019993,
    'Gifu': 1945763, 'Gunma': 1913254, 'Tochigi': 1908821, 'Okayama': 1862317,
    'Fukushima': 1790181, 'Mie': 1742174, 'Kumamoto': 1718327, 'Kagoshima': 1562662,
    'Okinawa': 1468318, 'Shiga': 1408931, 'Yamaguchi': 1313403, 'Ehime': 1306486,
    'Nara': 1305812, 'Nagasaki': 1283128, 'Aomori': 1204392, 'Iwate': 1180595,
    'Ishikawa': 1117637, 'Oita': 1106831, 'Miyazaki': 1052338, 'Yamagata': 1041025,
    'Toyama': 1016534, 'Kagawa': 934060, 'Akita': 929901, 'Wakayama': 903265,
    'Yamanashi': 801874, 'Saga': 800787, 'Fukui': 752855, 'Tokushima': 703852,
    'Kochi': 675705, 'Shimane': 657909, 'Tottori': 543620
}

PREFECTURE_POPULATIONS = {
    'Tokyo': 14038167, 'Kanagawa': 9232489, 'Osaka': 8782484, 'Aichi': 7495171,
    'Saitama': 7337089, 'Chiba': 6265975, 'Hyogo': 5402493, 'Hokkaido': 5140354,
    'Fukuoka': 5116046, 'Shizuoka': 3582297, 'Ibaraki': 2839555, 'Hiroshima': 2759500,
    'Kyoto': 2549749, 'Miyagi': 2279977, 'Niigata': 2152693, 'Nagano': 2019993,
    'Gifu': 1945763, 'Gunma': 1913254, 'Tochigi': 1908821, 'Okayama': 1862317,
    'Fukushima': 1790181, 'Mie': 1742174, 'Kumamoto': 1718327, 'Kagoshima': 1562662,
    'Okinawa': 1468318, 'Shiga': 1408931, 'Yamaguchi': 1313403, 'Ehime': 1306486,
    'Nara': 1305812, 'Nagasaki': 1283128, 'Aomori': 1204392, 'Iwate': 1180595,
    'Ishikawa': 1117637, 'Oita': 1106831, 'Miyazaki': 1052338, 'Yamagata': 1041025,
    'Toyama': 1016534, 'Kagawa': 934060, 'Akita': 929901, 'Wakayama': 903265,
    'Yamanashi': 801874, 'Saga': 800787, 'Fukui': 752855, 'Tokushima': 703852,
    'Kochi': 675705, 'Shimane': 657909, 'Tottori': 543620
}



DEFAULT_PARTY_NAME = "Liberal Democratic Party"

class Prefecture:
    # ** MODIFIED: Added population_growth_rate **
    def __init__(self, name, population=None, gdp=None, growth_rate=None):
        self.name = name
        # Use float for population internally to handle fractional growth
        self.population = float(population) if population is not None else float(random.randint(500000, 10000000))
        self.gdp = float(gdp) if gdp is not None else random.uniform(20.0, 100.0) # Billions USD
        self.economy = random.uniform(0.5, 1.5)
        self.approval = random.uniform(40.0, 60.0)
        self.unemployment = random.uniform(3.0, 10.0)
        # ** NEW: Population Growth Rate (% per year) **
        self.population_growth_rate = float(growth_rate) if growth_rate is not None else random.uniform(-1.0, 0.5) # Annual rate

    # ** NEW: Method for daily population update **
    def update_daily_population(self):
        """Updates population based on the annual growth rate, applied daily."""
        # Convert annual rate to daily rate (approximation)
        daily_rate_multiplier = (1.0 + self.population_growth_rate / 100.0)**(1.0/365.0)
        self.population *= daily_rate_multiplier
        # Keep population as float internally, can round for display if needed

    def normalize_values(self):
        """Ensure all values are within valid ranges"""
        self.approval = min(100.0, max(0.0, self.approval))
        self.unemployment = min(30.0, max(1.0, self.unemployment))
        self.economy = min(3.0, max(0.1, self.economy))
        self.gdp = max(1.0, self.gdp)
        self.population = max(1000.0, self.population) # Ensure pop doesn't go below a minimum threshold
        # Optional: Clamp growth rate?
        # self.population_growth_rate = min(5.0, max(-5.0, self.population_growth_rate))

    def get_gdp_per_capita(self):
        if self.population > 0:
            return (self.gdp * 1_000_000_000) / self.population
        return 0

    # ** NEW: Convenience method to get integer population for display/some calcs **
    def get_population_int(self):
        return int(round(self.population))


class PrimeMinister:
    def __init__(self, name, party_name):
        self.name = name
        self.party_name = party_name
        self.global_approval = 50.0
        self.base_popularity = random.uniform(50.0, 70.0)
        self.economy_skill = random.uniform(0.5, 1.5)
        self.unemployment_skill = random.uniform(0.5, 1.5)
        self.welfare_skill = random.uniform(0.5, 1.5)
        # ** NEW: Skill related to demographics/growth policies? **
        self.demographics_skill = random.uniform(0.5, 1.5)

    def calculate_global_approval(self, prefectures):
        total_approval = 0
        total_population = 0
        for prefecture in prefectures:
            pop_int = prefecture.get_population_int() # Use integer pop for weighting
            total_approval += prefecture.approval * pop_int
            total_population += pop_int
        if total_population > 0:
            self.global_approval = min(100.0, max(0.0, (total_approval / total_population)))
        else:
            self.global_approval = 0.0 # Handle case of zero population
        return self.global_approval

class RivalParty:
    def __init__(self, name):
        self.name = name
        self.base_popularity = random.uniform(40.0, 60.0)
        # ** NEW: Attributes for attack strength? **
        self.attack_skill = random.uniform(0.8, 1.2)
        self.preferred_attack = random.choice(["economy", "scandal", "welfare", "competence"])

    # ** NEW: Method to generate an attack message/effect **
    def generate_attack(self):
        """Generates a random attack message and potential approval impact."""
        attack_type = self.preferred_attack
        # Base impact range before skill modification
        base_impact = random.uniform(0.5, 2.5)
        # Modify impact by party's skill
        impact = base_impact * self.attack_skill

        messages = {
            "economy": [
                f"{self.name} criticizes the government's failed economic policies!",
                f"'{self.party_name}'s economic plan is hurting families,' claims {self.name}.",
                f"{self.name} points to rising inflation under the current administration."
            ],
            "scandal": [
                f"{self.name} hints at potential corruption within the cabinet.",
                f"Questions raised by {self.name} about the PM's transparency.",
                f"{self.name} calls for an investigation into government spending."
            ],
            "welfare": [
                f"{self.name} argues that welfare programs are being neglected.",
                f"'{self.party_name} doesn't care about the elderly,' says {self.name}.",
                f"{self.name} promises better social support if elected."
            ],
            "competence": [
                f"{self.name} slams the government's handling of recent events.",
                f"'{self.party_name} is out of touch with the people,' states {self.name}.",
                f"{self.name} questions the PM's leadership abilities."
            ]
        }
        message = random.choice(messages.get(attack_type, messages["competence"]))
        return message, impact # Returns the message and the calculated approval hit


class CountryStatistics:
    def __init__(self):
        self.economy = {
            'gdp_ppp': 6.31, 'gdp_nominal': 4.204, 'gdp_per_capita': 36990.33,
            'inflation': 3.2, 'growth_rate': 0.9,
        }
        self.demographics = {
            'population': 125921755, 'density': 333.2, 'migration_rate': 0.08,
            'birth_rate': 5.7,
            'immigration': {
                'total_foreigners': 3768977,
                'source_countries': [("China", 873286), ("Vietnam", 634361), ("South Korea", 409238), ("Nepal", 124356), ("Brazil", 206886)],
                'immigration_rate': 10.5
            }
        }

class PrefectureTab:
    # (No changes needed in PrefectureTab class structure itself for these new features)
    # ... (Keep PrefectureTab class as defined in the previous step) ...
    """A container for prefecture data tab in the notebook"""
    def __init__(self, parent, prefecture_data):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.prefecture_data = prefecture_data # Now expects data including GDP and GDP per capita
        self.setup_ui()

    def setup_ui(self):
        # Setup sorter and filters at the top
        sort_frame = tk.Frame(self.frame, bg="#f0f0f8")
        sort_frame.pack(fill=tk.X, pady=5)

        tk.Label(sort_frame, text="Sort by:", bg="#f0f0f8").pack(side=tk.LEFT, padx=5)
        # ** MODIFIED: Added Growth Rate **
        sort_options = ["Prefecture Name", "Population", "Economy", "Approval Rating", "Unemployment Rate",
                        "GDP (B USD)", "GDP per Capita (USD)", "Pop. Growth (%)"] # Added Growth Rate
        self.sort_var = tk.StringVar(value=sort_options[0])
        sort_menu = ttk.Combobox(sort_frame, textvariable=self.sort_var, values=sort_options, width=20)
        sort_menu.pack(side=tk.LEFT, padx=5)

        self.sort_asc_var = tk.BooleanVar(value=True)
        asc_radio = tk.Radiobutton(sort_frame, text="Ascending", variable=self.sort_asc_var, value=True, bg="#f0f0f8")
        desc_radio = tk.Radiobutton(sort_frame, text="Descending", variable=self.sort_asc_var, value=False, bg="#f0f0f8")
        asc_radio.pack(side=tk.LEFT, padx=5)
        desc_radio.pack(side=tk.LEFT, padx=5)

        search_frame = tk.Frame(sort_frame, bg="#f0f0f8")
        search_frame.pack(side=tk.RIGHT, padx=10)

        tk.Label(search_frame, text="Search:", bg="#f0f0f8").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame, width=15)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        # Setup treeview with scrollbars
        tree_frame = tk.Frame(self.frame)
        tree

DEFAULT_PM_NAME = 'Shigeru Ishiba'
DEFAULT_PARTY_NAME = 'Liberal Democratic Party'

