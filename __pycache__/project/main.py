from file_handler import read_file
from file_handler import write_invalid
from file_handler import save_data
from file_handler import load_data

from processor import process
from processor import get_invalid


print("Secure Log Analyzer & Backup System")

# Read records
records = read_file()

# Remove extra spaces
records = list(map(lambda x: x.strip(), records))

# Process valid records
valid = process(records)

# Find invalid records
invalid = get_invalid(records)


# Display valid records
print("\nValid Records:")

for record in valid:
    print(record)


# Write invalid records
write_invalid(invalid)

print("\nInvalid records saved to invalid_log.txt")


# Save valid records using pickle
save_data(valid)

print("Valid records saved using pickle")


# Load records from pickle
data = load_data()

print("\nRecords loaded from pickle file:")

for record in data:
    print(record)