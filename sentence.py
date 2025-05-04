

def read_sentence(usrinput):
    usrinput = usrinput.lower()
    usrinput = usrinput.split(" ")

    for word in usrinput:
        match word:
            case "rot":
                print("rot")
            case "+":
                print("+")
