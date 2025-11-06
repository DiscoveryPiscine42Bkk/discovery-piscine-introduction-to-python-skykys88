def checkmate(board: str):

    # break board input string into rows + parse board string into rows + find board size (in string length)
    try:
        rows = board.strip().split("\n")
        size = len(rows)

        # verify board dimensions (chess is 8*8, which means that the board size should be a square in any size)
        if not all(len(row) == size for row in rows):
            print("Error")
            return

        # find king
        king_pos = None
        for r, row in enumerate(rows):
            for c, column in enumerate(row):
                if column == 'K':
                    if king_pos:
                        print("Error")  # in the case of repeated K input
                        return
                    king_pos = (r, c)

        if not king_pos:
            print("Error")  # no king
            return

        # helper script: check ranged threats
        # direction in row and column (dr, dc), 
        def check_direction(dr, dc, valid_pieces):
            r, c = king_pos
            while True:
                r += dr
                c += dc
                if r < 0 or c < 0 or r >= size or c >= size:
                    return False
                column = rows[r][c]
                if column == '.':
                    continue
                if column in valid_pieces:
                    return True
                else:
                    return False

        kr, kc = king_pos

        # pawn (upwards diagonal /// according to the instructions) PPPPPPP
        # logic checks if 
        for dr, dc in [(1, -1), (1, 1)]:
            r, c = kr + dr, kc + dc
            if 0 <= r < size and 0 <= c < size:
                if rows[r][c] == 'P':
                    print("Success")
                    return

        # define rook directions (vertical/horizontal) + queen (horizontal/vertical moves)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if check_direction(dr, dc, ['R', 'Q']):
                print("Success")
                return

        # define bishops directions (diagonal) + queen (diagonal moves)
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if check_direction(dr, dc, ['B', 'Q']):
                print("Success")
                return

        print("Fail")

    except Exception:
        # silent return for any undefined behaviour
        return
