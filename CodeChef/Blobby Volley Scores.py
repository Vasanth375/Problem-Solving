aliceScore = 0
bobScore = 0
alice = "server"
bob = "receiver"

string = "BABAB"
for i in string:
    if i == "A":
        if alice == "server":
            aliceScore += 1
        elif alice == "receiver":
            alice = "server"
            bob = "receiver"
    elif i == "B":
        if bob == "server":
            bobScore += 1
        elif bob == "receiver":
            alice = "receiver"
            bob = "server"
print(aliceScore, bobScore)
