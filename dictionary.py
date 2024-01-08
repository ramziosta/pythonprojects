box = {"a": 2, "b": "string", "c": [1, "stringy", 44]}

answer = box.get("a") + 4

for i in box:
    if box.get(i) == "string":
        print(box.get(i) + "I am a sting as well")
    elif type(box.get(i)) == list:
        box.get(i).append(666)
        print(box.get(i))
    else:
        print(box.get(i) + 4)
