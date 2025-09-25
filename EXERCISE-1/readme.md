# Safety Inspection Checklist

This project implements a basic Safety Inspection Checklist using Python. It demonstrates how to work with core Python data types and control structures in the context of a practical safety inspection scenario.

---

## Project Overview

The script simulates a safety inspection process for a facility or workplace. It analyzes inspection scores, manages a checklist of safety items, processes structured data using dictionaries, and performs various computations to evaluate compliance with safety standards.

---

## Features and Structure

### 1. Integers
- A list of inspection scores is stored.
- Calculates the total, average, minimum, and maximum scores.

### 2. Strings
- Uses formatted strings (`f-strings`) to generate a structured summary report of the inspection results.

### 3. Booleans
- Evaluates whether the average inspection score exceeds a threshold.
- Uses a compound condition to determine if the inspection status is "Above Standard" or "Below Standard".

### 4. Lists
- Maintains a checklist of safety items (e.g., fire extinguishers, emergency exits).
- Adds a new item (`"Safety Signage"`).
- Removes an item (`"First Aid Kit"`) if it exists.
- Sorts and displays the checklist before and after modification.

### 5. Arrays
- Uses Python’s `array` module to store a fixed-size subset of inspection scores.
- Compares the sum of values in the array with the sum of the same values in a list.

### 6. Dictionaries
- Stores inspection records as a list of dictionaries, each containing an `id`, `name`, and `value`.
- Updates the score for a specific item.
- Deletes a record based on its `id`.
- Calculates the total score from all remaining records.

---

