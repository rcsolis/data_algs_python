import pandas as pd

data = {
    "name":
    [
        "Rafa",
        "Emi",
        "Sofi",
        "Pam"
    ],
    "age": [
        35,
        15,
        8,
        32
    ]
}

dataFrame = pd.DataFrame(data)

print(dataFrame)

# Extract adults
result = dataFrame[(dataFrame['age'] > 18)]
print(result)
