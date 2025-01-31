import requests
questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()['questions']
# Koden ovan hämtar hem alla frågor från APIet och sparar dom som en lista i variabeln questions.
#
# Ni skall nu skriva en dict comprehension som ger oss en dictionary där nyckeln är en frågas id och värdet är frågan själv. Så vi skall få fram något sådant här:
# Tänk på att konvertera id till en int
#
#
# {1: {'id': '1', 'prompt': 'Vilken funktion använder du för att skriva ut text i terminalen?', 'times_asked': '588', 'times_correct': '397', 'answers': [{'answer': 'print', 'correct': True}, {'answer': 'input', 'correct': False}, {'answer': 'import', 'correct': False}, {'answer': 'sys.exit', 'correct': False}]}
# 2: ....
# 3: ...
# }


r = {q['id']: q['prompt'] for q in questions}

for key, value in r.items():
    print(f'{key}: {value}')