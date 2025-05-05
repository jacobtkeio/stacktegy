def expand_words(words, usrinput):
    for i in range(len(usrinput)):
        for j in range(len(words)):
            if usrinput[i] == words[j].split(' ')[1]:
                return usrinput[:i] + expand_words(words, (words[j]).split(' ')[2:]) + expand_words(words, usrinput[1+i:])
    return usrinput

def define(usrinput, gamestate):
    (words, stack1, stack2, stack3, stack4) = gamestate

    if len(usrinput) >= 2:
       words.insert(0, ' '.join(usrinput))
       return

def execute(usrinput, gamestate):
    (words, stack1, stack2, stack3, stack4) = gamestate

    usrinput = usrinput[1:] # remove '!'
    usrinput = expand_words(words, usrinput)

    for word in usrinput:
        match word:
            case "diag":
                temp = stack1[0]
                stack1[0] = stack2[1]
                stack2[1] = stack3[2]
                stack3[2] = stack4[3]
                stack4[3] = temp
            case "top":
                temp = stack1[0]
                stack1[0] = stack2[0]
                stack2[0] = stack3[0]
                stack3[0] = stack4[0]
                stack4[0] = temp
            case "rot":
                stack1.insert(0, stack1.pop())
                stack2.insert(0, stack2.pop())
                stack3.insert(0, stack3.pop())
                stack4.insert(0, stack4.pop())
            case _:
                break

def apply_sentence(usrinput, gamestate):
    (words, stack1, stack2, stack3, stack4) = gamestate

    if usrinput[0] == ":":
        define(usrinput, gamestate)
        return

    if usrinput[0] == "!":
        execute(usrinput, gamestate)
        return

    if usrinput[0] == "q" or usrinput[0] = "quit" or usrinput[0] = "exit":
        exit(0)

    print("invalid sentence")

