class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()

        def max_consecutive(arr):
            mx = 1
            cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                    mx = max(mx, cur)
                else:
                    cur = 1
            return mx + 1

        max_h = max_consecutive(hBars)
        max_v = max_consecutive(vBars)

        side = min(max_h, max_v)
        return side * side
