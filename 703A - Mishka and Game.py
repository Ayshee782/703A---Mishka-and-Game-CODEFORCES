n = int(input())  # Number of rounds

mishka_wins = 0
chris_wins = 0

for _ in range(n):
    mi, ci = map(int, input().split())  # Mishka's and Chris's dice values
    if mi > ci:
        mishka_wins += 1
    elif ci > mi:
        chris_wins += 1
    # If equal, no one wins, so do nothing

# Determine the final winner
if mishka_wins > chris_wins:
    print("Mishka")
elif chris_wins > mishka_wins:
    print("Chris")
else:
    print("Friendship is magic!^^")
