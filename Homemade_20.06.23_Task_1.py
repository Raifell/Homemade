import json, requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


json_name = [
    "file_1(id=1).json",
    "file_2(id=2).json",
    "file_3(id=3).json",
    "file_4(id=4).json",
    "file_5(id=5).json",
    "file_6(id=6).json",
    "file_7(id=7).json",
    "file_8(id=8).json",
    "file_9(id=9).json",
    "file_10(id=10).json"
]


def form(name, todos):
    count_id = []
    count_list = []
    count_file = []

    for x in todos:
        if x["userId"] not in count_id:
            count_id.append(x["userId"])

    index = 0
    for x in todos:
        if x["userId"] in count_id:
            if count_id.index(x["userId"]) == index:
                count_list.append(x)

            else:
                index += 1
                count_file.append(count_list)
                count_list = []
                count_list.append(x)

    count_file.append(count_list)

    for x in range(len(count_file)):
        with open(name[x], 'w') as file:
            json.dump(count_file[x], file, indent=2)


form(json_name, todos)
