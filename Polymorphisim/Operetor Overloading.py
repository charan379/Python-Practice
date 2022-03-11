class marks:
    def __init__(self, telugu, maths, science):
        self.telugu = telugu
        self.maths = maths
        self.science = science
        self.total = self.telugu + self.maths + self.science

    # team score combined
    def __add__(self, *students):
        for student in students:
            self.telugu += student.telugu
            self.maths += student.maths
            self.science += student.science
            self.total += student.total
        return {'Telugu': self.telugu, 'Maths': self.maths, 'Science': self.science, 'Total': self.total}

    def studentTotal(self):
        self.total = self.telugu + self.maths + self.science
        return self.total



s1 = marks(10, 60, 60)
s2 = marks(60, 40, 60)

s3 = marks(10, 20, 60)
s4 = marks(10, 20, 60)

# team_score = (s1.m1+s2.m1) + (s1.m2+s2.m2)

# Team Can have any number of students
# team_score = marks.__add__(s1, s2, s3, s4)

team1_marks = marks.__add__(s1, s2)

team2_marks = marks.__add__(s3, s4)

print(team1_marks, '\n', team2_marks)

