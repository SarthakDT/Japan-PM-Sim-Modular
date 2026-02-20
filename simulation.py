import datetime
import random

from models import Prefecture, PrimeMinister, RivalParty
from constants import (
    PREFECTURE_NAMES,
    PREFECTURE_POPULATIONS,
    PREFECTURE_GDP_PLACEHOLDERS,
    PREFECTURE_GROWTH_RATES,
    LAST_ELECTION_DATE,
    START_DATE,
    TERM_DURATION_DAYS,
    COALITION_SEATS_BASELINE,
    DIET_TOTAL_SEATS,
    MAJORITY_THRESHOLD,
    SUPERMAJORITY_THRESHOLD,
    BASELINE_APPROVAL_2026,
)


class Simulation:
    def __init__(self, pm_name="Sanae Takaichi", party_name="LDP"):
        self.prefectures = [
            Prefecture(
                name,
                population=PREFECTURE_POPULATIONS.get(name),
                gdp=PREFECTURE_GDP_PLACEHOLDERS.get(name),
                growth_rate=PREFECTURE_GROWTH_RATES.get(name),
            )
            for name in PREFECTURE_NAMES
        ]
        self.pm = PrimeMinister(pm_name, party_name)
        self.current_date = START_DATE
        self.last_election_date = LAST_ELECTION_DATE
        self.days_to_term_end = TERM_DURATION_DAYS
        self.seats = COALITION_SEATS_BASELINE

        self.running = True
        self.election_in_progress = False
        self.override_power = True
        self.events = []
        self.approval_history = []
        self.approval_dates = []
        self.election_survival_message = ""
        self.game_over_reason = ""

        self.rivals = [RivalParty(n) for n in ["CDP", "DPP", "Ishin"]]
        self.last_event_type = None
        self.pending_election_reason = None
        self.desperation_penalty_armed = False

        self.update_history()

    def get_days_until_next_election(self):
        term_end = self.last_election_date + datetime.timedelta(days=TERM_DURATION_DAYS)
        return (term_end - self.current_date).days

    def update_history(self):
        self.pm.calculate_global_approval(self.prefectures)
        self.approval_history.append(self.pm.global_approval)
        self.approval_dates.append(self.current_date)

    def advance_day(self):
        if not self.running:
            return

        self.current_date += datetime.timedelta(days=1)

        for prefecture in self.prefectures:
            prefecture.update_daily_population()
            prefecture.approval += random.uniform(-0.15, 0.15)
            prefecture.normalize_values()

        # small random event flavor
        self.last_event_type = None
        if random.random() < 0.03:
            self.last_event_type = "Scandal"
            for prefecture in self.prefectures:
                prefecture.approval -= random.uniform(0.2, 0.9)
                prefecture.normalize_values()
            self.events.append("Scandal event hit the cabinet narrative.")

        self.pm.calculate_global_approval(self.prefectures)
        self.days_to_term_end = self.get_days_until_next_election()

        if self.days_to_term_end <= 0 and not self.election_in_progress:
            self.trigger_election(reason="Term Expired")

        self.update_history()

    def trigger_election(self, reason="PM Dissolution", manual=False):
        if self.election_in_progress:
            return False

        self.election_in_progress = True
        self.pending_election_reason = reason

        # Desperation penalty if PM dissolves during scandal / weak approval
        self.desperation_penalty_armed = bool(
            manual and (self.last_event_type == "Scandal" or self.pm.global_approval < 40.0)
        )

        self.events.append(f"ELECTION CALL: {reason} by PM {self.pm.name}")
        self.handle_election_voting()
        return True

    def dissolve_diet(self):
        return self.trigger_election(reason="PM Dissolution", manual=True)

    def handle_election_voting(self):
        approval_swing = self.pm.global_approval - BASELINE_APPROVAL_2026
        seat_change = int(approval_swing * random.uniform(4, 6))

        if self.desperation_penalty_armed:
            penalty = random.randint(10, 20)
            seat_change -= penalty
            self.events.append(f"Desperation Penalty applied: -{penalty} seats")

        new_total = max(0, min(DIET_TOTAL_SEATS, COALITION_SEATS_BASELINE + seat_change))
        self.seats = new_total
        self.last_election_date = self.current_date
        self.days_to_term_end = self.get_days_until_next_election()
        self.election_in_progress = False
        self.desperation_penalty_armed = False

        self.override_power = self.seats >= SUPERMAJORITY_THRESHOLD

        if self.seats < MAJORITY_THRESHOLD:
            self.running = False
            self.game_over_reason = f"Lost Majority! Coalition fell to {self.seats} seats."
            self.events.append(self.game_over_reason)
            return

        status = "Supermajority Intact" if self.override_power else "Majority Secured"
        self.election_survival_message = f"Election Results: {self.seats}/{DIET_TOTAL_SEATS} seats. {status}."
        self.events.append(self.election_survival_message)

    def make_policy(self, policy_type):
        self.events.append(f"Implemented {policy_type} policy.")
        for prefecture in self.prefectures:
            if policy_type == "economy":
                prefecture.approval += random.uniform(-0.2, 0.5)
            elif policy_type == "welfare":
                prefecture.approval += random.uniform(-0.1, 0.4)
            else:
                prefecture.approval += random.uniform(-0.2, 0.2)
            prefecture.normalize_values()

        self.pm.calculate_global_approval(self.prefectures)
        self.advance_day()


def create_default_simulation():
    return Simulation()
