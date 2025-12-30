"""
String Utility Functions
"""

def camel_to_snake(name):
    """Convert camelCase to snake_case."""
    result = [name[0].lower()]
    for char in name[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

def snake_to_camel(name):
    """Convert snake_case to camelCase."""
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate(text, length=50, suffix='...'):
    """Truncate text to specified length."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix

def word_count(text):
    """Count words in text."""
    return len(text.split())

# Examples
if __name__ == "__main__":
    print(camel_to_snake("myVariableName"))  # my_variable_name
    print(snake_to_camel("my_variable_name"))  # myVariableName
