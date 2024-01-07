PASSING_GRADE = 8


class Trainee:
    def __init__(self, name, surname):
        pass

    def visit_lecture(self):
        pass

    def do_homework(self):
        pass

    def miss_lecture(self):
        pass

    def miss_homework(self):
        pass

    def _add_points(self, points: int):
        pass

    def _subtract_points(self, points):
        pass

    def is_passed(self):
        pass

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
