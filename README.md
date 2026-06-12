# Task 2: Unbeatable Tic-Tac-Toe AI

An interactive, terminal-based Tic-Tac-Toe game powered by an unbeatable artificial intelligence opponent. This project leverages decision tree evaluation structures to map out optimal tactical gameplay.

## 🧠 Core Game Logic
- **Adversarial Search Matrix:** Uses the Minimax algorithm to dynamically scan every available future state permutation.
- **Alpha-Beta Pruning Efficiency:** Implements constraint bounds ($\alpha$ and $\beta$) to eliminate unnecessary branches, cutting down computational path exploration overhead.
- **Heuristic Depth Adjustments:** Incorporates an active depth penalty factor to drive the AI to intercept human traps instantly or force quick checkmates.

## 🛠️ Architecture & Requirements
- **Language Stack:** Python 3.x
- **Dependency Packages:** Zero external packages required (Uses standard modules `math` and `sys`).

## 💻 Running the Execution Build
1. Open your native terminal window.
2. Initialize execution with the following command:
   ```bash
   python tictactoe_ai.py
