def main():
    """Main function to interact with the user and manage game logic."""
    print("Choose a white piece from pawn or rook along with its coordinates: ")

    while True:
        # Prompt user for white piece input
        white_piece = input("Enter: ").strip().lower().split()

        # Validate white piece input
        if len(white_piece) == 2 and is_valid_piece(white_piece[0]) and is_valid_position(white_piece[1]):
            white_type = white_piece[0]
            white_position = white_piece[1]
            print(f"White piece {white_type} at {white_position} added successfully.")
            break
        else:
            print("Invalid input for white piece. Please try again.")

    black_pieces = []
    add_black_pieces(black_pieces, white_position)

    can_take = determine_takeable_pieces(white_type, white_position, black_pieces)

    if can_take:
        print(f"White {white_type} at {white_position} can capture the black pieces at:")
        for piece in can_take:
            print(f"  - {piece[0]} at {piece[1]}")
    else:
        print(f"The white {white_type} cannot take any black pieces.")

def is_valid_piece(piece):
    return piece in ["pawn", "rook"] #    Check if the piece is a valid type ('pawn' or 'rook').

def is_valid_position(position):
    """Check if the position is valid in chess notation (e.g., 'a1', 'h8')."""
    return len(position) == 2 and position[0] in 'abcdefgh' and position[1] in '12345678'

def add_black_pieces(black_pieces, white_position):
    """Prompt user to add black pieces and validate their input."""
    while len(black_pieces) < 16:
        entry = input("Enter black piece or 'done' once you finish: ").strip().lower()
        if entry == "done":
            if black_pieces:
                break
            else:
                print("At least one black piece must be added.")
                continue

        piece_info = entry.split()
        if len(piece_info) != 2 or not is_valid_piece(piece_info[0]) or not is_valid_position(piece_info[1]):
            print("Invalid input format for black piece.")
            continue

        if piece_info[1] == white_position or any(piece_info[1] == bp[1] for bp in black_pieces):
            print("This position is already filled. Please choose another position.")
            continue

        black_pieces.append((piece_info[0], piece_info[1]))
        print(f"Black piece {piece_info[0]} at {piece_info[1]} added successfully.")

    if len(black_pieces) >= 16:
        print("Maximum limit of 16 pieces reached.")

def determine_takeable_pieces(white_type, white_position, black_pieces):
    """Determine which black pieces can be captured by the white piece."""
    x, y = ord(white_position[0]) - ord('a'), int(white_position[1]) - 1
    takeable = []

    if white_type == "rook":     #Rook will check the closest pieces both horizontally and vertically
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        for dx, dy in directions:
            steps = 1
            while True:
                nx, ny = x + dx * steps, y + dy * steps
                if nx < 0 or nx > 7 or ny < 0 or ny > 7:
                    break  # Out of bounds
                position = chr(nx + ord('a')) + str(ny + 1)
                for piece_type, piece_position in black_pieces:
                    if piece_position == position:
                        takeable.append((piece_type, piece_position))
                        break
                if any(piece_position == position for _, piece_position in black_pieces):
                    break
                steps += 1

    elif white_type == "pawn":  # Pawns capture diagonally only forward (to higher ranks)
        for piece_type, position in black_pieces:
            bx, by = ord(position[0]) - ord('a'), int(position[1]) - 1
            if (y == by - 1) and (abs(x - bx) == 1):
                takeable.append((piece_type, position))

    return takeable

if __name__ == "__main__":
    main()
