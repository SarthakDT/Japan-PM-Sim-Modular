import random
import datetime

class Prefecture:
    def __init__(self, name, population=None, gdp=None, growth_rate=None):
        self.name = name
        self.population = float(population) if population is not None else float(random.randint(500000, 10000000))
        self.gdp = float(gdp) if gdp is not None else random.uniform(20.0, 100.0)
        self.economy = random.uniform(0.5, 1.5)
        self.approval = random.uniform(40.0, 60.0)
        self.unemployment = random.uniform(3.0, 10.0)
        self.population_growth_rate = float(growth_rate) if growth_rate is not None else random.uniform(-1.0, 0.5)

    def update_daily_population(self):
        """Compounded daily growth rate based on annual percentage."""
        daily_rate_multiplier = (1.0 + self.population_growth_rate / 100.0)**(1.0/365.0)
        self.population *= daily_rate_multiplier

    def normalize_values(self):
        self.approval = min(100.0, max(0.0, self.approval))
        self.unemployment = min(30.0, max(1.0, self.unemployment))
        self.economy = min(3.0, max(0.1, self.economy))
        self.gdp = max(1.0, self.gdp)
        self.population = max(1000.0, self.population)

    def get_gdp_per_capita(self):
        return (self.gdp * 1_000_000_000) / self.population if self.population > 0 else 0

    def get_population_int(self):
        return int(round(self.population))

class PrimeMinister:
    def __init__(self, name, party_name):
        self.name = name
        self.party_name = party_name
        self.global_approval = 50.0
        self.economy_skill = random.uniform(0.5, 1.5)
        self.unemployment_skill = random.uniform(0.5, 1.5)
        self.welfare_skill = random.uniform(0.5, 1.5)
        self.demographics_skill = random.uniform(0.5, 1.5)

    def calculate_global_approval(self, prefectures):
        total_weighted_approval = sum(p.approval * p.population for p in prefectures)
        total_pop = sum(p.population for p in prefectures)
        self.global_approval = total_weighted_approval / total_pop if total_pop > 0 else 0
        return self.global_approval

class RivalParty:
    def __init__(self, name):
        self.name = name
        self.attack_skill = random.uniform(0.8, 1.2)
        self.preferred_attack = random.choice(["economy", "scandal", "welfare", "competence"])

    def generate_attack(self):
        base_impact = random.uniform(0.5, 2.5) * self.attack_skill
        messages = {
            "economy": f"{self.name} slams the PM over rising inflation!",
            "scandal": f"{self.name} demands an inquiry into cabinet ethics.",
            "welfare": f"{self.name} claims the elderly are being abandoned.",
            "competence": f"{self.name} questions the PM's ability to lead."
        }
        return messages.get(self.preferred_attack, "Attack!"), base_impact