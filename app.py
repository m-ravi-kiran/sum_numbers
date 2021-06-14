import sys


class Sum:
    """Sums n intergers"""

    def __init__(self, n=0):
        """Constructs a Sum object.
        Args:
            n: the number of intergers to be sumed.
        """
        self.n = n

    def sum_numbers(self, *args):
        """Sums all the intergers sent in the variable function argument
        Args:
            *args: All the integers to be summed.

        Returns: The final sum of integers
        """
        if not self.validate(*args):
            return
        return sum(self.get_teen(i) for i in args)

    def get_teen(self, x):
        """Checks if an integer is a teen and returns it's value.
        Args:
            x: integer to be checked

        Returns: teen value of the integer
        """
        x = int(x)
        if x in (15, 16):
            return x
        elif x in range(13, 20):
            return 0
        return x

    def is_num(self, x):
        """Validates if a variable is an integer.
        Args:
            x: variable to be checked

        Returns:
            True: if variable is integer.
            False: if variable is not an integer.
        """
        try:
            int(x)
        except ValueError:
            print('All inputs must be numeric')
            return False
        return True

    def validate(self, *args):
        """Validates the set of variable for summing.
        Args:
            *args: all the variables.

        Returns:
            True: if all the variables are valid
            False: if any of the variable is invalid.
        """
        if len(args) != self.n:
            print('Exactly 3 numbers are required')
            return False
        for i in args:
            if not self.is_num(i):
                return False
        return True


if __name__ == '__main__':
    args = sys.argv[1:]
    result = Sum(3).sum_numbers(*args)
    if result:
        print(result)
