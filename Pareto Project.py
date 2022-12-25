# The Pareto Project

# We will create a population of a 1000 people, which will be trading with each other over a period of 500 generations
# Each person will be given the same starting sum, a dollar each, and we'll hopefully get an interesting development of the distrubtion
# of the wealth.

# The main goal of the project is to determine whether a Pareto distrubition is devedloped in a more realistic case for when
# each person in our population is assigned a personality that'll determine their style of trading

# We will model each persons personality with two characteristics, their trading points (tp) and their sucess points (sp)
# When two people from our population are randomly drawn, their trading points will be compared such that a coin with the same
# ratio of their trading points will be flipped. If both flips are in favour, a trade will be initiated, otherwise not.
# Then a new coin will be flipped, now regarding their sucess points, and through the same process, this will determine whether you lose
# a dollar or not.

import matplotlib.pyplot as plt
import numpy as np
import random

nump = 1000

class person:
    def __init__(self, key, money, tp, sp, o, c, e, a, n):
        self.key = key
        self.money = money
        self.tp = tp
        self.sp = sp
        self.c = c
        self.o = o
        self.e = e
        self.a = a
        self.n = n

population_list = []

def trading_points(normalvals):

    tp_start = 100
    tp_start += (normalvals[0] + normalvals[1] + normalvals[2] + normalvals[3] - normalvals[4]) * 20

    return tp_start

def sucess_points(normalvals):

    sp_start = 100
    sp_start += (normalvals[1]-normalvals[3]-normalvals[4]) * 20

    return sp_start

def personality_traits():

    for i in range(0,nump):
        normalvals = np.random.normal(loc=0.0, scale=1.0, size=5)
        tpp, spp = trading_points(normalvals), sucess_points(normalvals)

        personx = person(i,1, tpp,spp, normalvals[0], normalvals[1], normalvals[2], normalvals[3], normalvals[4])
        population_list.append(personx)

def decision(probability):
    return random.random() < probability

def trading():

    fig = plt.figure()
    numgens = 100

    money_list = [1 for i in range(0, nump)]

    for gen in range(0,numgens):

        templist = population_list.copy()
        random.shuffle(templist)
        money_list.clear()
        plt.clf()

        money_list = [x+1 for x in money_list if x == 0] # Payment in each generation for the poorest people
        # running the simulation with this doesn't seem to change anything, the pareto distribution remains
        # in fact, the already rich continue to accumulate even more money. This is expected since the personalities
        # of each individual doesn't change by our presumptions. This is clearly false in the real world, but still works
        # as a model.

        for el in range(0,nump//2):

            num1 = random.randint(0,len(templist)-1)
            personx = templist.pop(num1)

            num2 = random.randint(0,len(templist)-1)
            persony = templist.pop(num2)

            coinx, coiny = personx.tp/(personx.tp + persony.tp), persony.tp/(personx.tp + persony.tp)
            dx, dy = decision(coinx), decision(coiny)

            if dx == dy:
                cxs, cys = personx.sp / (personx.sp + persony.sp), persony.sp / (personx.sp + persony.sp)
                dxs, dys = decision(cxs), decision(cys)

                if dxs != dys:
                    if dxs == True:
                        if persony.money == 0:
                            pass
                        else:
                            personx.money = personx.money + 1
                            persony.money = persony.money - 1

                    else:
                        if personx.money == 0:
                            pass
                        else:
                            persony.money = persony.money + 1
                            personx.money = personx.money - 1

            money_list.append(personx.money)
            money_list.append(persony.money)


        my_dict = {i: money_list.count(i) for i in money_list}
        sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}

        plt.xlabel("Money $")
        plt.ylabel("Number of people")
        plt.title("Pareto Distribution with the Big Five Model")

        plt.bar(my_dict.keys(), my_dict.values(), color='g', width = 0.5)
        plt.plot(sorted_dict.keys(), sorted_dict.values(), color = "black", marker = '*')
        plt.pause(0.01)

personality_traits()
trading()

plt.show()
