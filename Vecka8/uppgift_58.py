# Ni skall nu använda list comprehensions för att arbeta med datan vi kan hämta från quiz-apiet
import requests
questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()['questions']

# Koden ovan hämtar alla frågor från apiet och lägger dom som en lista i variabeln questions. Ni skall nu:

# 1. Skriva en list comprehension som skapar en lista med alla prompter från frågorna.
# 2. Skriva en list comprehension som skapar en lista med alla prompter från frågorna där antalet gånger frågan ställts är över 500