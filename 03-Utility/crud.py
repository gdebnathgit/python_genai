import pandas as pd

df = pd.DataFrame([
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Sara"}
])

# Add a new record
new_record = {"id": 3, "name": "Amit"}

df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
# print(df)

# Delete a Record by Index
# df = df.drop(1)      # deletes row with index 1
# df = df.reset_index(drop=True)
# print(df)

# Delete Record Using a Condition
df = df[df["id"] != 2]
df = df.reset_index(drop=True)
# print(df)


# Update a Record
df.loc[df["id"] == 1, "name"] = "Johnny"

for name in df["name"]:
    print(name)
