import re

input_string = input()

# Ensure that the input is surrounded by (non-escaped) "", and remove.
if not re.match(r'^".*[^\\]"$', input_string):
    raise ValueError('Invalid string! (Doesn\'t end)')
input_string = input_string[1:-1]

# Replace escaped characters with their equivalent.
input_string = input_string.replace(r'\n', '\n')
input_string = input_string.replace(r'\"', '"')
input_string = input_string.replace(r'\\', '\\')

# Ensure that there aren't any other characters to escape (invalid).
escape_match = re.search(r'\\[a-zA-Z]', input_string)
if escape_match:
    escape_code = escape_match.group(0)
    raise ValueError('Invalid string! (Bad escape code, %s)' % escape_code)

print(input_string)