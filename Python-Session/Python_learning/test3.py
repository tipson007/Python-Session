def food_r():
    if "food" in food_r:
        print("menu solid")
    else:
        print("nothing healthy")
user_inputs = input("enter food item: ")
print(user_inputs.upper())


def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
print(sentence_maker("how are you"))

result = []
while True:
    user_inputs = input("say something: ")
    if user_inputs == "\end" :
        break
    else:
        result.append(sentence_maker(user_inputs))
print(" ".join(result))