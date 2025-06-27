class DynamicObject:
    def __init__(self):
        self.real_attr = "I'm real!"

    def __getattribute__(self, name):
        print(f"__getattribute__ called for '{name}'")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print(f"__getattr__ called for missing attribute '{name}'")
        return f"Dynamically created: {name}"


# Usage
obj = DynamicObject()
print(obj.real_attr)  # Output: __getattribute__ called for 'real_attr'
#         I'm real!
print(obj.fake_attr)  # Output: __getattribute__ called for 'fake_attr'
#         __getattr__ called for missing attribute 'fake_attr'
#         Dynamically created: fake_attr
