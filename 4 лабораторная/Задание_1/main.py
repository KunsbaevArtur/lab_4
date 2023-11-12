import json
def task() -> float:
    f_n = "input.json"
    with open(f_n) as f:
        json_datda = json.load(f)
    summa = sum([item["score"]* item["weight"] for item in json_datda])
    return round(summa, 3)


print(task())