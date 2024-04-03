# DataFlow Master: A Python Solution for Bulk Data Processing and SQL Storage

## Project Overview

This Python project is designed to process data from CSV files, suitable for a wide range of applications. It offers two UI options:

- **Single CSV Search**: Search using a single CSV file.
- **Bulk Search (ZIP)**: Perform searches with a ZIP archive containing multiple CSV files.

Data is read from CSV files, processed, analyzed, and stored in a Microsoft SQL Server database using pyodbc.

## Features

- **Data Reading**: Uses the `csv` library for CSV file reading and supports ZIP files for batch processing.
- **Data Processing**: Cleans, manipulates, and analyzes records, structuring data appropriately.
- **Database Integration**: Stores processed data in a Microsoft SQL Server database with `pyodbc`, ensuring persistent storage and access.

## Usage

1. Prepare data in CSV format. For multiple files, compile them into a ZIP file.
2. Place the CSV or ZIP file in the project directory.
3. Open the Python script (e.g., `data_processing.py`) and specify the file name and path.
4. Configure the database connection in `pyodbc.connect` with your server name, database name, username, and password.
5. Run the script to begin data processing.

## Code Explanation

Utilizing `os`, `zipfile`, `csv`, and `pyodbc` libraries, the script processes data from CSV files in a ZIP archive:

- Finds ZIP files in the directory, extracting them with `zipfile.ZipFile`.
- Iterates through CSV files in the temporary folder, reading data with `csv.reader`.
- Processes and organizes data into `dict_data`.
- Connects to Microsoft SQL Server with `pyodbc.connect` (parameters according to setup).
- Inserts processed data into the database with `cursor.execute` and commits with `conn.commit()`.

## Contribution

Feel free to contribute by opening issues or submitting pull requests. Your feedback and suggestions are valuable for enhancing the tool's functionality and efficiency.
