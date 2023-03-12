def str2tuple(p):
    return tuple((8 - int(p[1]), ord(p[0]) - 65))


def tuple2str(p):
    return chr(p[1] + 65) + str(8 - p[0])


move_direction = {"R": (0, 1), "L": (0, -1), "B": (1, 0), "T": (-1, 0),
                  "RT": (-1, 1), "LT": (-1, -1), "RB": (1, 1), "LB": (1, -1)}

king, stone, N = input().split()
king, stone = str2tuple(king), str2tuple(stone)

for i in range(int(N)):
    move = input()
    king_i = king[0] + move_direction[move][0]
    king_j = king[1] + move_direction[move][1]
    if 0 <= king_i < 8 and 0 <= king_j < 8:
        if stone == (king_i, king_j):
            stone_i = stone[0] + move_direction[move][0]
            stone_j = stone[1] + move_direction[move][1]
            if 0 <= stone_i < 8 and 0 <= stone_j < 8:
                king = (king_i, king_j)
                stone = (stone_i, stone_j)
        else:
            king = (king_i, king_j)

print(tuple2str(king))
print(tuple2str(stone))
