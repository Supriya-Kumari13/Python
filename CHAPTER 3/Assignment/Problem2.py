#Write a python program to fill in a letter template given below with name and date.
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>", "Mahi").replace("<|DATE|>", "3 april 2025"))  # Replace placeholders with actual values
