class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, worker_income):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self.__income = worker_income
        self.full_wages = self.__income.get('wages') + self.__income.get('bonus')
        # print(wages)


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.full_wages




worker = Position('Остап', 'Бендер', 'Главный глава', {'wages': 20000, 'bonus': 5000})
print(worker.position)
print(worker.get_full_name())
print(worker.get_total_income())