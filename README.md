# Nao Cheating Demo

Code for a public-facing demo where the Nao robot cheats at the game rock-paper-scissors.

## Relevant HRI Literature

Short, E., Hart, J., Vu, M., & Scassellati, B. (2010, March). No fair!! an interaction with a cheating robot. In _2010 5th ACM/IEEE International Conference on Human-Robot Interaction (HRI)_ (pp. 219-226). IEEE.

Litoiu, A., Ullman, D., Kim, J., & Scassellati, B. (2015, March). Evidence that robots trigger a cheating detector in humans. In _Proceedings of the Tenth Annual ACM/IEEE International Conference on Human-Robot Interaction (HRI)_ (pp. 165-172).

## Running the Code

You'll first need to set up the naoqi python library (see the [nao_tutorial](https://github.com/SeboLab/nao_tutorial)) github repo for instructions on how to do this.

Then, you just need to run:
```
python2 naocheat.py
```

## ToDos
- Some children got pretty upset at MSI, since the code right now has it so that the child can never win. The change we'd suggest making is that the robot cheats every other time that the person starts out winning (where it cheats on the first one, doesn't the second time, does the third time, etc.).
