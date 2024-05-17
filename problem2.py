class Solution_2:

    @staticmethod
    def check_parentheses(strings: list) -> list:
        result_list = []

        for text in strings:
            stack_indices = []

            #init marks
            marks = []
            text_length = len(text)

            for _ in range(text_length):
                marks.append(' ')

            #start check
            for index, char in enumerate(text):
                if char == '(':
                    stack_indices.append(index)
                elif char == ')':
                    if stack_indices and text[stack_indices[-1]] == '(':
                        stack_indices.pop()
                    else:
                        marks[index] = '?'

            while stack_indices:
                position = stack_indices.pop()
                marks[position] = 'x'

            result_list.append(''.join(marks))

        return result_list


if __name__ == '__main__':

    input_strings = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]

    output = Solution_2.check_parentheses(input_strings)


    for i in range(len(input_strings)):
        print(input_strings[i])
        print(output[i])