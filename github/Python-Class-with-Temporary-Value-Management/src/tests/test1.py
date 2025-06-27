class DynamicConfig:
    def __init__(self):
        self._config = {"timeout": 30, "retries": 3}

    def __getattr__(self, name):
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"No such attribute: {name}")


# Usage
config = DynamicConfig()
print(config.timeout)  # Output: 30
print(config.retries)  # Output: 3
# print(config.unknown)  # Raises AttributeError: No such attribute: unknown
