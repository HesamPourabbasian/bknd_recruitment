class LoggingAccess:
    def __init__(self):
        self._name = None

    def __set_name__(self, owner, name):
        self.attr_name = name

    def __get__(self, instance, owner):
        value = instance.__dict__.get(self.attr_name)
        print(f"Accessing '{self.attr_name}': {value}")
        return value

    def __set__(self, instance, value):
        if self.attr_name == 'name' and not isinstance(value, str):
            print("Error: name must be a string.")
        elif self.attr_name == 'age' and not isinstance(value, int):
            print("Error: age must be an integer.")
        else:
            print(f"Setting '{self.attr_name}' to {value}")
            instance.__dict__[self.attr_name] = value


class Person:
    name = LoggingAccess()
    age = LoggingAccess()


# Example usage
p = Person()
p.name = "Hesam"
p.age = 21
print(p.name)
print(p.age)
