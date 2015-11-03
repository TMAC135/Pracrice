class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        if digits == " " or digits == None:
            return [1]
        val=0
        digit=1
        for i in range(len(digits)-1,-1,-1):
            val += digit*digits[i]
            digit *= 10

        digits_new = []
        val_new = val+1
        while val_new / 10 != 0:
            digits_new.append(val_new % 10)
            val_new = val_new / 10
        digits_new.append(val_new % 10)
        digits_new.reverse()
        return digits_new  