#!/usr/bin/pyton
from __future__ import division
import random


def iterate_n_days(n, initial_items):
  current_items = initial_items 
  for x in range(1, n):
      new_items = 0;
      for y in range (1,current_items):
          if (random.random() < 0.01):
              new_items =new_items +1
      current_items=current_items+new_items;
#      print "day=",y," m=",current_items
  return current_items

def how_many_in_n_days():
  initial_items = int(raw_input("how many items do you have at the start?: ") or "50")
  iteration_days = int(raw_input("how many days do you have to multiple them?: ") or "100")
  trials = 1000
  average_items_accumulated = how_many_in_n_days(initial_items, iteration_days, trials)
  print "average items after ", iteration_days, " days over", trials, " trials", average_items_accumulated
  print "This assumes that you are moving items to new MUFG capsules when the capsule reaches 90 or so items and keeping your inventory from becoming overfull."

def how_many_in_n_days(initial_items, iteration_days, trials):
  total_items_accumulated = 0
  for y in range(1,trials):
    total_items_accumulated += iterate_n_days(iteration_days,initial_items)

  average_items_accumulated = total_items_accumulated / trials
  return average_items_accumulated
 

def how_many_in_n_capsules(initial_items, number_of_capsules):
  number_of_capsules = number_of_capsules
  each_capsule_items = int(initial_items / number_of_capsules)
  days_to_wait = 180
  trials = 1000
  
  print "Running trials for two capsules split: ..."
  total_items_accumulated = 0
  for capsule in range(0,number_of_capsules):
    total_items_accumulated = total_items_accumulated + how_many_in_n_days(each_capsule_items, days_to_wait, trials)
  print "Using separate capsules, on average we would get: ", total_items_accumulated

  print "Running trials for items together: ..."
  total_items_accumulated = how_many_in_n_days(initial_items, days_to_wait, trials)
  print "Putting items together, on average we would get: ", total_items_accumulated

initial_items = 4
number_of_capsules = 2
how_many_in_n_capsules(initial_items, number_of_capsules)
