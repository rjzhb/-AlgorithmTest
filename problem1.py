class Solution_1:

    @staticmethod
    def shortestWay(source: str, target: str) -> int:
        res = 0
        j = 0
        m = len(source)
        n = len(target)

        while j < n:
            pre = j
            for i in range(m):
                if j < n and source[i] == target[j]:
                    j += 1
            if j == pre:
                return -1
            res += 1

        return res


if __name__ == '__main__':
    source1, target1 = "abc", "abcbc"
    source2, target2 = "abc", "acdbc"
    source3, target3 = "xyz", "xzyxz"

    print(Solution_1.shortestWay(source1, target1))
    print(Solution_1.shortestWay(source2, target2))
    print(Solution_1.shortestWay(source3, target3))
