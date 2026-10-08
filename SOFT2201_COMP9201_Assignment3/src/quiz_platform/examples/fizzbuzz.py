class FizzBuzzGenerator:
    def __init__(self, fizz_divisor=3, buzz_divisor=5):
        self.fizz_divisor = fizz_divisor
        self.buzz_divisor = buzz_divisor

    def get_value(self, number):
        if number % (self.fizz_divisor * self.buzz_divisor) == 0:
            return "FizzBuzz"
        elif number % self.fizz_divisor == 0:
            return "Fizz"
        elif number % self.buzz_divisor == 0:
            return "Buzz"
        else:
            return str(number)

    def generate(self, n):
        if n <= 0:
            return []

        result = []
        for i in range(1, n + 1):
            result.append(self.get_value(i))
        return result


def fizzbuzz(n):
    generator = FizzBuzzGenerator()
    return generator.generate(n)
