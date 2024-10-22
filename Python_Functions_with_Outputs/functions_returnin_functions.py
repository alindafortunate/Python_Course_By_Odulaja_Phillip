# A program about functions that return other functions.


# parent function
def greeting(lang: str):
    # child function
    def greetings(name: str) -> str:
        if lang == "english":
            return f"Hello, {name}"
        elif lang == "french":
            return f"Bonjour, {name}"
        elif lang == "spanish":
            return f"Hola, {name}"
        else:
            return f"Sorry, I don't know how to greet in {lang} "

    return greetings


your_name = input("What is your name: ")
language = input("Which language do you speak: ")

# greet = greeting(lang)
# print(greet(name))

# For simplicity
# What happens here is that,
greetOne = greeting(
    language
)  # Now greetOne is also a function since this function is returning another function
greetingOne = greetOne(your_name)  # Now here you see that greetOne is being called too
print(greetingOne)
