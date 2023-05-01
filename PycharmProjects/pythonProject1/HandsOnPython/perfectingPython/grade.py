def grade():  
    score = int(input("Enter a score: "))
    checker = ""
    if score >= 80:
        checker = "Your score is A"
        print(checker)
    elif score <80 and score >= 65:
        checker = "Your score is B"
        print(checker)
    elif score >=50 and score <65:
        checker = "Your score is C"
        print(checker)
    elif score > 40 and score < 50:
        checker = "Your score is D"
        print(checker)
    elif score <= 40:
        checker = "Ciroma Adekunle"
        print(checker)
    return checker
    

grade()
