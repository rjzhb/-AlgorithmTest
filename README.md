# Python Project 3

## Project Overview

This project contains solutions for two problems along with their corresponding unit tests. The project structure is as follows:

pythonProject3/
│
├── problem1.py
├── problem2.py
├── run_tests.py
└── test/
    ├── test_problem1.py
    └── test_problem2.py
### Problem Descriptions

#### Problem 1: Shortest Way to Form String
Given two strings `source` and `target`, return the minimum number of subsequences of `source` such that their concatenation equals `target`. If the task is impossible, return -1.

**Examples:**
- `source = "abc"`, `target = "abcbc"`, Output: 2
- `source = "abc"`, `target = "acdbc"`, Output: -1
- `source = "xyz"`, `target = "xzyxz"`, Output: 3

#### Problem 2: Check Parentheses
Given a list of strings containing parentheses, check if the parentheses are balanced. If there are unmatched left parentheses, mark them with `x`; if there are unmatched right parentheses, mark them with `?`.

**Example Input:**

"bge)))))))))" 
"((IIII))))))" 
"()()()()(uuu" 
"))))UUUU((()" 

**Example Output:**
" ?????????" 
" ????" 
" x " 
"???? xx " 

## Files Description

- `problem1.py` - Contains the solution for Problem 1.
- `problem2.py` - Contains the solution for Problem 2.
- `run_tests.py` - Script to run all tests at once.
- `test/test_problem1.py` - Unit tests for Problem 1.
- `test/test_problem2.py` - Unit tests for Problem 2.

## Usage Instructions

### Running Tests

To run all tests, execute the following command in the project's root directory:

```sh
python run_tests.py
