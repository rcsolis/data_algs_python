print("Tic tac toe Sample Winner function")
# Test cases
noWinner = [
    ["o","x","o"],
    ["x","x","o"],
    ["x","o","x"]
]
oWinner = [
    ["o","x","o"],
    ["x","x","o"],
    ["x","","o"]
]
xWinner = [
    ["o","x","x"],
    ["o","x",""],
    ["x","o",""]
]
# winner function
def hasWinner(data):
    # parse data as linear
    linearData = [el for row in data for el in row]
    # posible winning combinations
    posibleWins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    # Loop over each posible win condition
    for combination in posibleWins:
        # unpact values(indexes)
        a,b,c = combination
        # winning condition
        if linearData[a] and linearData[a] == linearData[b] and linearData[a] == linearData[c]:
             return True
    return False
# Run tests
print("First case(noWinner)", noWinner)
print("result: ", hasWinner(noWinner))
print("Second case(oWinner)", oWinner)
print("result: ", hasWinner(oWinner))
print("Third case(xWinner)", xWinner)
print("result: ", hasWinner(xWinner))