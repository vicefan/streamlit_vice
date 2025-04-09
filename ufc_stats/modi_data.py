import json

with open("./match_results.json", "r", encoding="utf-8") as f:
    match_dict = json.load(f)

for key, value in match_dict.items():
    match_dict[key] = list(set(value))

with open("match_results.json", "w", encoding="utf-8") as f:
    json.dump(match_dict, f, ensure_ascii=False, indent=4)