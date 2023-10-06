import csv
import random

# Function to insert data into the CSV file
def insert_data_into_csv(file_path, data):
    try:
        # Open the CSV file in 'append' mode with newline=''
        with open(file_path, mode='a', newline='') as csv_file:
            fieldnames = data[0].keys()  # Extract field names from the dictionary keys

            # Create a CSV writer object
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # If the file is empty, write the header row
            if csv_file.tell() == 0:
                writer.writeheader()

            # Write the data to the CSV file
            for row in data:
                writer.writerow(row)

        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage to generate 1500 records with random data
data_to_insert = []

for i in range(1500):
    campaign_data = {
        "Campaign_ID": i + 1,
        "Date": f"2023-10-{i % 30 + 1}",
        "Ad_Type": random.choice(["Display", "Search", "Social"]),
        "Clicks": random.randint(100, 1000),
        "Impressions": random.randint(2000, 10000),
        "Conversions": random.randint(5, 50),
        "CTR (Click-Through Rate)": f"{random.uniform(1, 10):.2f}%",
        "Conversion_Rate": f"{random.uniform(1, 10):.2f}%",
        "Revenue_Created": random.randint(100, 1000),
        "Cost": random.randint(50, 500),
        "Owner": f"0x{''.join(random.choice('0123456789ABCDEF') for _ in range(40))}",  # Random Ethereum address
        "Likes": random.randint(0, 1000),  # Random number of likes
        "Dislikes": random.randint(0, 1000),  # Random number of dislikes
        "Fraud": random.choice([0, 1])  # Binary attribute indicating fraud (0 or 1)
    }
    data_to_insert.append(campaign_data)

csv_file_path = "campaign_data.csv"
insert_data_into_csv(csv_file_path, data_to_insert)
