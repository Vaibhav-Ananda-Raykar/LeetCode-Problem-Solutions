class Solution(object):
    def plusOne(self, digits):
        number = 0
        for i in range(len(digits)):
            number = number * 10 + digits[i]
        number += 1

        digits = list(str(number))
        digits = [int(d) for d in digits]

        return digits