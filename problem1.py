class Solution_1:

    @staticmethod
    def shortestway(source: str, target: str) -> int:
        result = 0
        j = 0
        source_size = len(source)
        target_size = len(target)

        while j < target_size:
            pre = j
            for i in range(source_size):
                if j < target_size and source[i] == target[j]:
                    j += 1
            if j == pre:
                return -1
            result += 1

        return result


if __name__ == '__main__':
    source1, target1 = "abc", "abcbc"
    source2, target2 = "abc", "acdbc"
    source3, target3 = "xyz", "xzyxz"

    print(Solution_1.shortestway(source1, target1))
    print(Solution_1.shortestway(source2, target2))
    print(Solution_1.shortestway(source3, target3))
