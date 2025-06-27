# **TempValue Class - Context Manager for Temporary Values**  

This Python class, `TempValue`, allows you to **temporarily** set and access a value within a `with` block. Once the block exits, the value is automatically removed.  

## **Features**  
✅ **Temporary Value Storage** – The value is only accessible inside the `with` block.  
✅ **Safe Attribute Handling** – Returns `"Not set"` if accessed outside the context.  
✅ **Clean Resource Management** – Uses Python’s context manager protocol (`__enter__`, `__exit__`).  

## **How It Works**  

### **1. Initialization**  
- When you create a `TempValue` object, it stores the given value in `self.temp_value`.  
- `self._data` is an empty dictionary that will later hold the temporary value.  

```python
obj = TempValue("Hello")  # Initializes with temp_value="Hello"
```

### **2. Accessing the Value (`obj.value`)**  
- If you try to access `obj.value` **outside** a `with` block, it returns `"Not set"` because the key `"value"` doesn’t exist in `self._data`.  
- Inside the `with` block, the value is temporarily stored, so `obj.value` returns the stored value.  

```python
print(obj.value)  # Output: "Not set" (before entering 'with')

with obj:
    print(obj.value)  # Output: "Hello" (temporarily set)

print(obj.value)  # Output: "Not set" (after exiting 'with')
```

### **3. Context Manager Behavior**  
- **`__enter__`** → Stores `self.temp_value` in `self._data["value"]`.  
- **`__exit__`** → Removes `"value"` from `self._data`, cleaning up automatically.  

## **Use Cases**  
🔄 **Temporary Configurations** – Set a value only for a specific block of code.  
🔒 **Secure Data Handling** – Ensure sensitive data is cleared after use.  
🧪 **Testing/Debugging** – Temporarily modify object state without permanent changes.  

## **Example Usage**  
```python
# Create an object with a temporary value
temp_obj = TempValue("Secret Data")

# Outside the context, value is not set
print(temp_obj.value)  # Output: "Not set"

# Inside the context, value is available
with temp_obj:
    print(temp_obj.value)  # Output: "Secret Data"

# After exiting, value is cleared
print(temp_obj.value)  # Output: "Not set"
```

## **Why Use This?**  
- **Cleaner Code**: Avoid manual cleanup of temporary values.  
- **Safer Access**: Prevents accidental access outside intended scope.  
- **Pythonic Design**: Uses context managers (`with`) for resource handling.  

---

### **Installation & Requirements**  
- Requires **Python 3.x** (no external dependencies).  
- Just copy the class into your project!  

---

🚀 **Try it out and see how it simplifies temporary value management!** 🚀