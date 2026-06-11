PASSING_GRADE = 8


class Trainee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.visited_lectures = 0
        self.missed_lectures = 0
        self.done_home_tasks = 0
        self.missed_home_tasks = 0
        self.mark = 0

    def visit_lecture(self):
        self.visited_lectures += 1
        self._add_points(1)

    def do_homework(self):
        self.done_home_tasks += 2
        self._add_points(2)

    def miss_lecture(self):
        self.missed_lectures -= 1
        self._subtract_points(1)

    def miss_homework(self):
        self.missed_home_tasks -= 2
        self._subtract_points(2)

    def _add_points(self, pts: int):
        if self.mark + pts > 10:
            self.mark = 10
        else:
            self.mark += pts

    def _subtract_points(self, pts):
        if self.mark - pts < 0:
            self.mark = 0
        else:
            self.mark -= pts

    def is_passed(self):
        gap = PASSING_GRADE - self.mark
        if gap <= 0:
            print("Good job!")
        else:
            print(f"You need to get {gap} more points. Try to do your best!")

    def __str__(self):
        status = (
            f"Trainee {self.name.title()} {self.surname.title()}:\n"
            f"done homework {self.done_home_tasks} points;\n"
            f"missed homework {self.missed_home_tasks} points;\n"
            f"visited lectures {self.visited_lectures} points;\n"
            f"missed lectures {self.missed_lectures} points;\n"
            f"current mark {self.mark};\n"
        )
        return status
