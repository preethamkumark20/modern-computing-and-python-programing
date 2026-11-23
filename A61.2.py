
text = input("Enter a string: ")

print("*" * 10 + " Indexing and Slicing " + "*" * 10)
print("First character:", text[0])
print("Last character:", text[-1])
print("First 3 characters:", text[0:3])
print("From index 3 onwards:", text[3:])
print("Reverse of text:", text[::-1])
print("Second character:", text[1])

print("*" * 10 + " Case Conversion " + "*" * 10)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

sub = input("Enter a character or substring: ")
print("'" + sub + "' occurs", text.count(sub), "time(s)")

print("*" * 10 + " Replace a Word " + "*" * 10)
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("After replacing:", text.replace(old, new))

print("*" * 10 + " Split and Join " + "*" * 10)
words = text.split()
print("After split:", words)
print("After join:", "-".join(words))

print("*" * 10 + " Starts With and Ends With " + "*" * 10)
start = input("Enter the substring to check at the start: ")
end = input("Enter the substring to check at the end: ")
print("Starts with:", text.startswith(start))
print("Ends with:", text.endswith(end))


