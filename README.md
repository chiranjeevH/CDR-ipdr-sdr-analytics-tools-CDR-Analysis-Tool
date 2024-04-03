# DataFlow Master: A Python Solution for Bulk Data Processing and SQL Storage

## Project Overview
This Python project is designed to process data from CSV files, making it suitable for a wide range of applications beyond just network traffic analysis. The project offers two UI options:

Single CSV Search: Allows users to search using a single CSV file containing records of interest.

Bulk Search (ZIP): Enables users to perform bulk searches by providing a ZIP archive containing multiple CSV files with records.

The project reads data from CSV files, performs data processing and analysis, and stores the results in a Microsoft SQL Server database using pyodbc.

## Features
Data Reading: Utilizes the csv library to read data from CSV files. Additionally, it can handle ZIP files containing multiple CSV files for batch processing.

Data Processing: After reading the data, the project performs processing to clean, manipulate, and analyze the records. The specific steps, including data extraction and transformation, are carried out to structure the data appropriately.

Database Integration: The processed data is stored in a Microsoft SQL Server database using the pyodbc library. This ensures that the data is persistently saved and can be accessed for further analysis or reporting.

## Usage
Prepare your data in CSV format. For multiple CSV files, you can compile them into a ZIP file.

Place the CSV or ZIP file in the project directory.

Open the Python script (e.g., data_processing.py) and specify the file name and path in the appropriate variables.

Configure the database connection details in the pyodbc.connect method within the Python script. Provide server name, database name, username, and password to establish a connection.

Run the Python script to start processing the data.

## Code Explanation
The provided Python script processes data from CSV files within the ZIP archive, utilizing the os, zipfile, csv, and pyodbc libraries. Key parts of the code include:

Walking through the project directory to find any ZIP files, extracting their contents to a temporary folder using the zipfile.ZipFile class.

Iterating through the CSV files within the temporary folder and reading each row of data with csv.reader.

Organizing the data into a dictionary dict_data.

Establishing a connection to the Microsoft SQL Server database with pyodbc.connect, using connection parameters according to your setup.

Inserting the processed data into the SQL Server database with cursor.execute and committing the changes with conn.commit().

## Contribution
Contributions to this project are welcome. Open issues or submit pull requests with your feedback and suggestions to enhance the functionality and efficiency of the data processing tool.
