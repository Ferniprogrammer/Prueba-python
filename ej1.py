board = [
    [5, 0, 0, 0, 4, 0, 0, 0 ,9],
    [0, 2, 0, 0, 1, 0, 6, 8, 0],
    [0, 0, 9, 8, 7, 0, 1, 0, 0],
    [0,0, 6, 7, 0, 0, 2, 0, 0],
    [0, 9, 0, 3, 5, 4, 0, 6, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 1],
    [9, 0, 0, 0, 6, 0, 0, 0, 2],
    [0, 1, 4, 0, 3, 0, 0, 5, 7],
    [0, 0, 5, 0, 8, 7, 0, 0, 0],
]

def print_board(board):
    for l in board:
        print(l)

def encontrar_coordenada_grid(val):
    if val <= 2:
        return 0
    elif val <= 5:
        return 1
    else:
        return 2

def obtener_grid_para_celda(x, y, board):
    subgrid_col = encontrar_coordenada_grid(x)
    subgrid_row = encontrar_coordenada_grid(y)
    
    grid = []
    for fila in board[subgrid_row *3: subgrid_row *3 + 3]:
        for col in fila[subgrid_col *3: subgrid_col *3 + 3]:
            grid.append(col)
            
    return grid


def es_posible(x, y, v, board):
    if v in board[y]:
        return False
    col = [fila[x] for fila in board]
    if v in col:
        return False
    grid3x3 = obtener_grid_para_celda(x, y, board)
    if v in grid3x3:
        return False
    return True


def resolver_board(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for valor in range(1,10):
                    if es_posible(x, y, valor, board):
                        board[y][x] = valor
                        resolver_board(board)
                        board[y][x] = 0
                return
    print_board(board)
    return

            
resolver_board(board)
