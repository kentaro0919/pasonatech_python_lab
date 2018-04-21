title = "star wars : the empire strikes back"


def formatter(st):
    title = st.split(":")[0].upper().center(60)
    subtitle = "\n" + st.split(":")[1].strip(" ").title().center(60)
    return title + subtitle

print(formatter(title))