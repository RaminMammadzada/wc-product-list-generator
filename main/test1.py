import json
correctAnswer = """{"Numara":{"name":"Numara","type":"label","terms":{"40":{"name":"40","color":"","image":"","show_tooltip":"","tooltip_text":"","tooltip_image":"","image_size":""},"41":{"name":"41","color":"","image":"","show_tooltip":"","tooltip_text":"","tooltip_image":"","image_size":""},"42":{"name":"42","color":"","image":"","show_tooltip":"","tooltip_text":"","tooltip_image":"","image_size":""},"43":{"name":"43","color":"","image":"","show_tooltip":"","tooltip_text":"","tooltip_image":"","image_size":""},"44":{"name":"44","color":"","image":"","show_tooltip":"","tooltip_text":"","tooltip_image":"","image_size":""},"45":{"name":"45","color":"","image":"","show_tooltip":"","tooltip_text":"","tooltip_image":"","image_size":""}}}}
                            """

# create json for Swatches Attributes
def createSwatchAttributesJson(sizes=[40,41,42,43,44,45]):

    answerJson = {}
    answerJson["Numara"] = {}
    answerJson["Numara"]["name"] = "Numara"
    answerJson["Numara"]["type"] = "label"
    answerJson["Numara"]["terms"] = {}

    for size in sizes:
        answerJson["Numara"]["terms"][str(size)] = {}
        answerJson["Numara"]["terms"][str(size)]["name"] = str(size)
        answerJson["Numara"]["terms"][str(size)]["color"] = ""
        answerJson["Numara"]["terms"][str(size)]["image"] = ""
        answerJson["Numara"]["terms"][str(size)]["show_tooltip"] = ""
        answerJson["Numara"]["terms"][str(size)]["tooltip_text"] = ""
        answerJson["Numara"]["terms"][str(size)]["tooltip_image"] = ""
        answerJson["Numara"]["terms"][str(size)]["image_size"] = ""

    json_data = json.dumps(answerJson)
    print(json_data)
    return json_data


def test():
    if(createSwatchAttributesJson() == correctAnswer):
        print(":::  DONE  :::")
    else:
        print("::: NOT YET  :::")

test()
#createSwatchAttributesJson()