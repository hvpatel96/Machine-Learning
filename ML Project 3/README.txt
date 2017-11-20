Name: Harsh Patel
Course: CS4641
Assignment: Unsupervised Learning

I utilized the WEKA 3.8.1 (java implementation) to split my datasets into training and testing sets (via random resampling without replacement -> x% training, (1-x)% testing) in addition to running each of the different ML algorithms required for this project (kMeans, Expectation Maximization, Principal Components, AutoEncoder, Random Projects, and Neural Networks). I also wrote my own python file (clusterConvert.py), commented to show thought process, to create new feature vectors from clusters for question 5 of the assignment.

In order to run my datasets to verify my results, follow the steps outlined below:
1. Open WEKA Explorer
2. Open the appropriate dataset file (stored in labeled folders (PCA, EN, RP, or ClusterNN [for question 5]))
3. Select the appropriate algorithm ->
    kMeans = SimpleKMeans (under cluster)
    Expectation Maximization = EM (under cluster)
    PCA = Principal Components (under filter -> unsupervised -> attributes in preprocessor)
    AutoEncoding = MLPAutoencoder (under filter -> unsupervised -> attributes in preprocessor)
    Random Projections = Random Projections (under filter -> unsupervised -> attributes in preprocessor)
    Neural Net = Multilayer Perceptron (under classification -> functions)
4. Set the hyperparameters to appropriate values or run CVParameterSelection (under meta) to find good starting values
5. Run using the dataset
6. For Part 5, run the provided python file clusterConvert.py and go back into WEKA to run Neural Network learner

Files included in this zip:
vehicle.arff (complete dataset),
vehicle.csv (complete dataset),
pendigits.arff (complete dataset),
clusterConvert.py (python file using vehicle.csv to create new file with transformed feature vectors),
README.txt,
hpatel304-analysis.pdf,
Raw_Data.xlsx,
EN (folder with all files related to AutoEncoding, including Neural Network files for question 4),
PCA (folder with all files related to Principal Components, including Neural Network files for question 4),
RP (folder with all files related to Random Projections, including Neural Network files for question 4),
and ClusterNeuralNet (folder with all files related to question 5)