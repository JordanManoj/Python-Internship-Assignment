# AI-Python-Internship-Assignment

This repository contains Python solutions to four programming exercises completed as part of an AI/Data Science internship assignment. Each task demonstrates fundamental Python skills such as date/time operations, number theory, file handling, NumPy processing, and REST API integration.

---

## Assignment Overview

The assignment includes the following exercises:

1. **Age Calculator**
2. **Prime Number Generator**
3. **Student Marks Processor**
4. **Weather Data Fetcher & Analyzer**

Each program includes proper error handling and is well-commented for clarity.

---

---

## Exercise Details

### Exercise 1: Age Calculator

**Functionality:**

- Accepts a birth date from the user in `mm/dd/yyyy` format.
- Validates the input format.
- Calculates and displays current age.
- Converts the input to European format (`dd/mm/yyyy`).
- Handles invalid inputs with clear error messages.

---

### Exercise 2: Prime Number Generator

**Functionality:**

- Takes two positive integers (range start and end).
- Validates that the inputs are positive.
- Generates all prime numbers within the given range.
- Displays the primes, formatted to 10 numbers per line.
- Gracefully handles invalid input.


---

### Exercise 3: Student Marks Processor

**Functionality:**

- Reads student data from `student_marks.txt` (format: RegNo, ExamMark, CourseworkMark).
- Calculates the overall mark using:
- - Overall = 0.7 * ExamMark + 0.3 * CourseworkMark
- Assigns grades based on overall mark:
  - A: 90–100
  - B: 75–89
  - C: 60–74
  - D: 50–59
  - F: below 50
- Stores data in a structured NumPy array.
- Sorts students by overall mark (descending).
- Writes the results to `final_report.txt`.
- Displays grade statistics.

**Input (`students_sampledata.txt`):**


---

### Exercise 4: Weather Data Fetcher & Analyzer

**Functionality:**

- Fetches real-time weather data for a given city using the OpenWeatherMap API.
- Analyzes:
  - Temperature → Cold (≤10°C), Mild (11–24°C), Hot (≥25°C)
  - Alerts → High wind (>10 m/s), Humid conditions (>80%)
- Logs the data into `weather_log.csv`.

**Steps to Use:**

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get your API key.
2. Replace the provided api key in the script with your actual API key.







