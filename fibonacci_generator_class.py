class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield self.b
            self.a, self.b = self.b, self.a + self.b

fibonacci_list = Fibonacci(0, 1)

for i in fibonacci_list.series():
    if i > 100:
        break
    print(i, end=' ')