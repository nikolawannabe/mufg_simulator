# mufg_simulator
Simulator for production of items in a MUFG


# Examples
```
$ python mufg_simulator.py 
Calculate items gained in N days (calcitems) or Run some tests about how whether it's better to use multiple capsules or one (testcapsules):     
how many items do you have at the start?: 24
how many days do you have to multiple them?: 90
average items after  90  days over 1000  trials 58.386
This assumes that you are moving items to new MUFG capsules when the capsule reaches 90 or so items and keeping your inventory from becoming overfull.
```

```
ctalbot@frankland ~/src/ingress/mufg_simulator  (master)  ❄ python mufg_simulator.py 
Calculate items gained in N days (calcitems) or Run some tests about how whether it's better to use multiple capsules or one (testcapsules): testcapsules
how many days to wait (default 90) 
how many items altogether? (default 24) 
how many capsules to split them into (default 2) 
Running  1000 trials for two capsules split: ...
Using separate capsules, on average we would get:  58.832
Running 1000 trials for items together: ...
Putting items together, on average we would get:  58.829
```
