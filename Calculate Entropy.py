#Calculate Entropy

class Solution(object):
    def calculateEntropy(self, input):
        """
        :type input: List[int]
        :rtype: float
        """
        set_of_numbers = set(input)

        entropy = 0.0

        for num in set_of_numbers:
            occurences = input.count(num)
            probability = float(occurences) / len(input)
            if probability != 0:
                entropy += -probability * math.log(probability, 2)

        return entropy