import random

# Fungsi untuk membuat board matrix
def create_board(width, height):
    return [['-' for _ in range(width)] for _ in range(height)]

# Fungsi untuk mencetak board
def print_board(board):
    for row in board:
        print(''.join(row))
    print()

# Fungsi untuk menghasilkan posisi acak bidak dan goals
def generate_positions(width, height):
    try:
        a_x = random.randint(0, width - 1)
        a_y = random.randint(0, height - 1)
        o_x = random.randint(0, width - 1)
        o_y = random.randint(0, height - 1)
        if (a_x, a_y) != (o_x, o_y):
            return a_x, a_y, o_x, o_y
        else:
            raise ValueError("Posisi bidak dan goals harus berbeda.")
    except ValueError as e:
        print(e)
        return generate_positions(width, height)

# Fungsi untuk memeriksa apakah pemain menang
def is_winning(board, a_x, a_y, o_x, o_y):
    return (a_x, a_y) == (o_x, o_y)

# Fungsi untuk memeriksa apakah pergerakan pemain valid
def is_valid_move(move, a_x, a_y, width, height):
    if move == 'w':
        return a_y > 0
    elif move == 's':
        return a_y < height - 1
    elif move == 'a':
        return a_x > 0
    elif move == 'd':
        return a_x < width - 1

# Fungsi utama permainan
def play_game():
    print("Selamat datang di permainan board game pemrograman fungsional ...")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)")
    print("Gunakan keyboard ASDW untuk bergerak")
    print("Selamat bermain ...")

    width = int(input("Enter the board width: "))
    height = int(input("Enter the board height: "))

    a_x, a_y, o_x, o_y = generate_positions(width, height)

    board = create_board(width, height)
    board[o_y][o_x] = 'O'
    board[a_y][a_x] = 'A'
    print("\nnew board generation")
    print_board(board)

    while True:
        move = input("New position generated (Y/N)? ").strip().lower()
        if move != 'y':
            break

        a_x, a_y, o_x, o_y = generate_positions(width, height)
        board = create_board(width, height)
        board[o_y][o_x] = 'O'
        board[a_y][a_x] = 'A'
        print_board(board)

    print("\nLet's play... This is your game board")
    print_board(board)

    while True:
        print("what is your move? (w/a/s/d)")
        move = input().strip().lower()
        if is_valid_move(move, a_x, a_y, width, height):
            if move == 'w':
                a_y -= 1
            elif move == 's':
                a_y += 1
            elif move == 'a':
                a_x -= 1
            elif move == 'd':
                a_x += 1

            board = create_board(width, height)
            board[o_y][o_x] = 'O'
            board[a_y][a_x] = 'A'
            print_board(board)

            if is_winning(board, a_x, a_y, o_x, o_y):
                print("you win")
                play_again = input("wanna try again? (y/n): ").strip().lower()
                if play_again != 'y':
                    break
                else:
                    a_x, a_y, o_x, o_y = generate_positions(width, height)
                    board = create_board(width, height)
                    board[o_y][o_x] = 'O'
                    board[a_y][a_x] = 'A'
                    print("\nnew board generation")
                    print_board(board)
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
