import xml.etree.ElementTree as ET

# This script is designed to parse data from XML files. It stores the text content of each element
# within a global dictionary, allowing for quick access and processing of the information.
# This script demonstrates the parsing process and then uses the parsed data to print values associated with
# specific tags and to calculate and print the average price, if price information is available.
# It also includes examples of using the walrus operator and the ternary conditional operator for cleaner code.

# Examples for new programmers:
# - To use this script, ensure you have an XML file ready and call parse_xml(file_path) where file_path is the file path to your XML.
# - After parsing, you can use print_values_from_tag(tag) to print all values for a specific tag in the XML.
# - The script also demonstrates advanced Python features like list comprehensions, the walrus operator, and ternary conditional operators.

# Global list to store the parsed data
parsed_data = {}

def parse_xml(file_path):
    global parsed_data
    try:
        # Attempt to parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Append all elements' text content to the global list
        for elem in root.iter():
            if elem.text and isinstance(elem.text, str) and elem.text.strip():
                if elem.tag not in parsed_data:
                    parsed_data[elem.tag] = [] # Initialize a list for new tags
                if elem.text and elem.text.strip():
                    parsed_data[elem.tag].append(elem.text.strip()) # Append text, ensuring it's stripped of whitespace

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ET.ParseError:
        print(f"Error: There was a problem parsing the file {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print(f"Successfully parsed {file_path}")

def print_values_from_tag(tag):
    # This function prints all values found for a given XML tag
    if tag in parsed_data:
        for value in parsed_data[tag]:
            print(value)
    else:
        print(f"No values found for tag: {tag}")

# Path to the XML file
xml_file_path = 'example.xml'
parse_xml(xml_file_path)

# Print all parsed titles
print_values_from_tag('title')

# Calculate the average price if available
if parsed_data.get('price'):
    prices = [float(price) for price in parsed_data['price']]
    if prices:
        print(f"The average price is: {sum(prices) / len(prices)}")
    else:
        print("No prices found.")
else:
    print("No price information available.")

# Optimized version
if prices := parsed_data.get('price'):  # := is the walrus operator, allowing variable assignment and return in a single expression
    prices = [float(price) for price in prices] # Convert price strings to floats for calculation
    # The ternary conditional operator is used here. It's like a compact if-else statement.
    # Syntax: [on_true] if [condition] else [on_false]
    # If 'prices' list is not empty, the average is computed and printed. Otherwise, it prints "No prices found".
    print(f"The average price is: {sum(prices) / len(prices)}" if prices else "No prices found.")

# Example of ternary conditional operator
# Determines if a number is positive or not
number = 5
result = "Positive" if number > 0 else "Non-positive"
print(result)  # Output: Positive

# Another example
# Checks if a list is empty and prints an appropriate message
my_list = []
print("List is not empty" if my_list else "List is empty")  # Output: List is empty

# One more example
# Decides between two actions based on a boolean flag
is_raining = False
activity = "Go for a walk" if not is_raining else "Stay indoors"
print(activity)  # Output: Go for a walk