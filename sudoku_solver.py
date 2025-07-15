''' Projekti perdor idene e "backtracking" 
qe me pak fjale i bje provo nje numer, nese nuk funksionon, kthehu edhe provoje nje numer tjeter '''


#Funksioni e gjen qelizen e pare boshe
# Vlerat e seciles jena duke i shenu me 0
 
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            #nese eshte bosh qeliza (permban 0) kthen pozicionin
            if puzzle[r][c] == 0:
                return r, c
    return None, None
    
# funksioni qe e kqyr a munet mu vendos nje numer ne qat "qelize"
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False #nese nr o qaty smun mu vendos
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3


    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True    


#Funksioni kryesor qe zgjidh Puzzle
def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle) # e gjen nje qelize te lire 

#nese nuk ka qelize te lire, i bje qe eshte i zgjidhur
    if row is None:
        return True

#I provojme numrat prej 1-9 ne qelizen e lire
    for guess in range(1, 10):
    # E shikojme a eshte numri valid per mu vendos
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess # vendosim nr ne qelize
    #HAPI 4: thirrim funksionin me vazhdu
            if solve_sudoku(puzzle):
                return True #Kur zgjidhet me sukses, kthen "True"
        
        #ne qofte se jo, e hjekim numrin (backtrack!)
        puzzle[row][col] = 0

    return False #kur asnje numer nuk funksionon, kthehet False, i bje qe nuk ka zgjidhje


#SHEMBULL!
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 7, 2, 1, 9, 5, 0, 0, 0],
    [1, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 8, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(puzzle):
    for row in puzzle:
        print(row)
else:
    print("No solution exists")