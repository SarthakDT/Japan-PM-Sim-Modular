import datetime

PREFECTURE_NAMES = [
    "Hokkaido", "Aomori", "Iwate", "Miyagi", "Akita", "Yamagata", "Fukushima", "Ibaraki", "Tochigi", "Gunma",
    "Saitama", "Chiba", "Tokyo", "Kanagawa", "Niigata", "Toyama", "Ishikawa", "Fukui", "Yamanashi", "Nagano",
    "Gifu", "Shizuoka", "Aichi", "Mie", "Shiga", "Kyoto", "Osaka", "Hyogo", "Nara", "Wakayama", "Tottori",
    "Shimane", "Okayama", "Hiroshima", "Yamaguchi", "Tokushima", "Kagawa", "Ehime", "Kochi", "Fukuoka",
    "Saga", "Nagasaki", "Kumamoto", "Oita", "Miyazaki", "Kagoshima", "Okinawa"
]

PREFECTURE_GDP_PLACEHOLDERS = {
    "Tokyo": 1000, "Osaka": 400, "Aichi": 380, "Kanagawa": 350, "Saitama": 230, "Chiba": 210, "Hyogo": 200,
    "Fukuoka": 190, "Hokkaido": 180, "Shizuoka": 170, "Ibaraki": 130, "Hiroshima": 120, "Kyoto": 110,
    "Niigata": 100, "Miyagi": 95, "Gunma": 90, "Tochigi": 88, "Okayama": 85, "Gifu": 80, "Nagano": 78,
    "Mie": 75, "Fukushima": 70, "Shiga": 68, "Yamaguchi": 65, "Kumamoto": 60, "Ehime": 58, "Kagoshima": 55,
    "Toyama": 53, "Ishikawa": 52, "Wakayama": 50, "Oita": 48, "Yamagata": 46, "Nagasaki": 45, "Yamanashi": 44,
    "Aomori": 43, "Iwate": 42, "Akita": 40, "Miyazaki": 38, "Fukui": 37, "Kagawa": 36, "Tokushima": 35,
    "Saga": 34, "Nara": 33, "Okinawa": 32, "Kochi": 30, "Shimane": 28, "Tottori": 25
}

PREFECTURE_GROWTH_RATES = {
    "Tokyo": 0.4, "Kanagawa": 0.1, "Saitama": 0.05, "Chiba": 0.0, "Aichi": 0.0, "Osaka": -0.1, "Fukuoka": 0.05,
    "Okinawa": 0.3, "Shiga": 0.0,
    "Hokkaido": -0.5, "Aomori": -1.0, "Iwate": -0.9, "Miyagi": -0.3, "Akita": -1.5, "Yamagata": -1.1, "Fukushima": -0.8,
    "Ibaraki": -0.4, "Tochigi": -0.5, "Gunma": -0.6, "Niigata": -0.9, "Toyama": -0.7, "Ishikawa": -0.6, "Fukui": -0.7,
    "Yamanashi": -0.6, "Nagano": -0.7, "Gifu": -0.5, "Shizuoka": -0.4, "Mie": -0.6, "Kyoto": -0.3, "Hyogo": -0.3,
    "Nara": -0.7, "Wakayama": -1.0, "Tottori": -0.9, "Shimane": -1.1, "Okayama": -0.3, "Hiroshima": -0.2, "Yamaguchi": -0.8,
    "Tokushima": -1.0, "Kagawa": -0.6, "Ehime": -0.9, "Kochi": -1.1, "Saga": -0.7, "Nagasaki": -1.0, "Kumamoto": -0.5,
    "Oita": -0.8, "Miyazaki": -0.9, "Kagoshima": -0.8
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

# Election-cycle constants
LAST_ELECTION_DATE = datetime.date(2026, 2, 8)
START_DATE = datetime.date(2026, 2, 9)
TERM_DURATION_DAYS = 1460

COALITION_SEATS_BASELINE = 352
DIET_TOTAL_SEATS = 465
MAJORITY_THRESHOLD = 233
SUPERMAJORITY_THRESHOLD = 310
BASELINE_APPROVAL_2026 = 55.0
