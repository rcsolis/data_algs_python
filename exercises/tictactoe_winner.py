print("Tic tac toe Sample Winner function")
#  Test cases
noWinner = [
    ["o", "x", "o"],
    ["x", "x", "o"],
    ["x", "o", "x"]
]
oWinner = [
    ["o", "x", "o"],
    ["x", "x", "o"],
    ["x", "", "o"]
]
xWinner = [
    ["o", "x", "x"],
    ["o", "x", ""],
    ["x", "o", ""]
]


#  winner function
def has_winner(data):
    #  parse data as linear
    linear_data = [el for row in data for el in row]
    #  possible winning combinations
    possible_wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    #  Loop over each possible win condition
    for combination in possible_wins:
        #  unpack values(indexes)
        a, b, c = combination
        #  winning condition
        if linear_data[a] and linear_data[a] == linear_data[b] and linear_data[a] == linear_data[c]:
            return True
    return False


#  Run tests
print("First case(noWinner)", noWinner)
print("result: ", has_winner(noWinner))
print("Second case(oWinner)", oWinner)
print("result: ", has_winner(oWinner))
print("Third case(xWinner)", xWinner)
print("result: ", has_winner(xWinner))
