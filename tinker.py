import time


class TinkerTailor:

    @staticmethod
    def counting_out(n, k):
        children_list = list(range(1, n+1))
        k -= 1
        out = k
        while len(children_list) != 1:
            children_list.pop(out)
            out = (out + k) % len(children_list)
        print("winner:", children_list[0])


if __name__ == "__main__":
    start = time.time()
    game = TinkerTailor()
    game.counting_out(5, 3)
    print("Runtime: ", time.time() - start)
