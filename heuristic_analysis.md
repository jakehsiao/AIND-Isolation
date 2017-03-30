In this project, the heuristic function is used to evaluate the game result when the searching tree reaches the maximum depth.

My heuristic is this:
```
score = a * own_moves^2 / (1 + opp_moves) + b * own_moves / (1 + opp_moves^2)
```
which own\_moves stands for the legal moves of current player, opp\_moves stands for that of opponent, "^" stands forpower and a,b are hyperparameters to tune.

To get the best choice of parameters a and b, I used an optimization algorithm called "twiddle" which I learned from course "artificial intelligence for robotics"(in "tournament.py", line 188\-221).

Then after x iters of twiddle, the best parameters chosen are:
```
a = 
b = 
```

