import json

session_data_filename = "session_data.json"

def save_session_data(data):
    """
    Saves session data to a file.
    """
    with open(session_data_filename, 'w') as f:
        json.dump(data, f)

def load_session_data():
    """
    Loads session data from a file.
    """
    try:
        with open(session_data_filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file does not exist
