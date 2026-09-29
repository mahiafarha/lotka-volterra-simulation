# Lotka-Volterra Nonlinear Dynamical Simulation Engine

A computational engine modeled in Python to simulate discrete-time Lotka-Volterra predator-prey dynamics, evaluate parametric survival thresholds, and calculate non-trivial steady-state equilibria.

## Mathematical Formulation

The system updates iteratively across discrete time-steps according to coupled difference equations:

$$\text{Prey}(t+1) = \text{Prey}(t) + \alpha \cdot \text{Prey}(t) - \beta \cdot \text{Prey}(t) \cdot \text{Predator}(t)$$

$$\text{Predator}(t+1) = \text{Predator}(t) + \delta \cdot \text{Prey}(t) \cdot \text{Predator}(t) - \gamma \cdot \text{Predator}(t)$$

Where:
- $\alpha$: Prey intrinsic reproduction rate
- $\beta$: Predation mortality coefficient
- $\delta$: Predator conversion efficiency per prey consumed
- $\gamma$: Predator natural mortality rate

Boundary conditions enforce non-negative populations: $\text{Prey}(t) \ge 0, \text{Predator}(t) \ge 0$.

## Features

- **Trajectory Modeling:** Simulates multi-period population interactions with automated zero-boundary termination.
- **Equilibrium Identification:** Algorithmic grid search to identify fixed-point steady-states where $\Delta N = 0$ and $\Delta P = 0$.
- **Parametric Longevity Optimization:** Evaluates initial predator density permutations to maximize prey survival over constrained temporal horizons.
- **Automated Visualization:** Generates publication-ready time-series plots using Matplotlib.

## Installation & Usage

### 1. Clone Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/lotka-volterra-simulation.git
cd lotka-volterra-simulation