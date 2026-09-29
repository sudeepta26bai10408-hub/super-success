# Student Performance Analyzer

## 1. Project Overview

The **Student Performance Analyzer** is a Python-based project for managing and analyzing student marks. It calculates individual averages, class statistics, top-performing students, subject-wise averages, and performance graphs. It can also save the final report as a CSV file.

## 2. Features

- Store student marks for Python, Maths, and Physics
- Validate marks
- Calculate individual averages
- Display student records
- Generate a class performance summary
- Display the top 5 students
- Calculate subject-wise averages
- Generate performance graphs using Matplotlib
- Export the report to CSV
- Menu-driven interface

## 3. Requirements

You need:

- Python 3.8 or later
- Matplotlib

The `csv` and `os` modules are included with Python and require no separate installation.

## 4. Project Structure

```text
Student Performance Analyzer/
├── main.py
├── README.md
└── output/
    └── student_report.csv
```

The `output` folder and CSV file are created automatically when the CSV export option is used.

## 5. Environment Setup

### Step 1: Install Python

Install Python 3 from the official Python website.

On Windows, select **Add Python to PATH** during installation.

Verify the installation:

```bash
python --version
```

If `python` does not work on Windows, try:

```bash
py --version
```

### Step 2: Open the Project Folder

Place `main.py` and `README.md` in the same folder.

Example:

```text
Student Performance Analyzer/
    main.py
    README.md
```

Open Command Prompt or Terminal in this folder.

## 6. Dependency Installation

Install Matplotlib with:

```bash
python -m pip install matplotlib
```

On Windows, you can also use:

```bash
py -m pip install matplotlib
```

Verify the installation:

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
```

## 7. Configuration

No database, API key, password, or external configuration file is required.

The sample student data is stored in `main.py`.

The project uses these subjects:

- Python
- Maths
- Physics

Marks should be between **0 and 100**.

To use different students or marks, edit the `students` list in `main.py`.

## 8. Running the Project

Run:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The program displays this menu:

```text
1. Display Student Records
2. View Class Summary
3. Show Top 5 Students
4. Show Subject Averages
5. Student Performance Graph
6. Subject Average Graph
7. Save Report to CSV
8. Exit
```

Enter a number from 1 to 8 and press Enter.

## 9. Menu Options

### 1. Display Student Records

Shows each student's roll number, name, marks, and average.

### 2. View Class Summary

Shows:

- Number of students
- Class average
- Highest performer
- Lowest performer
- Number of students passed
- Number of students failed

The current program considers an average of **40% or above** as passing.

### 3. Show Top 5 Students

Sorts students by average marks and displays the five highest averages.

### 4. Show Subject Averages

Calculates the class average for Python, Maths, and Physics.

### 5. Student Performance Graph

Displays a Matplotlib bar graph of students' average marks.

### 6. Subject Average Graph

Displays a Matplotlib bar graph comparing subject averages.

### 7. Save Report to CSV

Creates:

```text
output/student_report.csv
```

The CSV contains:

```text
RollNo, Name, Python, Maths, Physics, Average
```

### 8. Exit

Closes the application.

## 10. Example Execution

```text
============================================================
STUDENT PERFORMANCE ANALYZER
============================================================

1. Display Student Records
2. View Class Summary
3. Show Top 5 Students
4. Show Subject Averages
5. Student Performance Graph
6. Subject Average Graph
7. Save Report to CSV
8. Exit

Enter your choice:
```

For example, entering `2` displays the class summary.

## 11. Troubleshooting

### `ModuleNotFoundError: No module named 'matplotlib'`

Run:

```bash
python -m pip install matplotlib
```

Then run the project again.

### `python is not recognized`

Try:

```bash
py main.py
```

If that does not work, reinstall Python and enable **Add Python to PATH**.

### Graph does not appear

Run the project on a computer environment that supports Matplotlib graphical windows. Some online Python compilers do not support `plt.show()` correctly.

### Program closes immediately

Run the program from Command Prompt or Terminal instead of double-clicking `main.py`. This lets you see the output and any error messages.

## 12. Technologies Used

- **Python 3** — programming language
- **CSV** — report storage
- **Matplotlib** — data visualization
- **Command-line interface** — user interaction

## 13. Project Output

The project produces:

1. Student performance records
2. Individual average marks
3. Class statistics
4. Top 5 student list
5. Subject-wise averages
6. Student performance graph
7. Subject average graph
8. CSV performance report

## 14. Author

**Student Performance Analyzer Project**

An academic Python project demonstrating data management, calculations, file handling, and data visualization.
