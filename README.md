# Slot Machine

A Python-based terminal slot machine engine built for prototyping RNG and payout logic.

## Overview

This repository implements a lightweight slot machine simulation with a 3x3 reel matrix and configurable symbol distribution. The code demonstrates:

- procedural game flow
- configurable betting constraints
- pseudo-random symbol generation using `random.choice`
- line-based payout detection
- simple state management for player balance

## Architecture

`main.py` contains the full runtime:

- `deposit()` — validates user deposit input
- `get_numnber_of_lines()` — enforces line selection bounds
- `get_bet()` — validates per-line betting amount
- `get_slot_machine_spin(rows, cols, symbols)` — constructs reels from weighted symbol pools
- `check_winnings(columns, lines, bet, values)` — evaluates matching symbols by line and calculates payout
- `print_slot_machine(columns)` — renders the reel matrix in the terminal
- `spin(balance)` — orchestrates one spin cycle and returns net balance delta
- `main()` — game loop with balance persistence and quit control

## Data model

- `symbol_count`: `dict[str, int]` defining reel frequency for each symbol
- `columns`: `list[list[str]]` representing vertical reels
- `winnings_lines`: `list[int]` storing line indices that hit
- `balance`: player bank roll updated after each spin

## Execution

Prerequisites:

- Python 3.10+

To run:

```powershell
cd C:\Users\amer\Slot_Machine
python main.py
```

## Runtime behavior

1. Deposit funds
2. Choose lines to wager on (1-3)
3. Place a per-line bet within configured min/max bounds
4. Generate a random reel set from the weighted symbol pool
5. Evaluate each active row for matching symbols across all columns
6. Print payout and update the player balance

## Developer notes

- The current RNG uses Python's standard `random` module; swap to `secrets` or `numpy` for stronger randomness.
- The reel generation algorithm copies the symbol pool (`all_symbols[:]`) per column and removes chosen symbols to avoid duplicates within a column.
- `check_winnings()` uses a short-circuit loop to skip payout when any column symbol on a line differs from the first column.
- The code is intentionally simple, making it easy to extend with features such as:
  - dynamic reel count
  - scatter symbols
  - multi-line pay tables
  - session persistence
  - unit tests for deterministic payout validation

## File summary

- `main.py` — game engine and terminal UI
- `README.md` — project documentation
