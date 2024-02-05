# NetworkFlow Master: A Python Solution for Bulk IPDR Processing and SQL Storage

# IPDR Python Project

## Overview
This Python project is designed to process IPDR (Internet Protocol Detail Record) data, commonly used for network traffic analysis. The project offers two UI options:

Single CSV Search: This option allows users to search using a single CSV file containing IPDR records.

Bulk Search (ZIP): This option enables users to perform bulk searches by providing a ZIP archive containing multiple CSV files with IPDR records.

The project reads IPDR data from CSV files, performs data processing and analysis, and stores the results in a Microsoft SQL Server database using pyodbc.
## Features

- **Data Reading**: The project utilizes the `csv` library to read IPDR data from a CSV file. Additionally, it can handle ZIP files containing multiple CSV files for batch processing.

- **Data Processing**: After reading the IPDR data, the project performs data processing to clean, manipulate, and analyze the records. The specific processing steps, including data extraction and transformation, are carried out to structure the data appropriately.

- **Database Integration**: The processed data is stored in a Microsoft SQL Server database using the `pyodbc` library. This ensures that the data is persistently saved and can be accessed for further analysis or reporting.


## Usage

1. Prepare your IPDR data in CSV format. If you have multiple CSV files, you can put them in a ZIP file.

2. Place the CSV or ZIP file in the project directory.

3. Open the Python script (e.g., `ipdr_processing.py`) and specify the file name and path in the appropriate variables.

4. Configure the database connection details in the `pyodbc.connect` method within the Python script. Provide the server name, database name, username, and password to establish a connection.

5. Run the Python script to start processing the IPDR data.

## Code Explanation

The provided Python script processes the IPDR data from CSV files within the ZIP archive. It uses the `os`, `zipfile`, `csv`, and `pyodbc` libraries to achieve this. The essential parts of the code are as follows:

- The script walks through the project directory and finds any ZIP files. For each ZIP file found, it extracts the contents to a temporary folder using the `zipfile.ZipFile` class.

- The script then iterates through the CSV files within the temporary folder and uses the `csv.reader` to read each row of data.

- The IPDR data is processed and organized into a dictionary `dict_data`.

- The `pyodbc.connect` method is used to establish a connection to the Microsoft SQL Server database. The connection parameters should be provided according to your setup.

- The processed data is inserted into the SQL Server database using the `cursor.execute` method and committed using `conn.commit()`.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and suggestions are valuable in improving the functionality and efficiency of the IPDR processing tool.
