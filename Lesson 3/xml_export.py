from lxml import etree

# Sample user data
users = [
    {"name": "John Doe", "email": "johndoe@example.com", "age": 30, "occupation": "Software Developer"},
    {"name": "Jane Doe", "email": "janedoe@example.com", "age": 28, "occupation": "Graphic Designer"},
    {"name": "Mike Ross", "email": "mikeross@example.com", "age": 35, "occupation": "Lawyer"},
    {"name": "Harvey Specter", "email": "harveyspecter@example.com", "age": 40, "occupation": "Senior Partner"}
]

# Create the root element
root = etree.Element("users")

# Iterate over the user data and create XML elements
for user in users:
    # Create a subelement for each user in the root element
    user_elem = etree.SubElement(root, "user")
    # Add a 'name' subelement under each 'user' element
    name_elem = etree.SubElement(user_elem, "name")
    name_elem.text = user["name"]
    # Add an 'email' subelement under each 'user' element
    email_elem = etree.SubElement(user_elem, "email")
    email_elem.text = user["email"]
    # Add an 'age' subelement under each 'user' element, converting the age to string
    age_elem = etree.SubElement(user_elem, "age")
    age_elem.text = str(user["age"])
    # Add an 'occupation' subelement under each 'user' element
    occupation_elem = etree.SubElement(user_elem, "occupation")
    occupation_elem.text = user["occupation"]

# Create a tree from the root element
tree = etree.ElementTree(root)

try:
    # Write the tree to an XML file with pretty formatting
    with open("users.xml", "wb") as f:  # "wb" stands for "write binary", and it's used here because XML files are saved as binary data to ensure proper encoding is maintained.
        f.write(etree.tostring(root, pretty_print=True, encoding="utf-8", xml_declaration=True))
except IOError as e:
    print(f"An error occurred while writing the file: {e}")