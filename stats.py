def sort_on(dict):
    return dict["count"]

def word_count(text):
    text_list = text.split()
    return len(text_list)

def character_count(text):
    char_dict = [{"char" : "a", "count" : 0},
                 {"char" : "b", "count" : 0},
                 {"char" : "c", "count" : 0},
                 {"char" : "d", "count" : 0},
                 {"char" : "e", "count" : 0},
                 {"char" : "f", "count" : 0},
                 {"char" : "g", "count" : 0},
                 {"char" : "h", "count" : 0},
                 {"char" : "i", "count" : 0},
                 {"char" : "j", "count" : 0},
                 {"char" : "k", "count" : 0},
                 {"char" : "l", "count" : 0},
                 {"char" : "m", "count" : 0},
                 {"char" : "n", "count" : 0},
                 {"char" : "o", "count" : 0},
                 {"char" : "p", "count" : 0},
                 {"char" : "q", "count" : 0},
                 {"char" : "r", "count" : 0},
                 {"char" : "s", "count" : 0},
                 {"char" : "t", "count" : 0},
                 {"char" : "u", "count" : 0},
                 {"char" : "v", "count" : 0},
                 {"char" : "w", "count" : 0},
                 {"char" : "x", "count" : 0},
                 {"char" : "y", "count" : 0},
                 {"char" : "z", "count" : 0},
                 {"char" : "æ", "count" : 0},
                 {"char" : "â", "count" : 0},
                 {"char" : "ê", "count" : 0},
                 {"char" : "ë", "count" : 0},
                 {"char" : "ô", "count" : 0}] 

    text = text.lower()
    for char in text:
        if char == "a":
            char_dict[0]["count"] += 1
        elif char == "b":
            char_dict[1]["count"] += 1
        elif char == "c":
            char_dict[2]["count"] += 1
        elif char == "d":
            char_dict[3]["count"] += 1
        elif char == "e":
            char_dict[4]["count"] += 1
        elif char == "f":
            char_dict[5]["count"] += 1
        elif char == "g":
            char_dict[6]["count"] += 1
        elif char == "h":
            char_dict[7]["count"] += 1
        elif char == "i":
            char_dict[8]["count"] += 1
        elif char == "j":
            char_dict[9]["count"] += 1
        elif char == "k":
            char_dict[10]["count"] += 1
        elif char == "l":
            char_dict[11]["count"] += 1
        elif char == "m":
            char_dict[12]["count"] += 1
        elif char == "n":
            char_dict[13]["count"] += 1
        elif char == "o":
            char_dict[14]["count"] += 1
        elif char == "p":
            char_dict[15]["count"] += 1
        elif char == "q":
            char_dict[16]["count"] += 1
        elif char == "r":
            char_dict[17]["count"] += 1
        elif char == "s":
            char_dict[18]["count"] += 1
        elif char == "t":
            char_dict[19]["count"] += 1
        elif char == "u":
            char_dict[20]["count"] += 1
        elif char == "v":
            char_dict[21]["count"] += 1
        elif char == "w":
            char_dict[22]["count"] += 1
        elif char == "x":
            char_dict[23]["count"] += 1
        elif char == "y":
            char_dict[24]["count"] += 1
        elif char == "z":
            char_dict[25]["count"] += 1
        elif char == "æ":
            char_dict[26]["count"] += 1
        elif char == "â":
            char_dict[27]["count"] += 1
        elif char == "ê":
            char_dict[28]["count"] += 1
        elif char == "ë":
            char_dict[29]["count"] += 1
        elif char == "ô":
            char_dict[30]["count"] += 1
    char_dict == char_dict.sort(key=sort_on, reverse=True)
    return char_dict

