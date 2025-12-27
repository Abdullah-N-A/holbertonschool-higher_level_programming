Python – Serialization (Basic JSON Serialization)
📌 Project Overview

This project introduces the concept of serialization in Python, focusing on converting Python data structures into a JSON format and restoring them back to Python objects.

Serialization is a fundamental concept used in data persistence, file storage, APIs, and data exchange between systems.

In this task, we implement a simple serialization module that:

Saves a Python dictionary into a JSON file.

Loads a JSON file and recreates the original Python dictionary.

🧠 Key Concepts
🔹 What is Serialization?

Serialization is the process of converting a Python object (such as a dictionary) into a format that can be:

Stored in a file

Sent over a network

In this project, the serialization format used is JSON.

🔹 What is Deserialization?

Deserialization is the reverse process:

Reading serialized data (JSON)

Converting it back into a Python data structure

🧩 Task Description

We create a Python module named:

task_00_basic_serialization.py


It contains two functions:

1️⃣ serialize_and_save_to_file(data, filename)

Takes a Python dictionary as input.

Serializes the dictionary into JSON.

Saves it into a file.

Overwrites the file if it already exists.

2️⃣ load_and_deserialize(filename)

Reads a JSON file.

Deserializes its content.

Returns the equivalent Python dictionary.

🛠️ Requirements

Use JSON format

Use file handling with Python

No need to handle file permission or exception errors

The data provided is always a Python dictionary

📂 File Structure
python-serialization/
│
├── task_00_basic_serialization.py
├── README.md
└── data.json (created at runtime)

▶️ Example Usage
from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize
)

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data, "data.json")
print("Data serialized and saved to 'data.json'.")

loaded_data = load_and_deserialize("data.json")
print("Deserialized Data:")
print(loaded_data)

✅ Output
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}

🎯 Learning Outcomes

By completing this task, you should be able to:

Explain serialization and deserialization

Convert Python dictionaries to JSON files

Load JSON files back into Python objects

Understand how JSON is used in real-world applications such as APIs and databases

🚀 Conclusion

This project provides a solid foundation for understanding how data can be stored and transferred efficiently using JSON serialization. These skills are essential for backend development, APIs, and data-driven applications.
