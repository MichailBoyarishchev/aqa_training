import json
import module1

json_strings = """
{
    "response":{
    "items":[{
        "id":1,
        "name":"Anny",
        "number":"+380961727223"},
        {
        "id":2,
        "name":"Janny",
        "number":"+380501225644"},
        {
        "id":3,
        "name":"Penny",
        "number":"+380931234321"},
        {
        "id":4,
        "name":"Tommy",
        "number":"+380504141414"},
        {
        "id":5,
        "name":"Sam",
        "number":"+380961626226"}]


}
}"""

data = json.loads(json_strings)

with open("my.json", "w") as file:
    json.dump(data, file, indent=3)
with open("my.json", "r") as file:
    json.load(file)

module1.parser(data)

module1.parser2(data)
