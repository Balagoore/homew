class Driver:
    def __init__(self, name, time1, time2):
        self.name = name
        self.time1 = time1
        self.time2 = time2

    def __str__(self):
        return f'{self.name}\n{self.time1}, {self.time1}, {self.time1}'


driver = Driver("Vasya", 1, 3)
print(driver)
