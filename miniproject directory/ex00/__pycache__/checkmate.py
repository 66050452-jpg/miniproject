def checkmate(board):
    # แปลง string เป็น list 2 มิติ
    grid = board.split("\n")
    size = len(grid)

    # หา King
    king_row = -1
    king_col = -1

    for i in range(size):
        for j in range(len(grid[i])):
            if grid[i][j] == "K":
                king_row = i
                king_col = j

    # ถ้าไม่มี King
    if king_row == -1:
        print("Fail")
        return

    # ----------------------------
    # ฟังก์ชันเช็คเดินเส้นตรง (Rook / Queen)
    # ----------------------------
    def check_straight(r, c):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dr, dc in directions:
            x = r
            y = c
            while True:
                x += dr
                y += dc

                # เช็คออกนอกกระดาน
                if x < 0 or x >= size or y < 0 or y >= size:
                    break

                # ถ้าเจอตัวอะไรบางอย่าง
                if grid[x][y] != ".":
                    if (x == king_row and y == king_col):
                        return True
                    break
        return False

    # ----------------------------
    # ฟังก์ชันเช็คทแยง (Bishop / Queen)
    # ----------------------------
    def check_diagonal(r, c):
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for dr, dc in directions:
            x = r
            y = c
            while True:
                x += dr
                y += dc

                if x < 0 or x >= size or y < 0 or y >= size:
                    break

                if grid[x][y] != ".":
                    if (x == king_row and y == king_col):
                        return True
                    break
        return False

    # ----------------------------
    # ฟังก์ชันเช็ค Pawn
    # ----------------------------
    def check_pawn(r, c):
        # Pawn โจมตีทแยงขึ้น
        if r - 1 >= 0 and c - 1 >= 0:
            if grid[r - 1][c - 1] == "K":
                return True

        if r - 1 >= 0 and c + 1 < size:
            if grid[r - 1][c + 1] == "K":
                return True

        return False

    # ----------------------------
    # วนดูทุกตัวในกระดาน
    # ----------------------------
    for i in range(size):
        for j in range(size):
            piece = grid[i][j]

            if piece == "P":
                if check_pawn(i, j):
                    print("Success")
                    return

            if piece == "R":
                if check_straight(i, j):
                    print("Success")
                    return

            if piece == "B":
                if check_diagonal(i, j):
                    print("Success")
                    return

            if piece == "Q":
                if check_straight(i, j) or check_diagonal(i, j):
                    print("Success")
                    return

    # ถ้าไม่มีใครกิน King ได้
    print("Fail")
