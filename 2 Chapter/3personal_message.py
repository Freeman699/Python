name = "     hugh laurie      "
message = f"Hello {name.title()}, how are you?"
print(message)

message = f"Hello {name.title().lstrip()}, how are you?"
print(message)

message = f"Hello {name.title().rstrip()}, how are you?"
print(message)

message = f"Hello {name.title().strip()}, how are you?"
print(message)