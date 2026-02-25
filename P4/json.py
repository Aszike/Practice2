import json

# JSON строка
sample_json = '{"name": "Almaty", "population": 2000000, "is_capital": false}'

# 1. Из JSON в Dictionary
data = json.loads(sample_json)
print(f"Город: {data['name']}")

# 2. Из Dictionary в JSON (с отступами для красоты)
python_dict = {"course": "Python", "practice": 4, "completed": True}
json_string = json.dumps(python_dict, indent=4)
print(json_string)