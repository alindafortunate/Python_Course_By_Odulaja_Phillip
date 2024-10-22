def create_multiplier(factor: int):
    def multiplier(n: int):
        return n * factor

    return multiplier


double = create_multiplier(3)
print(double(2))
tripple = create_multiplier(5)
print(tripple(3))


def greeting(lang: str):
    def greetings(name: str):
        if lang == "English":
            return f"Hello {name}"
        elif lang == "Spanish":
            return f"Hola {name}"
        else:
            return f"Oh {name}, sorry I can't greet in {lang}"

    return greetings


language = input("Which language do you speek: ")
your_name = input("What is your name: ")

greetingOne = greeting(language)

print(greetingOne(your_name))
