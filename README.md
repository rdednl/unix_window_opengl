This repo is a minimum working example to show how openGL behaves differently on MacOS and Linux.

You can run the simple simulation example (`sim.py`) in two modes.

## User-controlled mode

```
python3 user.py
```

This mode consists in using keyboard commands to control the simulation. It is a very simple simulation.
You press the spacebar to change color between black and pink. Nothing else.

This mode works both in Mac and Linux. (ie. the window opens and we are able to see the simulation)

## Automated mode

```
python3 auto.py
```

This mode consists in a loop that automatically controls the simulation, for 2 sequences of 200 steps each.
Every 20 steps, the color changes automatically.

This mode works in Linux, that is, the window opens and we are able to see the simulation, but it doesn't work on MacOS.
