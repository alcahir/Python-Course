PASSING_GRADE = 8


class Trainee:
    """
    0 as a beggining value of attributes, as a start for further calculations
    """
    def __init__(self,
                name,
                surname,
                visited_lectures = 0,
                done_home_tasks =0,
                missed_lectures =0,
                missed_home_tasks = 0,
                mark = 0 ):
        self.name = name
        self.surname = surname
        self.visited_lectures = visited_lectures
        self.done_home_tasks = done_home_tasks
        self.missed_lectures = missed_lectures
        self.missed_home_tasks =missed_home_tasks
        self.mark = mark


    def visit_lecture(self):
        """
        This method adds one to the value of attribute representing visited lectures. Also calls method used to calculate a mark.
        """
        self.visited_lectures += 1
        self._add_points(1)

    def do_homework(self):
        """
        This method adds two to the value of attribute representing done home tasks. Also calls method used to calculate a mark.
        """
        self.done_home_tasks += 2
        self._add_points(2)

    def miss_lecture(self):
        """
        This method subtracts one from the value of attribute representing visited lectures. Also calls method used to calculate a mark.
        """
        self.missed_lectures -=1
        self._subtract_points(1)

    def miss_homework(self):
        """
        This method subtracts two from the value of attribute representing done homeworks. Also calls method used to calculate a mark.
        """
        self.missed_home_tasks -=2
        self._subtract_points(2)

    def _add_points(self, points: int):
        """
        This method adds points to the value of attribute representing mark. It has a max value of mark set as 10, if calculated mark is higher, it sets it to 10.
        """
        self.mark += points
        if self.mark > 10:
            self.mark = 10

    def _subtract_points(self, points):
        """
        This method subtracts points from the value of attribute representing mark. It has a min value of mark set as 0, if calculated mark is lower, it sets it to 0.
        """
        self.mark -= points
        if self.mark < 0:
            self.mark = 0

    def is_passed(self):
        """
        This method prints and returns result of a course, based on calculated mark.
        """
        if self.mark >= 8:
            print("Good job!")
            return "Good job!"
        else:
            print(f'You need to {PASSING_GRADE - self.mark} points. Try to do your best!')
            return f'You need to {PASSING_GRADE - self.mark} points. Try to do your best!'


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
