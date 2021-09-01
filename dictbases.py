print("DICTIONARIES")
print("Key/Value pairs, are Unordered")

print("create dicts with {}")
x = {"name":"Rafael", "age":35, "job":"Software Engineer", 10:"Ten"}
print(x, type(x))
del x
print("Create using dict with list of key/value tuples")
x = dict([
    ("name", "Rafael"),
    ("age", 35),
    ("job", "Software engineer")
])
print(x, type(x))
print("Create using dict with named paramets")
x = dict(name="Rafael", age=35, job="Software Engineer")
print(x, type(x))

print("adding or update")
x["name"] = "Rafael Chavez"
x["programming"] = "Python/Go/Node/C++"
x["company"] = "FANG"
print(x)
print("Delete item")
del(x["company"])
print(x)
print("Length ")
print(len(x))
print("Clear items")
x.clear()
print(x)
x = dict(name="Rafael", age=35, job="Software Engineer")
print("Access keys, values and items")
print("Keys")
print(x.keys())
print("Values")
print(x.values())
print("Items (returns list of tuples)")
print(x.items())
print("Check membership only in keys")
print(x, "job", "job" in x)
print("Check membership only in values")
print(x, "Rafael", "Rafael" in x.values())

print("Iterating (Unordered)")
print("Loop using keys")
for k in x:
    print(k, x[k])
print("Loop using keys and values (using items)")
for k, v in x.items():
    print(k, v)
