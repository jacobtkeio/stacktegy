

def apply_sentence(usrinput, gamestate):

    for word in usrinput:
        match word:
            case "rot":
                print("rot")
            case "+":
                print("+")
            case "q" | "quit" | "exit":
                exit(0)
