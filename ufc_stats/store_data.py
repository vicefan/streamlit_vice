import json

with open("match_results.txt", "r", encoding="utf-8") as f:
    match_results = f.read().strip("\n").strip("[]").replace("'", "").replace('"', "").split("], [")

match_results = [match.split(", ") for match in match_results]
match_results = sorted(match_results, key=lambda x: x[0])

match_dict = {}
for match in match_results:
    winner, loser = match
    if winner in match_dict:
        match_dict[winner].append(loser)
    else:
        match_dict[winner] = [loser]

for key, value in match_dict.items():
    match_dict[key] = sorted(value)


with open("match_results.json", "w", encoding="utf-8") as f:
    json.dump(match_dict, f, ensure_ascii=False, indent=4)