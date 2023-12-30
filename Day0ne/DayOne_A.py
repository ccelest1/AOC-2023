class Solution:
    def read_first_and_last(self, input_f) -> int:
        def is_nums(char: str) -> bool:
            return ord("0") <= ord(char) <= ord("9")

        def extract_nums(line: str) -> bool:
            str = ""
            integers = [int(char) for char in line if is_nums(char)]
            if len(integers) == 1:
                str = (integers[0] * 10) + integers[0]
            else:
                str = (integers[0] * 10) + integers[-1]
            return str

        total_sum = 0
        with open(input_f, "r") as f1:
            for line in f1:
                total_sum += extract_nums(line)
        return total_sum

    def read_first_last_strsIncluded(self, input_f: str) -> int:
        def is_nums(char: str) -> bool:
            return ord("0") <= ord(char) <= ord("9")

        def extract_nums_and_strings(line: str) -> bool:
            str = ""
            conversion = {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
            }
            integers = []
            for char in line:
                for key in conversion.keys():
                    if key in line:
                        integers.append(conversion[key])
                if is_nums(char):
                    integers.append(int(char))
            # integers = [int(char) for char in line if is_nums(char)]
            if len(integers) == 1:
                line_str = (integers[0] * 10) + integers[0]
            else:
                line_str = (integers[0] * 10) + integers[-1]
            print(line_str)
            return line_str

        total_sum = 0
        with open(input_f, "r") as f1:
            for line in f1:
                total_sum += extract_nums_and_strings(line)
        return total_sum


Test = Solution()
print(Test.read_first_and_last("input.txt"))
print(Test.read_first_last_strsIncluded("input.txt"))
