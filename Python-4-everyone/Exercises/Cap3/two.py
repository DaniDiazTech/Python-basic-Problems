"""
Program that returns a grade from a score from 0, to 1.
The scale is:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""


class Score:
    def __init__(self, score):
        self.score = score

    def get_grade(self):
        try:
            correct_score = float(self.score)
            if 0 <= correct_score <= 1:
                if correct_score >= 0.9:
                    return "A"
                elif correct_score >= 0.8:
                    return "B"
                elif correct_score >= 0.7:
                    return "C"
                elif correct_score >= 0.6:
                    return "D"
                else:
                    return "F"
        except ValueError:
            return "Score must be a number"


def main():
    while True:
        score = input("Float score here >> ")
        my_score = Score(score)
        print(my_score.get_grade())


if __name__ == "__main__":
    main()
