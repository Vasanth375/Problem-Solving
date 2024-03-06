tokens = [100]
power = 50

tokens = [200, 100]
power = 150

tokens = [100, 200, 300, 400]
power = 200

score = 0
# for token in tokens:
#     if power >= token:
#         # face-up
#         power -= token
#         score += 1
#     elif score >= 1:
#         # face-down
#         power += token
#         score -= 1
# print(power, score)

# two pointers implementation
low = 0
high = len(tokens)-1
tokens.sort()

while low <= high:
    # When we have enough power, play lowest token face-up
    if power >= tokens[low]:
        score += 1
        power -= tokens[low]
        low += 1
    # We don't have enough power to play a token face-up
    # If there is at least one token remaining,
    # and we have enough score, play highest token face-down
    elif score > 0 and low < high:
        score -= 1
        power += tokens[high]
        high -= 1
    # We don't have enough score, power, or tokens
    # to play face-up or down and increase our score
    else:
        print(score)
        break
print(score)
