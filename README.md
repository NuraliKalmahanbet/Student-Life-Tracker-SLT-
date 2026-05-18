# Student Activity Tracker

A lightweight, object-oriented Python console application designed to help students log, track, and manage their daily activities, including academic tasks and sports exercises. This project features full data persistence, custom decorators, input validation, and duplicate prevention.

---

## Core Features

* **Object-Oriented Architecture:** Built using robust OOP principles including inheritance, polymorphism, and encapsulation.
* **Data Persistence (File I/O):** All activities are automatically saved to and loaded from a structured `data.json` file.
* **Custom Decorators:** Implements advanced Python decorators for clean, centralized execution logging and status auditing.
* **Data Validation and Integrity:** Automatic duplicate checking (case-insensitive) to prevent repetitive logging, and strict exception handling protecting the system against invalid user inputs.
* **Unique Identification:** Generates a short, unique identifier (UUID) for each registered activity to ensure clean tracking.

---

## Tech Stack and Core Concepts Covered

* **Language:** Python 3.x
* **Data Structures:** Lists, Dictionaries, JSON Objects
* **Modules Used:** `json` (for file persistence), `uuid` (for unique ID generation)
* **OOP Concepts:** Base class (`Activity`), Subclasses (`StudyTask`, `Exercise`), method overriding, and inheritance initialization via `super()`.

---

## Project Structure

    ├── main.py          # Main application file containing classes, logic, and CLI menu
    ├── data.json        # Persistent JSON storage file (Auto-generated upon first run)
    └── README.md        # Project documentation and guidelines

---

## Installation and Usage

### Prerequisites
Make sure you have Python installed on your local machine.

### Running the Application
1. Clone this repository or download the source code.
2. Open your terminal/command prompt in the project directory.
3. Execute the script using:
   `python main.py`

### Application Menu Guide
* **Option 1:** View full historical records loaded directly from the JSON database.
* **Option 2:** Add a study assignment by specifying its name and submission deadline.
* **Option 3:** Add an exercise session by entering duration (minutes) and calorie expenditure.
* **Option 4:** Safely exit the tracker environment.

---

## Demonstration and Validation Showcase

The application includes rigorous layers to maintain data health:
* **Duplicate Safeguard:** Attempting to log "Calculus 2 Assignment" twice will safely cancel the second registration and output an inline warning.
* **Type Error Resilience:** Entering strings like "forty" instead of integers inside the exercise field will throw a clear validation error without triggering a fatal application crash.