#
# ENTER THE DIMENTIONS OF
# BREAKTHRU GAME
#
rows 		= 5   # Number of rows for the table
cols 		= 5   # Number of Columns in the table
row_pieces 	= 2   # It should be an even number b/c each player will have row_pieces/2 rows of PAWNS
starter     = "O" # Which player start the game O(White) or X(Black)?

# Strategies : conqueror, evasive, enhanced, block
# The best one so far is enhanced

x_strategy  = "block" # Enter the play strategy of X
o_strategy  = "conqueror" # Enter the play strategy of O