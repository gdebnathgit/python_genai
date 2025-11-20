import pandas as pd
import json

json_data = '{"name": "John", "age": 30, "city": "Delhi"}'
record = pd.json_normalize(json.loads(json_data))

print(record["name"])

json_data = '{"name": "John", "age": 30, "city": "Delhi"}'
record = json.loads(json_data)


print(record)
