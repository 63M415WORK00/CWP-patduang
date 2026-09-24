def check_error(board):
    count_error = 0
    count_K = 0
    for i in range(0,len(board),1):
        if abs(len(board[i])-len(board)) >= 1:
            count_error += 1
    for row in board:
        for col in row:
            if col == "K":
                count_K += 1
    if count_K != 1:
        count_error += 1
    return count_error

def crerate_board(board):
    board_spl = []
    rows = board.splitlines()
    for i in rows:
        i = i.strip().replace("\\","")
        if i != "":
            board_spl.append(list(i))
    return board_spl

def block(board, row1, col1, rowK, colK):
    if row1 == rowK:
        direct_row = 0
    else:
        if rowK > row1:
            direct_row = 1
        else:
            direct_row = -1

    if col1 == colK:
        direct_col = 0
    else:
        if colK > col1:
            direct_col = 1
        else:
            direct_col = -1
    
    row = row1 + direct_row
    col = col1 + direct_col

    while (row, col) != (rowK, colK):
        if board[row][col] in ["R","P","B","Q","K"]:
            return False
        row += direct_row
        col += direct_col
    return True


def checkmate(board):
    board_spl = crerate_board(board)
    if check_error(board_spl) >= 1:
        print("Error")
        return
    
    # 1. เปลี่ยนตำแหน่งเป็น List เพื่อรองรับหมากซ้ำหลายตัว
    positions = {
    "r": [],"p": [],"b": [],"q": [],"k": None
    }

    have = {
    "r": 0,"p": 0,"b": 0,"q": 0,"k": 0
    }

    sus = 0

    # 2. วนลูปเก็บพิกัดแบบ .append() ไม่ให้โดนทับ
    for i in range(0,len(board_spl),1):
        for j in range(0,len(board_spl[i]),1):
            if board_spl[i][j] in ["R","P","B","Q","K"]:
                if board_spl[i][j] == "R":
                    have["r"] += 1
                    positions["r"].append((i,j))
                elif  board_spl[i][j] == "P":
                    have["p"] += 1
                    positions["p"].append((i,j))
                elif  board_spl[i][j] == "B":
                    have["b"] += 1
                    positions["b"].append((i,j))
                elif  board_spl[i][j] == "Q":
                    have["q"] += 1
                    positions["q"].append((i,j))
                elif  board_spl[i][j] == "K":
                    have["k"] += 1
                    positions["k"] = (i,j)
                    
    k_pos = positions["k"]

    # 3. ใช้ลูปเช็คตัวหมากแต่ละประเภททีละตัวใน List
    if have["p"] > 0 and k_pos is not None:  
        for p_pos in positions["p"]:
            if abs(p_pos[1] - k_pos[1]) == 1 and p_pos[0] - k_pos[0] == 1:
                sus += 1
            
    if have["b"] > 0 and k_pos is not None:
        for b_pos in positions["b"]:
            if abs(b_pos[0] - k_pos[0]) == abs(b_pos[1] - k_pos[1]) \
                and block(board_spl, b_pos[0], b_pos[1], k_pos[0], k_pos[1]):
                sus += 1
            
    if have["r"] > 0 and k_pos is not None:
        for r_pos in positions["r"]:
            if ((r_pos[0] == k_pos[0]) or (r_pos[1] == k_pos[1])) \
                and block(board_spl, r_pos[0], r_pos[1], k_pos[0], k_pos[1]):
                sus += 1
            
    if have["q"] > 0 and k_pos is not None:
        for q_pos in positions["q"]:
            if (q_pos[0] == k_pos[0] or q_pos[1] == k_pos[1] \
                or abs(q_pos[0] - k_pos[0]) == abs(q_pos[1] - k_pos[1])) \
            and block(board_spl, q_pos[0], q_pos[1], k_pos[0], k_pos[1]):
                sus += 1

    if sus >= 1:
        print("Success")
    else:
        print("Fail")