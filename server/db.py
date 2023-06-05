import json
import os

class DBHandler:
    """A simple class for handling CRUD operations on a JSON file."""
    
    def __init__(self, file_name="db.json"):
        """
        Args:
            file_name (str): Path to the JSON file.
        """
        self.file_name = file_name
        
    def log_request(self, A, B, C, D):
        """
        Log a new request in the JSON file.

        Args:
            A (str): First word in analogy.
            B (str): Second word in analogy.
            C (str): Third word in analogy.
            D (str): Fourth word in analogy (computed response).

        Example:
            >>> db = DBHandler()
            >>> db.log_request("man", "king", "woman", "queen")
        """
        # Read existing data
        data = self.get_all_logs()
        
        # Append new record
        data.append([A, B, C, D])

        # Write back to file
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False, sort_keys=False)
        
    def get_all_logs(self):
        """
        Retrieve all logs from the JSON file.
        
        Returns:
            data (list): A nested list representing the logs.

        Example:
            >>> db = DBHandler()
            >>> logs = db.get_all_logs()
            >>> print(logs)
        """
        if not os.path.exists(self.file_name):
            return []
        
        with open(self.file_name, "r") as file:
            data = json.load(file)
        return data

# If the module is run directly, demonstrate its usage
if __name__ == "__main__":
    db = DBHandler()
    db.log_request("man", "king", "woman", "queen")
    logs = db.get_all_logs()
    print(logs) # Expect: ['man', 'king', 'woman', 'queen']
