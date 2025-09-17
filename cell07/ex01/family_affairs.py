def find_the_redheads(family: dict):
    redheads = filter(lambda name: family[name] == "red", family.keys())
    return list(redheads)


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))