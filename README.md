# Black-Hole
# Project Black Hole — Disk Failure Simulation

## Overview

Project Black Hole is an educational Python project that simulates a disk corruption scenario and a hypothetical operating system failure.

The program demonstrates how to organize a system-level simulation using configuration objects, environment checks, progress reporting, logging, and exception handling.

**This project does not modify physical disks or cause a real system crash.**

## Features

- Operating system and Python version reporting
- Configurable simulated disk target
- Configurable block size and simulated operation size
- Progress updates during the simulation
- Timestamped logging
- Exception handling and process exit codes
- Simulated system failure reporting

## Requirements

- Python 3.10 or later
- No third-party dependencies

## Project Structure

```text
project-black-hole/
├── main.py
└── README.md
```

## Usage

Run the script from a terminal:

```bash
python main.py
```

The program displays the simulation configuration, reports progress, and prints a final status message.

## Configuration

The simulation parameters are defined in `SimulationConfig`:

- `drive`: A representative disk identifier used for display only.
- `buffer_size`: The simulated block size in bytes.
- `simulated_size_mb`: The total simulated operation size in megabytes.

Changing these parameters changes the simulation output only.

## Execution Flow

1. `check_environment()` reports the operating system and Python version.
2. `simulate_disk_write()` displays a simulated disk-writing progress sequence.
3. `simulate_system_failure()` reports a hypothetical system failure.
4. `main()` coordinates execution and handles errors.

## Safety Limitations

The application does not:

- Open physical disks for raw writing.
- Overwrite MBR, GPT, boot sectors, or filesystem metadata.
- Delete or overwrite user data.
- Trigger a Windows blue screen.
- Invoke privileged kernel operations.

The disk identifier is informational and is never opened.

## Educational Purpose

This project is intended for learning Python architecture, logging, progress reporting, configuration management, and safe simulations of operating system failure scenarios.

For defensive cybersecurity work, the simulation can be extended with unit tests and monitoring exercises using disposable virtual-machine environments.

## Disclaimer

This is a non-destructive simulation. It is not a disk-wiping utility, partition-table editor, or system-crashing tool.

