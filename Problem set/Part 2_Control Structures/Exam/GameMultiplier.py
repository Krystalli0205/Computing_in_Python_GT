score = 500
difficulty_bonus = 1.2
perfect_run = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you're writing the code for a video game. Your code
#calculates the player's final score on a particular level.
#
#The player's original final score is given by the variable
#score. Then, there are a few multipliers or changes that
#can apply:
#
# - The score should be multiplied by the Difficulty Bonus,
#   which could be 1.0, 1.2, 1.4, 1.6, 1.8, or 2.0.
# - If the player achieves a Perfect Run (perfect_run = True),
#   their score (after applying the Difficulty Bonus) is
#   doubled.
# - If the player's original score (before the difficulty
#   bonus and perfect run bonus) exceeds 200 points, then
#   they receive a 200 point High Performer bonus. The
#   Difficulty bonus and Perfect Run multiplier should not
#   be applied to the High Performer bonus, though.
# - Finally, round their score should be cast to an integer
#   in case any decimals were introduced in the process.
#
#For example, with the original values above, the player's
#original score is 500. The Difficulty Bonus is 1.2, and
#500 * 1.2 = 600. They had a Perfect Run, so their score
#is doubled, and 600 * 2 = 1200. Then, their original score
#was over 200, so they receive the 200-point High Performer
#bonus, and 1200 + 200 = 1400. So, their final scoreis 1400.
#
#Print the final score according to this format:
#
#Your final score is: 1400


#Add your code here!
final_score = score * difficulty_bonus

if perfect_run:
    final_score *= 2

if score > 200:
    final_score += 200

final_score = int(final_score)
print(f"Your final score is: {final_score}")
