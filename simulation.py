import datetime
import random
from models import Prefecture, PrimeMinister, RivalParty
from constants import PREFECTURE_NAMES, PREFECTURE_POPULATIONS, PREFECTURE_GDP_PLACEHOLDERS, PREFECTURE_GROWTH_RATES

class Simulation:
    def __init__(self, pm_name="Shigeru Ishiba", party_name="LDP"):
        self.prefectures = [
            Prefecture(
                name, 
                population=PREFECTURE_POPULATIONS.get(name),
                gdp=PREFECTURE_GDP_PLACEHOLDERS.get(name),
                growth_rate=PREFECTURE_GROWTH_RATES.get(name)
            ) for name in PREFECTURE_NAMES
        ]
        self.pm = PrimeMinister(pm_name, party_name)
        self.current_date = datetime.date(2025, 1, 1)
        self.running = True
        self.election_in_progress = None
        self.events = []
        self.approval_history = []
        self.approval_dates = []
        self.rivals = [RivalParty(n) for n in ["CDP", "DPP", "Ishin"]]
        self.update_history()

    def update_history(self):
        self.pm.calculate_global_approval(self.prefectures)
        self.approval_history.append(self.pm.global_approval)
        self.approval_dates.append(self.current_date)

    def advance_day(self):
        if not self.running: return
        
        # Date Logic Fix: Use timedelta to avoid manual month/day math errors
        self.current_date += datetime.timedelta(days=1)
        
        for p in self.prefectures:
            p.update_daily_population()
            p.approval += random.uniform(-0.1, 0.1)
            p.normalize_values()
            
        if self.pm.calculate_global_approval(self.prefectures) < 30.0:
            self.trigger_election()
            
        self.update_history()

    def trigger_election(self):
        self.election_in_progress = "triggered"
        self.events.append("Election Triggered: Approval below 30%!")

    def make_policy(self, policy_type):
        # Implementation of policy impacts...
        self.events.append(f"Implemented {policy_type} policy.")
        self.advance_day()