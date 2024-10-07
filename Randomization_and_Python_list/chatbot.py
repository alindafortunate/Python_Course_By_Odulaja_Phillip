# A program that works like a chatbot.
import random

print("Welcome to my first chatbot program!")

conversation = [
    "Hello",
    "How are you doing?",
    "Hey",
    "How is your day",
    "Hello, talk to you later",
    "Wasssup",
    "Be right back",
]
# Step1: Print a welcome message.
print(
    "Hello I am a chatbot... ",
    end="",
)
# Step2: Prompt the user for a response.
user_interaction = input("\n")

# Step3: Prompt the random response from the bot.
chatbot_reply = random.choice(conversation)

# Step4: Check if the responses are the same and generate a new one.
if chatbot_reply.lower() == user_interaction.lower():
    print(random.choice(conversation))
else:
    print(chatbot_reply)
