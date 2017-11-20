Name: Harsh Patel
Course: CS4641
Assignment: Randomized Optimization

I utilized the ABAGAIL framework (https://github.com/pushkar/ABAGAIL) to complete parts 1 and 2 of this project. I have included the modifed code for AbaloneTest.java along with my dataset (Vehicle) if you deem necessary to replicate my results.

I utilized the Flappy Bird Genetic Algorithm by Namkha Norsang (https://github.com/Nam-Nor/Flappy-Bird-Genetic-Algorithms) to complete part 3 of this project. I have included flappy.py along with all of my Keras models if you deem necessary to replicate my results.

In order to run my datasets to verify my results, follow the steps outlined below:
For Part 1:
1. Replace AbaloneTest.java with the one provided in the ABAGAIL framework.
2. Add in vehicle.txt to the same directory as AbaloneTest.java
3. Run the Java File

For Part 2:
1. Utilize built in optimization problems from ABAGAIL (src -> opt -> test); specifically CountOnesTest.java, TravelingSalesman.java, and ContinuousPeaks.java
2. Tune hyperparameters in the same way as I point out in my analysis
3. Run the Java File

For Part 3:
1. Replace flappy.py from the Flappy Bird Genetic Algorithms software with the one provided in this zip
2. Tune the hyperparaters as pointed out in the analysis
3. Run the Python File

[Note: I have made changes to the mainGame() and showGameOverScreen() to better visualize the changes. In mainGame(), I added a limit on the number of generations and a limit on the score (after which the game exits and a summary is printed). In showGameOverScreen(), I simply print out useful information such as the current generation number, average fitness, total score, etc. ]

Files included in this zip: vehicle.txt (complete dataset), vehicle_train.arff, AbaloneTest.java, flappy.py, Flappy Bird Keras Models (folder with all old models), README.txt, hpatel304-analysis.pdf, Raw_Data.xlsx