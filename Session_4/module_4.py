PASSING_GRADE = 8


class Trainee:
    """Represents a trainee, tracking their attendance, tasks, and marks."""

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.mark = 0
        self.visited_lectures = 0
        self.done_home_tasks = 0
        self.missed_lectures = 0
        self.missed_home_tasks = 0

    def visit_lecture(self):
        self.visited_lectures += 1
        self.mark = min(10, self.mark + 1)

    def do_homework(self):
        self.done_home_tasks += 2
        self.mark = min(10, self.mark + 2)

    def miss_lecture(self):
        # Changed to addition because missed counts should increment
        self.missed_lectures += 1
        self.mark = max(0, self.mark - 1)

    def miss_homework(self):
        # Changed to addition because missed counts should increment
        self.missed_home_tasks += 2
        self.mark = max(0, self.mark - 2)

    def _add_points(self, points: int):
        self.mark += points

    def _subtract_points(self, points: int):
        self.mark -= points

    def is_passed(self) -> bool:
        if self.mark >= PASSING_GRADE:
            print("Good job!")
            return True

        needed = PASSING_GRADE - self.mark
        print(f"You need to get {needed} more points. Try to do your best!")
        return False

    def __str__(self) -> str:
        return (
            f"Trainee {self.name.title()} {self.surname.title()}:\n"
            f"done homework {self.done_home_tasks} points;\n"
            f"missed homework {self.missed_home_tasks} points;\n"
            f"visited lectures {self.visited_lectures} points;\n"
            f"missed lectures {self.missed_lectures} points;\n"
            f"current mark {self.mark};\n"
        )
