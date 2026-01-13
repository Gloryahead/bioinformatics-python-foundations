# Bioinformatics Python Foundations

This repository documents my progression toward writing clean,
reproducible Python command-line tools for scientific and
bioinformatics workflows.

## Day 01 – Hello CLI
**Focus:** CLI structure, argument parsing, and clean entry points.

**Skills demonstrated:**
- argparse
- function isolation
- __main__ entry point

**Usage:**
```bash
python src/day01_hello_cli/main.py --name Michael
```

## Day 02 – Input Validation
**Focus:** Safe user input and defensive programming.

**Usage:**
```bash
python src/day02_input_validation/tip_calculator.py
```

## Day 03 – File I/O
**Focus:** Persistent storage and safe file reading/writing.

**Skills demonstrated:**
- `pathlib.Path` for reliable file paths
- append vs read modes (`"a"` / `"r"`)
- graceful handling of missing/empty files
- separating I/O from program flow

**Usage:**
```bash
python src/day03_file_io/notes.py
```

## Day 04 – Data Structures
**Focus:** Dictionary-based structured data and controlled program flow.

**Usage:**
```bash
python src/day04_data_structures/flashcards.py
```

