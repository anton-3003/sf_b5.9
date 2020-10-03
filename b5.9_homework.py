import time

class Repeater():
    # Передаем кол-во проходов, default - 5
    def __init__(self, num_runs=5):
        self.num_runs = num_runs
    # принимаем ф-цию для оборачивания, как арг-т декоратора
    def __call__(self, func):
        def wrapper():
            begin_run = time.time()
            print("==> Начали оболочку <==")
            for _ in range(self.num_runs):
                func()
            print("==> Закончили оболочку <==")
            finish_run = time.time()

            diff_time = (finish_run - begin_run)
            diff_time /= self.num_runs

            print("Время работы - %.5f сек." % diff_time)
        return wrapper

# объект класса; в аргумент передается кол-во проходов
repeater = Repeater(12)

@repeater
def work_function():
    print("Выполнение основной функции")

work_function()