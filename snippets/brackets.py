import logging
import unittest
from parameterized import parameterized

logger = logging.getLogger('brackets_logger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
logger.addHandler(ch)

def check_paranthes(input):
    previous = ""
    while (len(input) != len(previous)):
        previous = input
        input = input.replace("()", "")
        input = input.replace("[]", "")
        input = input.replace("{}", "")

    if (len(input) == 0): return True
    else: return False


def check_brackets(bracket_string):

    logger.info ("bracket_string: %s " % bracket_string)

    lefters = ['(', '[', '{']
    righters = [')', ']', '}']
    index = 0

    while index < len(bracket_string):
        if bracket_string[index] in righters:
            if bracket_string[index - 1] == lefters[righters.index(bracket_string[index])]:
                bracket_string = bracket_string[:index - 1] + bracket_string[index + 1:]
                index = index - 2
            else:
                return False
        index = index + 1

    if len(bracket_string) == 0: return True
    else: return False

tested_strings = [
        ("()", True),
        (")", False),
        ("(()", False),
        ("([(({{[]}}))])", True),
        ("([([{{[]}}]({{[]}}))])", True),
        ("([()([{{[]}}]({{[]}}))])", True),
        ("{}[]([()([{{[]}}]({{[]}}))])", True),
        ("{}[]([()([{{[(])[]}}]({{[]}}))])", False)
    ]

class TestStringMethods(unittest.TestCase):

    @parameterized.expand(tested_strings)
    def test_brackets(self, str, expected):
        logger.info("str: \"{0}\", expected: {1}".format(str, expected))
        assert check_brackets(str) == expected

    @parameterized.expand(tested_strings)
    def test_paranthes(self, str, expected):
        logger.info("str: \"{0}\", expected: {1}".format(str, expected))
        assert check_paranthes(str) == expected


if __name__ == '__main__':
    unittest.main()

