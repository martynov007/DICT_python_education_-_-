import operator
from random import choice

class Test:
    mark = 0
    arithmetic_test_range = range(2, 10)
    square_test_range = range(11, 30)
    arithmetic_operation = {
        '+': operator.add,
        '*': operator.mul
    }

    def __init__(self) -> None:
        options = {
            1: self.arithmetic_test,
            2: self.square_test
        }
        levels = {
            1: '1 - simple operations with numbers 2-9',
            2: '2 - integral squares of 11-29'
        }

        choice_ = Validator.validate_input(
            'Choose a math level\n{}\n{}\nYour input: '.format(*levels.values()),
            range(1, 3),
            is_int=True)

        self.level = levels.get(choice_)
        math_test = options.get(choice_)
        math_test()

    def arithmetic_test(self):
        self.mark = 0

        for _ in range(5):
            self.get_random_values(self.arithmetic_test_range, 2)
            first_number, second_number = self.rand_numbers

            operation_list = list(self.arithmetic_operation.keys())
            operation_choice = choice(operation_list)
            rand_operation = self.arithmetic_operation.get(operation_choice)

            student_answer = Validator.validate_input(
                '{} {} {}\nYour answer is: '.format(
                    first_number, operation_choice, second_number),
                is_int=True)
            correct_answer = rand_operation(*self.rand_numbers)

            if student_answer == correct_answer:
                print('You\'r right!')
                self.mark += 1
            else:
                print('You\'r wrong!The answer was {}'.format(correct_answer))

        self.get_results()

    def square_test(self):
        for _ in range(5):
            self.get_random_values(self.square_test_range, 1)

            student_answer = Validator.validate_input(
                'Square the number {}\nYour answer is: '.format(self.rand_numbers),
                is_int=True)
            correct_answer = self.rand_numbers ** 2

            if student_answer == correct_answer:
                print('You\'r right!')
                self.mark += 1
            else:
                print('You\'r wrong!The answer was {}'.format(correct_answer))

        self.get_results()

    def get_random_values(self, numbers_range: list, rand_count):
        self.rand_numbers = []
        
        if rand_count == 1:
            self.rand_numbers = choice(numbers_range)

            return None

        for _ in range(rand_count):
            self.rand_numbers.append(choice(numbers_range))

    def get_results(self):
        choice_ = Validator.validate_input(
            'You mark is {} out of 5. Do you want to save your result? Enter yes(y) or no(n).: '.format(
                self.mark),
            ['yes', 'y', 'no', 'n'])

        if choice_ in ['yes', 'y']:
            name = input('What\'s your name?: ')
            with open('arithmetic-test/results.txt', mode='a') as f:
                f.write('\n{}: {}/5 in level {}'.format(
                    name,
                    self.mark,
                    self.level
                ))


class Validator:
    @staticmethod
    def validate_input(text, range=None, is_int=False):
        text = '\n' + text
        while True:
            try:
                if is_int:
                    result = int(input(text))
                else:
                    result = input(text)

                if range:
                    # * убираю регистрозависимость и случайные пробелы
                    if isinstance(result, str):
                        result = result.lower().strip()

                    if result in range:
                        return result
                    else:
                        print(
                            '\nIncorrect choice. There is no {} in the list.'.format(result))
                else:
                    return result

            except Exception:
                print('\nIncorrect format!')

if __name__ == "__main__":
    Test()