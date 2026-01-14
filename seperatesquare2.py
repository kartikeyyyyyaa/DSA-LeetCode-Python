class Solution:
    def separateSquares(self, squares):
        def union_area(limit_y=None):
            events = []
            for x, y, l in squares:
                y1 = y
                y2 = y + l
                if limit_y is not None:
                    if y1 >= limit_y:
                        continue
                    y2 = min(y2, limit_y)
                events.append((y1, 1, x, x + l))
                events.append((y2, -1, x, x + l))

            events.sort()
            active = []
            prev_y = None
            area = 0.0

            def x_union():
                if not active:
                    return 0
                active.sort()
                total = 0
                cur_l, cur_r = active[0]
                for l, r in active[1:]:
                    if l > cur_r:
                        total += cur_r - cur_l
                        cur_l, cur_r = l, r
                    else:
                        cur_r = max(cur_r, r)
                total += cur_r - cur_l
                return total

            for y, typ, x1, x2 in events:
                if prev_y is not None and y > prev_y:
                    area += x_union() * (y - prev_y)
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                prev_y = y

            return area

        total = union_area()

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):
            mid = (low + high) / 2
            below = union_area(mid)
            if below * 2 < total:
                low = mid
            else:
                high = mid

        return low
