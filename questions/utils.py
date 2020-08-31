# def get_score():
#     if option_one.ANSWER_SELECTOR is ANSWER:
#         return self.score = 5

#     elif self.option_two.ANSWER_SELECTOR is ANSWER:
#         return self.score = 5
        
#     elif self.option_three.ANSWER_SELECTOR is ANSWER:
#         return self.score = 5
        
#     elif self.option_four.ANSWER_SELECTOR is ANSWER:
#         return self.score = 5

#     else:
#         return 'Invalid Response'

def get_average(self):
    while self.count <= self.max_question:
        count = count + 1
        total_score = total_score + self.score

    max_score = 50
    average = total_score / max_score

    return average

def get_grade(self):
    if get_average.average < 0.75:
        return 'Fail'

    elif get_average.average >= 0.75 and <= 100:
        return 'Pass'

    else: 
        return 'Invalid Score' 