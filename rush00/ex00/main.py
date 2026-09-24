from checkmate import checkmate
def main():
    board = """\
    .....
    KPPPR
    .....
    .....
    .....\
    """
    checkmate(board)
    board = """\
    ..
    .K\
    """
    checkmate(board)
    print("------------")
    board = """\
    R...
    .K..
    ..P.
    ....\
    """
    checkmate(board)
    board = """\
    R...
    .K..
    .P..
    ....\
    """
    checkmate(board)
    board = """\
    R...
    .K.....
    ..P.
    ....\
    """
    checkmate(board)

    board = """\
    R...
    .K..
    ..K.
    ....\
    """
    checkmate(board)

    board = """\
     R...
    ....
    ..P.
    ....\
    """
    checkmate(board)
    
    board = """\
    R.B.Q
    .....
    .K...
    .....
    P....\
    """
    checkmate(board)
   
if __name__ == "__main__":
    main()