# CSV_to_JSON_Converter

A simple and user-friendly Python script to convert CSV files into JSON format. This tool is designed for anyone who frequently works with structured data transformations. The script supports dynamic input/output paths and provides helpful error messages to ensure smooth usage.

---

## **Features:**
  - Converts CSV files to JSON format.
  - Prompts users to input custom paths for both the CSV and JSON files.
  - Validates file extensions and provides clear error messages.
  - Outputs JSON in a structured and readable format (indented).

---

## **Requirements:**
  - Python 3.6 or higher
  - `pandas` library

---

## **Installation:**

  1. Clone the repository:
     ```bash
     git clone https://github.com/JderenthalCS/CSV_to_JSON_converter.git
     ```

  2. Navigate to the project directory:
     ```bash
     cd CSV_to_JSON_converter
     ```
  
  3. Install required dependency (`pandas`):
     ```bash
     pip install pandas
     ```

---

## **Usage:**

  1. Run the script:
     ```bash
     python csv_to_json.py
     ```
     
  2. Enter the path to the CSV file when prompted:
     ```
     Enter the path to the CSV file: C:/path/to/your/file.csv
     ```
     
  3. Enter the path where the JSON file should be saved:
     ```
     Enter the desired path for the JSON file: C:/path/to/output/file.json
     ```

  4. If successful, the script will output:
     ```plaintext
     Reading CSV file...
     Converting CSV to JSON...
     JSON file has been saved as C:/path/to/output/file.json
     ```

---

## **Contribution:**
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.



  

