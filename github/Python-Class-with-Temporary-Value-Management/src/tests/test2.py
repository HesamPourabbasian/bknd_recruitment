class AccessLogger:
    def __init__(self):
        self.data = 42

    def __getattribute__(self, name):
        # Access the attribute using object.__getattribute__ to avoid recursion
        value = object.__getattribute__(self, name)
        print(f"Accessing attribute '{name}' with value: {value}")
        return value


# Usage
obj = AccessLogger()
print(obj.data)  # Output: Accessing attribute 'data' with value: 42
#         42
