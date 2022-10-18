kievstar = "096"
life = "093"
vodafone = "050"


def parser(x):
    for item in x["response"]["items"]:
        if (str(item["number"][3:6])) == kievstar:
            print(str(item["number"] + " this is kievstar"))
        if (str(item["number"][3:6])) == life:
            print(str(item["number"] + " this is life"))
        if (str(item["number"][3:6])) == vodafone:
            print(str(item["number"] + " this is vodafone"))


def parser2(x):
    for item in x["response"]["items"]:
        print(str(item["number"][6:]))
