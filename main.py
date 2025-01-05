import streamlit as st
import json
from typing import Dict, Any, List


def flatten_json(data: Any, prefix: str = '') -> Dict[str, Any]:
    """Flatten nested JSON into dot notation."""
    items: List = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            items.extend(flatten_json(value, new_prefix).items())
    elif isinstance(data, list):
        for i, value in enumerate(data):
            new_prefix = f"{prefix}[{i}]"
            items.extend(flatten_json(value, new_prefix).items())
    else:
        items.append((prefix, data))

    return dict(items)


def sanitize_variable_name(name: str) -> str:
    """Convert JSON key to valid Python variable name."""
    # Replace invalid characters with underscore
    sanitized = ''.join(c if c.isalnum() else '_' for c in name)
    # Ensure it doesn't start with a number
    if sanitized[0].isdigit():
        sanitized = 'v_' + sanitized
    # Remove consecutive underscores
    while '__' in sanitized:
        sanitized = sanitized.replace('__', '_')
    # Remove trailing underscores
    sanitized = sanitized.rstrip('_')
    return sanitized.lower()


def generate_python_code(json_data: Dict) -> str:
    """Generate Python code for accessing all values in the JSON."""
    # Flatten the JSON
    flat_data = flatten_json(json_data)

    # Generate Python code for each flattened key
    python_lines = []
    for path, _ in flat_data.items():
        var_name = sanitize_variable_name(path)
        parts = path.replace('[', '.[').split('.')

        # Generate the access code
        access_parts = []
        for part in parts:
            if part.startswith('[') and part.endswith(']'):
                # Handle list index
                access_parts.append(f"{part}")
            else:
                # Handle dict key
                access_parts.append(f'["{part}"]')

        python_lines.append(f"{var_name} = json_data{'.get('.join(
            access_parts)}" if '.get(' in access_parts else f"{var_name} = json_data{''.join(access_parts)}")

    return '\n'.join(python_lines)


# Start Streamlit app

st.set_page_config(
    page_title="JSON to Python Converter",
    page_icon="🐍",
)

st.header("JSON to Python Variables Converter")

json_input = st.text_area(
    "Paste your JSON here:",
    height=300
)

if json_input != '':
    try:
        json_data = json.loads(json_input)

        python_code = generate_python_code(json_data)

        st.code(python_code, language="python")

    except json.JSONDecodeError:
        st.error("Invalid JSON input.")
else:
    st.info("Paste your JSON in the input above.")
