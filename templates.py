from jinja2 import Template

# Load the templates
basic_template = Template(open("basic_template.html").read())
dynamic_template = Template(open("dynamic_template.html").read())
conditional_template = Template(open("conditional_template.html").read())

# Example data
data = {
    "subject": "Welcome to Our Newsletter!",
    "body": "Thank you for subscribing to our newsletter.",
    "recipient_name": "John Doe",
    "sender_name": "Company XYZ",
    "attachment": True  # Simulating conditional content
}

# Render templates
basic_email = basic_template.render(**data)
dynamic_email = dynamic_template.render(**data)
conditional_email = conditional_template.render(**data)

print("Basic Email:")
print(basic_email)
print("\nDynamic Email:")
print(dynamic_email)
print("\nConditional Email:")
print(conditional_email)
