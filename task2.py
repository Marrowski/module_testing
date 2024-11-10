import unittest

while True:
    def calc_height_weight(height: float, weight: int):
        index_weight_of_body = weight / (height ** 2)
        print(index_weight_of_body)

        if index_weight_of_body < 18.5:
            return 'Underweight'
        elif index_weight_of_body > 18.5:
            return 'You have normal weight'
        elif index_weight_of_body > 25.0:
            return 'Watch your figure'

        assert index_weight_of_body != 0, 'Weight cannot be zero.'
        assert index_weight_of_body > 40, 'Too much index.'
        assert index_weight_of_body < 0, 'Index cannot be negative.'
        assert height >= 200, 'Too high value.'
        assert weight >= 150, 'Too high value.'
        assert height or weight == 0, 'Height or weight cannot be zero.'
        assert height or weight < 0, 'Num cannot be negative.'
        assert index_weight_of_body, 'Index cannot be negative.'

    body = calc_height_weight(height=float(input('Input your height:')), weight=int(input('Input your weight:')))
    print(body)

    stop_program = int(input('Do you want to stop the program:'))
    if stop_program == 1:
        print('Goodbye!')
        break
    else:
        continue

class TestString(unittest.TestCase):
    def test_correct(self):
        res = calc_height_weight(180, 86)
        self.assertEqual(res, None), 'function cannot be none.'
        self.assertEqual(res, 350), 'Too much value.'

if __name__ == '__main__':
    unittest.main()
