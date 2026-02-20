import tkinter as tk
from tkinter import messagebox

from constants import DIET_TOTAL_SEATS
from simulation import Simulation


class JapanPMSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Japan PM Simulator")
        self.simulation = Simulation()

        self.info_frame = tk.Frame(root, bg="#e1e1f0", padx=8, pady=8)
        self.info_frame.pack(fill=tk.X)

        self.date_label = tk.Label(self.info_frame, text="", font=("Arial", 11), bg="#e1e1f0")
        self.date_label.grid(row=0, column=0, sticky="w")

        self.approval_label = tk.Label(self.info_frame, text="", font=("Arial", 11), bg="#e1e1f0")
        self.approval_label.grid(row=1, column=0, sticky="w")

        self.term_label = tk.Label(self.info_frame, text="", font=("Arial", 11), bg="#e1e1f0")
        self.term_label.grid(row=2, column=0, sticky="w")

        self.status_label = tk.Label(self.info_frame, text="", font=("Arial", 10), bg="#e1e1f0")
        self.status_label.grid(row=3, column=0, sticky="w")

        self.control_frame = tk.Frame(root, padx=8, pady=8)
        self.control_frame.pack(fill=tk.X)

        self.advance_btn = tk.Button(self.control_frame, text="Advance 1 Day", command=self.advance_day)
        self.advance_btn.grid(row=0, column=0, padx=3, pady=3)

        self.policy_btn = tk.Button(self.control_frame, text="Pass Welfare Policy", command=self.run_policy)
        self.policy_btn.grid(row=0, column=1, padx=3, pady=3)

        self.dissolve_btn = tk.Button(
            self.control_frame,
            text="Dissolve House of Representatives 🏛️",
            command=self.manual_dissolution,
            bg="#f44336",
            fg="white",
        )
        self.dissolve_btn.grid(row=0, column=2, padx=3, pady=3)

        self.events_box = tk.Text(root, height=12, width=90, state=tk.DISABLED)
        self.events_box.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.update_display()

    def append_event(self, text):
        self.events_box.config(state=tk.NORMAL)
        self.events_box.insert(tk.END, f"{text}\n")
        self.events_box.see(tk.END)
        self.events_box.config(state=tk.DISABLED)

    def advance_day(self):
        previous_events = len(self.simulation.events)
        self.simulation.advance_day()
        for event in self.simulation.events[previous_events:]:
            self.append_event(event)
        self.update_display()

    def run_policy(self):
        previous_events = len(self.simulation.events)
        self.simulation.make_policy("welfare")
        for event in self.simulation.events[previous_events:]:
            self.append_event(event)
        self.update_display()

    def update_display(self):
        sim = self.simulation
        self.date_label.config(text=f"Date: {sim.current_date.isoformat()}")

        seat_status = f"Seats: {sim.seats}/{DIET_TOTAL_SEATS}"
        self.approval_label.config(text=f"Approval: {sim.pm.global_approval:.2f}% | {seat_status}")

        days = sim.days_to_term_end
        self.term_label.config(text=f"Days Remaining in Term: {days}")

        if not sim.running:
            status = f"GAME OVER — {sim.game_over_reason}"
            self.advance_btn.config(state=tk.DISABLED)
            self.policy_btn.config(state=tk.DISABLED)
            self.dissolve_btn.config(state=tk.DISABLED)
        else:
            override = "Yes" if sim.override_power else "No"
            status = f"Override Power: {override}"
            self.dissolve_btn.config(state=tk.DISABLED if sim.election_in_progress else tk.NORMAL)

        self.status_label.config(text=status)

    def manual_dissolution(self):
        if not self.simulation.running:
            return

        if messagebox.askyesno("Dissolve Diet", "Dissolve the House and call a snap election?"):
            previous_events = len(self.simulation.events)
            self.simulation.dissolve_diet()
            for event in self.simulation.events[previous_events:]:
                self.append_event(event)
            self.update_display()


def run_app():
    root = tk.Tk()
    JapanPMSimulatorApp(root)
    root.mainloop()
