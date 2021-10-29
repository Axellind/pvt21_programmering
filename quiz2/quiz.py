import requests
import math

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Answer:
    # Implementera klassen Answer
    # Vilka attribut skall den ha
    # Vilka metoder behöver vi?
    def __init__(self, answer, correct):
        self.answer = answer
        self.correct = correct
    pass



class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list
    # answers: list[Answer]

    def __init__(self, id_, prompt, times_asked, times_correct, answers):
        self.id = int(id_)
        self.prompt = prompt
        self.times_asked = int(times_asked)
        self.times_correct = int(times_correct)
        self.answers = [Answer(i['answer'], i['correct']) for i in answers]


    def percent_correct(self) -> int:
        # ex: "34%"
        return int(round((self.times_correct/self.times_asked) * 100))
        #return (self.times_correct * 100) // self.times_asked
        pass

    def print_answers(self):
        r = []
        for a in self.answers:
            print(a.answer)





"Fråga 10. [34% har svarat rätt] Vad är en int?"

ex_q = {'id': '1',
        'prompt': 'Vilken funktion använder du för att skriva ut text i terminalen?',
        'times_asked': '35',
        'times_correct': '16',
        'answers':
            [{'answer': 'print',
              'correct': True},
             {'answer': 'input',
              'correct': False},
             {'answer': 'import',
              'correct': False},
             {'answer': 'sys.exit',
              'correct': False}]}


def get_questions():
    # Hämta frågor från API
    # ta varje fråga och läs in som instans av question
    # lägg till i en lista
    # returnera lista
    res = []
    response = requests.get(QUIZ_URL)
    #print(response.json())
    for q in response.json()['questions']:
        fråga = Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], q['answers'])
        res.append(fråga)
    return res


def parse_question(q) -> Question:
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], q['answers'])

if __name__ == '__main__':
    question = parse_question(ex_q)

    for q in get_questions():
        print(f'{q.prompt} [{q.percent_correct()}% Har svarat rätt på den här frågan]')
        print(q.print_answers())
        print('-'*80)


    # print(question.prompt)
    # print(type(question.id))
    # print(type(question))
    # print(question)
    # print(question.percent_correct())

    # res = get_questions()
    # print(res.json())
    # questions = res.json()
    #
    # print(questions['questions'][0]['prompt'])
