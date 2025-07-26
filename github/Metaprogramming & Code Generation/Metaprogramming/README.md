
# 🧠 Metaprogramming in Python

Metaprogramming in Python involves writing code that **manipulates or generates other code dynamically**. It allows programs to inspect, modify, or create code at runtime, enabling powerful abstractions and automation.

A subset of metaprogramming, **code generation**, focuses on programmatically generating source code, often to reduce boilerplate or adapt to dynamic requirements.

This guide introduces key concepts, techniques, and practical examples to get you started.

---

## 📚 Key Concepts

- **Introspection**: Examining code structures at runtime (e.g., inspecting classes, functions, or modules).
- **Dynamic Code Execution**: Creating or modifying code during execution using tools like `exec()` or `eval()`.
- **Metaclasses**: Classes that define the behavior of other classes.
- **Decorators**: Functions that modify or extend other functions or methods.
- **Code Generation**: Programmatically creating source code or executable structures.

---

## 1️⃣ Decorators

Decorators are a common metaprogramming tool. They wrap a function or method to add functionality without modifying the original source.

### Example: Timing a Function

```python
import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function(n):
    time.sleep(n)
    return n * 2

print(slow_function(1))  # Output: slow_function took 1.00 seconds, 2
````

---

## 2️⃣ Metaclasses

Metaclasses customize class creation. Python’s default metaclass is `type`, but you can define your own.

### Example: Enforcing Method Naming Convention

```python
class MethodNameChecker(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith("do_"):
                raise ValueError(f"Method {attr_name} must start with 'do_'")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MethodNameChecker):
    def do_something(self):  # Valid
        pass
    # def invalid_method(self):  # Would raise ValueError
    #     pass
```

---

## 3️⃣ Dynamic Code Execution

Python provides `exec()` and `eval()` to run dynamically created code. Use with **caution**, especially with untrusted input.

### Example: Creating a Function at Runtime

```python
code = """
def generated_function(x):
    return x * 2
"""
exec(code)
print(generated_function(5))  # Output: 10
```

---

## 4️⃣ Code Generation

Generate classes or functions programmatically to reduce repetition.

### Example: Dynamic Class Generator

```python
def generate_class(class_name, attributes):
    attr_code = "\n".join(f"    {name} = None" for name in attributes)
    class_code = f"""
class {class_name}:
{attr_code}
    def __init__(self, {', '.join(attributes)}):
        {"; ".join(f"self.{name} = {name}" for name in attributes)}
    def __str__(self):
        return f"{class_name}({', '.join(f'{name}={{self.{name}}}' for name in attributes)})"
"""
    namespace = {}
    exec(class_code, namespace)
    return namespace[class_name]

Person = generate_class("Person", ["name", "age"])
p = Person("Alice", 30)
print(p)  # Output: Person(name=Alice, age=30)
```

---

## 5️⃣ Introspection

Python allows inspecting objects using `dir()`, `getattr()`, `hasattr()`, and `inspect`.

### Example: Invoking Methods Dynamically

```python
class Worker:
    def do_task(self):
        return "Task done"

worker = Worker()
method_name = "do_task"
if hasattr(worker, method_name):
    result = getattr(worker, method_name)()
    print(result)  # Output: Task done
```

---

## 6️⃣ Real-World Use Cases

* **ORMs** (e.g., SQLAlchemy)
* **Testing frameworks** (e.g., pytest)
* **API clients** (from OpenAPI specs)
* **Domain-specific languages** (DSLs)

---

## ✅ Best Practices

* **Keep It Simple**: Don’t overcomplicate logic unless needed.
* **Security**: Avoid `exec()`/`eval()` with untrusted input.
* **Documentation**: Always document metaprogramming logic.
* **Testing**: Generated code must be tested thoroughly.

---

## 🧰 Tools and Libraries

* `ast`: Abstract Syntax Tree manipulation.
* `inspect`: Advanced runtime introspection.
* `functools`: Tools like `wraps()` for decorators.
* `jinja2`: Generate code as templates.

---

## 💡 Example: Safe Code Generation with `ast`

```python
import ast

code = ast.FunctionDef(
    name="multiply",
    args=ast.arguments(
        posonlyargs=[],
        args=[ast.arg(arg="x"), ast.arg(arg="y")],
        kwonlyargs=[], kw_defaults=[], defaults=[]
    ),
    body=[ast.Return(ast.BinOp(
        left=ast.Name(id="x", ctx=ast.Load()),
        op=ast.Mult(),
        right=ast.Name(id="y", ctx=ast.Load())
    ))],
    decorator_list=[]
)

module = ast.Module(body=[code], type_ignores=[])
code_obj = compile(module, "<string>", "exec")
namespace = {}
exec(code_obj, namespace)

print(namespace["multiply"](4, 5))  # Output: 20
```

---

## ⚠️ Limitations & Risks

* **Complexity**: Harder to understand and debug.
* **Performance**: Slightly slower due to dynamic overhead.
* **Security**: Be cautious with dynamic execution.
