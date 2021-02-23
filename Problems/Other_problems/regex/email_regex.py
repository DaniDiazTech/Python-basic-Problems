import re

another = "[a-zA-ZÀ-ÿ\u00f1\u00d1]+"

regex = "^est\.[a-zA-ZÀ-ÿ\u00f1\u00d10-9]+@liceocarmelita\.edu\.co$"

while 1:
    i = input("email >>> ")
    if i == "done":
        break

    print("Yeah, good" if bool(re.match(regex, i)) else "NO match :(")
