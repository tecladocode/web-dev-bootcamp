"""Python refresher course - Strings Section"""

name = "Michelle"
greeting = f"Hello, {name}"

print(greeting)

# below is a string template
name = "Milo"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

# below is an example of a longer template using the .format method
longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("PK", "Thursday")

print(formatted)
