import pandas as pd

# Prompts the user to enter CSV file path
csv_file = input("Enter the path to the CSV file: ").strip().strip('"') # Example: C:/path/to/your/file.csv

# Prompts the user to enter desired JSON file output
json_file = input("Enter the desired path for the JSON file: ").strip().strip('"')   # Example: C:/path/to/your/output.json

# Ensure the JSON file path includes a file name
if not json_file.endswith(".json"):
    print("Error: Please include a filename and '.json' extension in the output path.")
else: 
    try: 
        # Read the CSV file into pandas DataFrame
        print("Reading CSV file...")
        data = pd.read_csv(csv_file)

        # Convert the DataFrame to JSON format
        print("Converting CSV to JSON...")
        data.to_json(json_file, orient="records", indent=4)
        
        # Confirmation Message
        print(f"JSON file has been saves as {json_file}")

    except FileNotFoundError:
        # Catch cases where CSV_file does not exist
        print(f"Error: The CSV file at '{csv_file}' was not found. Please check the path.")
        
    except Exception as e:
        # Catch and Print any other errors
        print(f"An unexpected error occurred: {e}")
        
