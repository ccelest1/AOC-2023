class Solution:
    def read_first_and_last(self, input_f) -> int:
        def is_nums(char: str) -> bool:
            return ord("0") <= ord(char) <= ord("9")

        def get_sums(current_line: str) -> int:
            line_int = ""
            l, r = 0, len(current_line) - 1
            while l <= r:
                if not is_nums(current_line[l]):
                    l += 1
                else:
                    line_int += current_line[l]
                    break

                if not is_nums(current_line[l]):
                    r -= 1
                else:
                    line_int += current_line[r]
                    break
            if line_int.isdigit():
                return int(line_int)
            else:
                return 0

        with open(input_f, "r") as f1:
            total_sum = 0
            for line in f1:
                line_parse = line.strip().split()
                for word in line_parse:
                    total_sum += get_sums(word)
            return total_sum


Test = Solution()
print(Test.read_first_and_last("input.txt"))
