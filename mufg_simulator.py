#!/usr/bin/pyton
from __future__ import division
import random

initial_items = int(raw_input("how many items do you have at the start?: ") or "50")
iteration_days = int(raw_input("how many days do you have to multiple them?: ") or "100")
trials = 1000


def iterate_n_days(n, initial_items):
  current_items = initial_items 
  for x in range(1, n):
      new_items = 0;
      for y in range (1,current_items):
          if (random.random() < 0.01):
              new_items =new_items +1
      current_items=current_items+new_items;
      print "day=",y," m=",current_items
  return current_items

total_items_accumulated = 0
for y in range(trials):
  total_items_accumulated += iterate_n_days(iteration_days,initial_items)

average_items_accumulated = total_items_accumulated / trials 



print "average items after ", iteration_days, " days over", trials, " trials", average_items_accumulated
print "This assumes that you are moving items to new MUFG capsules when the capsule reaches 90 or so items and keeping your inventory from becoming overfull."
