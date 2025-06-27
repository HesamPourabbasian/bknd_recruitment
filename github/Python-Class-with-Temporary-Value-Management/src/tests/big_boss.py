class TempValue:
    def __init__(self, temp_value):
        self._data = {}
        self.temp_value = temp_value

    def __getattr__(self, name):
        if name == "value":
            return self._data.get(name, "Not set")
        raise AttributeError(f"No such attribute: {name}")

    def __enter__(self):
        self._data["value"] = self.temp_value
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._data.pop("value", None)


obj = TempValue("Hello")
print(obj.value)  # Output: Not set
with obj:
    print(obj.value)  # Output: Hello
print(obj.value)  # Output: Not set
