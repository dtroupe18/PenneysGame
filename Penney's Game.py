"""
Problem:

Alice and Bill ask a neutral mediator to flip a fair coin repeatedly and record the sequence
of results. When one of the respective patterns A = HHT (Alice's special pattern) or B = THH (Bill's special pattern)
appears for the first time on the last three flips, play stops and the corresponding player wins.
For instance, the flips may be HTTHTTTHH at which point, Bill wins.

Oscar learns of this game and argues as follows: since either of the special patterns for Alice and Bill can
occur in sequence with probability 1/8, both players will have the same number of wins on average if the game
is played repeatedly. Prove or disprove Oscar's reasoning.
  """

"""
Solution:
A = HHT vs B = THH certainly do not have the same odds of success in the this game.
Oscar can be proven wrong by just looking at the results of the first flip.
If the first flip is a T then THH has a 100% chance of winning.
Additionally, if the first flip is H both of sequences have a 50% chance of winning.
It is clear that the odds favor THH, but by how much?

Analyze the problem by looking at all of the possible sub sequences of length two.
We have four possible scenarios {HH, HT, TH, TT} we will see that THH wins in three of these scenarios.
Given HH is the result of the first two flips then HHT has a 100% chance of winning.
This is because it is impossible for THH to occur before HHT given that HH has already appeared.
Given {TH, HT, or TT} is the result of the first two flips then THH has a 100% chance of winning.
This is because once a  T has occurred it is impossible for HHT to appear before THH.
Thus we have 4 possibilities and 3 result in a win for THH.
This means that the odds in this case are 3:1 in favor of THH.

"""

# Finally Some Code

import numpy as np
import time


# generate a million trials each with 30 flips
experiment = np.random.randint(0, 2, (1000000, 30))
# 1000 = number of trials 50 = flips per trial
# 0 = heads 1 = tails

# Function takes in a sequence of flips and determines the winner

def wins(flipSequence):
    numWins = 0
    for i in range(len(flipSequence)):
            if flipSequence[i] == 1 and flipSequence[i - 1] == 0 and flipSequence[i - 2] == 0:
                # Alice won HHT or 001
                numWins += 1
                break
            else:
                # + 1 means Bill won THH or 100
                numWins -= 1
                break
    return numWins

# Now we want to run wins on all 1 million trials and print out the odds ratio

t0 = time.clock()
count = np.apply_along_axis(wins, 1, experiment)
bWins = count.sum() * -1
aWins = len(experiment) - bWins
odds = (aWins / bWins)
print("Time to run wins: ", time.clock() - t0)
print(odds)


