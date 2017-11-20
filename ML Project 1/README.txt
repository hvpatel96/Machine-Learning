Name: Harsh Patel
Course: CS4641
Assignment: Supervised Learning

I utilized the WEKA 3.8.1 (java implementation) to split my datasets into training and testing sets (via random resampling without replacement -> 80% training, 20% testing) in addition to running each of the five different ML algorithms required for this project (Decision Trees, Neural Nets, Boosting, SVM, and KNN).

In order to run my datasets to verify my results, follow the steps outlined below:
1. Open the Explorer
2. Open the training set file (labeled either vehicle_train or pendigits_train)
3. Select the appropriate algorithm ->
    Decision Tree = J48 (under trees)
    Neural Net = Multilayer Perceptron (under functions)
    Boosting = AdaBoostM1 (weka.classifiers.meta.AdaBoostM1, download using package manager on main window -> under meta)
    SVM = LibSVM (weka.classifiers.functions.LibSVM, download using package manager on main window -> under functions)
    KNN = IBK (under lazy)
4. Set the hyperparameters to appropriate values or run CVParameterSelection (under meta) to find good starting values
5. Run using the training set as testing set
6. Run using 10 fold cross-validation
7. Re-evaluate previous two models on specific testing set (labeled either vehicle_test or pendigits_test)

Files included in this zip: vehicle.arff (complete dataset), vehicle_train.arff, vehicle_test.arff, pendigits.arff (complete dataset), pendigits_train.arff, pendigits_test.arff, README.txt, hpatel304-analysis.pdf, Raw_Data.xlsx