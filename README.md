# Recreating the Pareto distribution by simulating an economy

We will create a population of a 1000 people, which will be trading with each other over a period of 500 generations
Each person will be given the same starting sum, a dollar each, and we'll hopefully get an interesting development of the distrubtion of the wealth.

<img align="right" src="https://user-images.githubusercontent.com/121384892/212167589-1b81061f-455d-4ae7-88e7-f617e86c3e19.png" width="250" height="250">

The main goal of the project is to determine whether a Pareto distrubition is developed in a more realistic case for when each person in our population is assigned a personality according to the Big Five model that'll determine their style of trading. For instance, someone who's more conscientious might be working more to earn more money, whereas someone who's introverted might be shy to interact in a dialogue for an eventual trade. Of course, this is a very oversimplistic model of the real world case.

We will model each persons personality with two characteristics, their trading points (tp) and their sucess points (sp). When two people from our population are randomly drawn, their trading points will be compared such that a coin with the same ratio of their trading points will be flipped. If both flips are in favour, a trade will be initiated, otherwise not. Then a new coin will be flipped, now regarding their sucess points, and through the same process, this will determine whether you lose a dollar or not.

The economic distribution of this process will be simulated under the course of our 500 generations. The distribution found in the end will hopefully resemble a Pareto distribution. 
