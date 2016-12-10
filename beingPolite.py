def be_polite(sentences):
    if sentences[-1] == "?" and "please" not in sentences:
        #return sentences[:-1] + "please?"
        print(sentences[:-1] + " please?")
    elif sentences[:-7] == "please?":
        #return sentences
        print(sentences)
    else:
        #return sentences
        print(sentences)

be_polite("May I borrow your pencil?")