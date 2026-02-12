# Your task is to create a sentimental analysis tool using regular expressions (regex)
# The tool should analyze a given text and determine the sentiment (positive, negative, or neutral) based on certain
# patterns or keywords present in the text.
# Implement the function to perform sentimental analysis on the given text using regular expressions.
# Follow these steps within the function:
# a. Create a regex pattern to match positive sentiment keywords (e.g., "good," "great," "amazing," etc.).
# You can use the pipe (|) operator to specify multiple keywords in the pattern.
# b. Create another regex pattern to match negative sentiment keywords (e.g., "bad," "terrible," "awful," etc.).
# c. Use the re.findall() function to find all matches of positive and negative sentiment keywords in the text.
# d. Determine the sentiment based on the number of matches:

# If there are more positive matches than negative matches, return "Positive sentiment."
# If there are more negative matches than positive matches, return "Negative sentiment."
# If the number of positive and negative matches is the same, return "Neutral sentiment."
# Test your function with different text inputs to ensure it provides the correct sentiment analysis.
# example texts
# This movie is really good!
# I had a terrible experience.
# The weather is okay.
import re


def sentiment(text: str):
    """This program returns a positive, negative and neutral sentiment."""
    positivepattern = re.compile(r"(good|amazing|great)", flags=re.I)
    negativepattern = re.compile(r"(bad|terrible|awful)", flags=re.I)

    positivematch = positivepattern.findall(text)
    negativematch = negativepattern.findall(text)
    if len(positivematch) > len(negativematch):
        return "Positive Sentiment"
    elif len(negativematch) > len(positivematch):
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"


sentence = "This movie is really good!, very amazing but somehow bad"
sentence1 = "I had a terrible experience."
sentence2 = "The weather is okay"
print(sentiment(sentence))
print(sentiment(sentence1))
print(sentiment(sentence2))
