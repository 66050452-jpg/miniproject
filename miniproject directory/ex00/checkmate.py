def checkmate(board):
    
    if isinstance(board, str):
        board = board.splitlines()

    grid = [row.strip() for row in board if row.strip()]

    if not grid:
        print("Fail")
        return

    rows = len(grid)
    cols = len(grid[0])

    
    for row in grid:
        if len(row) != cols:
            print("Fail")
            return


    # King

    king_positions = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "K":
                king_positions.append((i, j))

    if len(king_positions) != 1:
        print("Fail")
        return


    def check_straight(i, j):
        
        x = i - 1
        while x >= 0:
            if grid[x][j] == "K":
                return True
            if grid[x][j] != ".":
                break
            x -= 1

        
        x = i + 1
        while x < rows:
            if grid[x][j] == "K":
                return True
            if grid[x][j] != ".":
                break
            x += 1

        
        y = j - 1
        while y >= 0:
            if grid[i][y] == "K":
                return True
            if grid[i][y] != ".":
                break
            y -= 1

        
        y = j + 1
        while y < cols:
            if grid[i][y] == "K":
                return True
            if grid[i][y] != ".":
                break
            y += 1

        return False


    def check_diagonal(i, j):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            while 0 <= x < rows and 0 <= y < cols:
                if grid[x][y] == "K":
                    return True
                if grid[x][y] != ".":
                    break
                x += dx
                y += dy

        return False


    def check_pawn(i, j):
        
        if i - 1 >= 0:
            if j - 1 >= 0 and grid[i - 1][j - 1] == "K":
                return True
            if j + 1 < cols and grid[i - 1][j + 1] == "K":
                return True

        
        if i + 1 < rows:
            if j - 1 >= 0 and grid[i + 1][j - 1] == "K":
                return True
            if j + 1 < cols and grid[i + 1][j + 1] == "K":
                return True

        return False

 
    for i in range(rows):
        for j in range(cols):
            piece = grid[i][j]

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

            if piece == "P":
                if check_pawn(i, j):
                    print("Success")
                    return

    print("Fail")
