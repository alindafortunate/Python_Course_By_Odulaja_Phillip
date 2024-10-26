# A program to see how inheritance works where by a class inheritance methods of the parent class.


class Speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def power_on(self):

        print(
            f"Press the power button for powering on {self.color} {self.model} speaker."
        )

    def power_off(self):
        print(f"Powering off {self.color} {self.model} speaker.")


class SmartSpeaker(Speaker):
    def __init__(self, color, model, voice_assistant):
        super().__init__(color, model)
        self.voice_assistant = voice_assistant

    def say_hello(self):
        print(f"Hello, I am {self.voice_assistant}")

    def power_on(self, button):
        super().power_on()
        self.button = button
        print(f"For me to power on, press {self.button} button")

    def power_off(self):
        print(f"I am powering of by {self.voice_assistant}")


# creating objects.
speaker_one = Speaker("red", "XYB001")
# speaker_one.power_on()
# speaker_one.power_off()

smartSpeaker_one = SmartSpeaker("black", "YXZ02", "Alexa")
smartSpeaker_one.say_hello()
smartSpeaker_one.power_on("On")
smartSpeaker_one.power_off()
