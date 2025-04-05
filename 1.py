std={
    "name":"rahul",
    "age":20,
    "roll":10
    }
new_std=std.copy()
print(new_std)

print(std.get("name"))

print(std.keys())

print(std.items())

print(std.values())

std.update({"age:25"})

print(std)