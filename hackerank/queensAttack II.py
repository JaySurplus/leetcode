# Complete the extraLongFactorials function below.
import time


def queensAttack(n, k, r_q, c_q, obstacles):
    res = 0  # + min(r_q - 1, c_q - 1) + min(n-r_q,
    #                            c_q-1) + min(n-c_q, r_q-1) + min(n - r_q, n - c_q)
    visited = set()
    dic = {
        "right": n - c_q,
        "left": c_q - 1,
        "up": r_q - 1,
        "down": n - r_q,
        "up_right": min(n-c_q, r_q-1),
        "up_left": min(r_q-1, c_q-1),
        "down_right": min(n-r_q, n-c_q),
        "down_left": min(n-r_q, c_q-1)
    }

    for x, y in obstacles:
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x == r_q:
            if y > c_q:
                dic["right"] = min(dic["right"], y-c_q-1)
            else:
                dic["left"] = min(dic["left"], c_q-y-1)

            continue
        if y == c_q:
            if x > r_q:
                dic["down"] = min(dic["down"], x - r_q - 1)
            else:
                dic["up"] = min(dic["up"], r_q - x - 1)
            continue
        if x - r_q == y - c_q or x - r_q == c_q - y:
            if x > r_q and y > c_q:
                dic["down_right"] = min(dic["down_right"], x - r_q - 1)
            if x > r_q and y < c_q:
                dic["down_left"] = min(dic["down_left"], x - r_q - 1)
            if x < r_q and y > c_q:
                dic["up_right"] = min(dic["up_right"], y - c_q - 1)
            if x < r_q and y < c_q:
                dic["up_left"] = min(dic["up_left"], r_q - x - 1)

    for k, v in dic.items():
        res += v
    return res


if __name__ == '__main__':
    n = 1
    k = 0
    r_q = 1
    c_q = 1
    print(queensAttack(n, k, r_q, c_q, []))

    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [(5, 5), (4, 2), (2, 3)]
    print(queensAttack(n, k, r_q, c_q, obstacles))

    n = 88587
    k = 9
    r_q = 20001
    c_q = 20003

    obstacles = [(20001, 20002),
                 (20001, 20004),
                 (20000, 20003),
                 (20002, 20003),
                 (20000, 20004),
                 (20000, 20002),
                 (20002, 20004),
                 (20002, 20002),
                 (564, 323)]
    print(queensAttack(n, k, r_q, c_q, obstacles))
