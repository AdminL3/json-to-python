# JSON to Python Variables Converter

1. **Flatten Nested JSON (`flatten_json` function):**

   - This function recursively traverses a JSON object (dictionaries and lists) and flattens it into a single dictionary with "dot notation" keys.
   - For example:
     ```python
     Input: {"a": {"b": [1, 2]}}
     Output: {"a.b[0]": 1, "a.b[1]": 2}
     ```

2. **Sanitize Variable Names (`sanitize_variable_name` function):**

   - Converts JSON keys into valid Python variable names:
     - Replaces invalid characters with underscores (`_`).
     - Ensures variable names don't start with numbers.
     - Collapses consecutive underscores and trims trailing underscores.
     - Converts everything to lowercase.
   - For example:
     ```python
     Input: "User-Data[1]"
     Output: "user_data_1"
     ```

3. **Generate Python Code (`generate_python_code` function):**
   - Takes the flattened JSON structure and generates Python code to access each value in the JSON using valid Python syntax.
   - Example:
     ```python
     Input: {"a.b[0]": 1, "a.b[1]": 2}
     Output:
         a_b_0 = json_data["a"]["b"][0]
         a_b_1 = json_data["a"]["b"][1]
     ```

---

### **Streamlit App Features**

1. **App Setup:**

   - The app is titled **"JSON to Python Variables Converter"** with a snake 🐍 icon.

2. **User Input:**

   - A text area (`st.text_area`) lets users paste their JSON data.

3. **Processing the JSON:**

   - If valid JSON is entered:
     - It is parsed using `json.loads`.
     - Flattened and sanitized.
     - Python code to access all keys/values is generated and displayed using `st.code`.

4. **Error Handling:**

   - If the input is not valid JSON, an error message is displayed using `st.error`.

5. **Instructions:**
   - If the input field is empty, the app shows an info box (`st.info`) with instructions.

---

### **Example Use Case**

#### Input JSON:

```json
{
	"user": {
		"name": "Alice",
		"details": {
			"age": 25,
			"hobbies": ["reading", "hiking"]
		}
	}
}
```

#### Generated Python Code:

```python
user_name = json_data["user"]["name"]
user_details_age = json_data["user"]["details"]["age"]
user_details_hobbies_0 = json_data["user"]["details"]["hobbies"][0]
user_details_hobbies_1 = json_data["user"]["details"]["hobbies"][1]
```

---

### **Purpose**

- Quickly convert a JSON structure into Python variable access code for easier use in scripts or debugging.
- Useful for programmers working with large, nested JSON data.
