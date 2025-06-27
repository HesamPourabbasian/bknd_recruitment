class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Active connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        if exc_type:
            print(f"Exception occurred: {exc_type}, {exc_value}")
            return False  # Let exception propagate
        return True


# Usage
with DatabaseConnection("my_db") as conn:
    print(f"Using {conn}")
    # Simulate an error
    # raise ValueError("Oops!")

# Output (without error):
# Connecting to my_db...
# Using Active connection to my_db
# Closing connection to my_db

# Output (with error):
# Connecting to my_db...
# Using Active connection to my_db
# Closing connection to my_db
# Exception occurred: <class 'ValueError'>, Oops!
# (ValueError is raised)
