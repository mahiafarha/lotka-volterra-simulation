"""
Lotka-Volterra Predator-Prey Dynamical Simulation Engine
Models discrete nonlinear population dynamics, equilibrium points, and survival thresholds.
"""

from dataclasses import dataclass
from typing import List, Tuple
import matplotlib.pyplot as plt


@dataclass
class ModelParameters:
    alpha: float = 0.2    # Prey birth rate
    beta: float = 0.005   # Predation death rate
    delta: float = 0.001  # Predator reproduction rate per prey consumed
    gamma: float = 0.2    # Predator mortality rate


class PopulationSimulator:
    def __init__(self, params: ModelParameters):
        self.params = params

    def step(self, prey: float, pred: float) -> Tuple[float, float]:
        """Calculates single-step population updates with non-negative constraints."""
        new_prey = prey + (self.params.alpha * prey) - (self.params.beta * prey * pred)
        new_pred = pred + (self.params.delta * prey * pred) - (self.params.gamma * pred)
        return max(0.0, new_prey), max(0.0, new_pred)

    def simulate(self, initial_prey: int, initial_pred: int, max_steps: int) -> Tuple[List[int], List[int], List[int]]:
        """Simulates population counts over a sequence of discrete time steps."""
        time_history = [0]
        prey_history = [initial_prey]
        pred_history = [initial_pred]

        prey, pred = float(initial_prey), float(initial_pred)
        for t in range(1, max_steps + 1):
            prey, pred = self.step(prey, pred)
            if prey == 0 or pred == 0:
                break
            time_history.append(t)
            prey_history.append(round(prey))
            pred_history.append(round(pred))

        return time_history, prey_history, pred_history

    def find_max_survival_predators(self, prey_initial: int = 200, max_search: int = 1000, horizon: int = 200) -> Tuple[int, int]:
        """Finds initial predator count that maximizes prey longevity under fixed horizon."""
        best_pred = 1
        max_longevity = 0

        for pred_init in range(1, max_search + 1):
            t = 0
            prey, pred = float(prey_initial), float(pred_init)
            while round(prey) > 0 and round(pred) > 0 and t < horizon:
                t += 1
                prey, pred = self.step(prey, pred)

            if t > max_longevity:
                max_longevity = t
                best_pred = pred_init

        return best_pred, max_longevity

    def find_steady_state_equilibrium(self, max_prey: int = 500, max_pred: int = 500) -> Tuple[int, int]:
        """Identifies non-trivial steady state where populations remain constant year-over-year."""
        for p_init in range(1, max_pred + 1):
            for n_init in range(1, max_prey + 1):
                next_n, next_p = self.step(n_init, p_init)
                if round(next_n) == n_init and round(next_p) == p_init:
                    return n_init, p_init
        return None, None


def plot_trajectories(time: List[int], prey: List[int], pred: List[int]):
    """Plots and displays temporal population curves."""
    plt.figure(figsize=(9, 5))
    plt.plot(time, prey, label="Prey (Badgers)", color="#1f77b4", marker="o", markersize=4)
    plt.plot(time, pred, label="Predator (Dachshunds)", color="#ff7f0e", marker="s", markersize=4)
    plt.xlabel("Time (Discrete Steps)")
    plt.ylabel("Population Count")
    plt.title("Discrete-Time Lotka-Volterra Population Trajectories")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("population_dynamics.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    params = ModelParameters()
    simulator = PopulationSimulator(params)

    # 1. Run standard simulation
    time_hist, prey_hist, pred_hist = simulator.simulate(initial_prey=500, initial_pred=1, max_steps=13)
    print("Simulation complete. Sample steps:")
    for t, n, p in zip(time_hist, prey_hist, pred_hist):
        print(f"t = {t:2d} | Prey: {n:4d} | Predator: {p:4d}")

    # 2. Find equilibrium point
    eq_prey, eq_pred = simulator.find_steady_state_equilibrium()
    print(f"\nNon-trivial Steady State Equilibrium: Prey = {eq_prey}, Predator = {eq_pred}")

    # 3. Find optimal predator density for 200 prey survival
    best_p, max_t = simulator.find_max_survival_predators(prey_initial=200, max_search=1000, horizon=200)
    print(f"Optimal Initial Predators: {best_p} (Prey survived {max_t} steps)")

    # 4. Save visualization plot
    plot_trajectories(time_hist, prey_hist, pred_hist)