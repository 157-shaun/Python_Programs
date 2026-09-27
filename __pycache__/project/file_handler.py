import pickle


def read_file():
    try:
        file = open("log.txt", "r")
        records = file.readlines()
        file.close()

        return records

    except:
        print("Error reading file")
        return []


def write_invalid(records):
    try:
        file = open("invalid_log.txt", "w")

        for record in records:
            file.write(record + "\n")

        file.close()

    except:
        print("Error writing file")


def save_data(records):
    try:
        file = open("valid_records.pkl", "wb")
        pickle.dump(records, file)
        file.close()

    except:
        print("Error saving pickle file")


def load_data():
    try:
        file = open("valid_records.pkl", "rb")
        records = pickle.load(file)
        file.close()

        return records

    except:
        print("Error loading pickle file")
        return []