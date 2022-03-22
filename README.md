# Cluster based shrinkage of correlation matrix implementation

This is an implementation using Python of the Cluster based shrinkage correlation estimator proposed by Begusic and Kostanjcar in the paper *Cluster-Based Shrinkage of Correlation Matrices for Portfolio Optimization* (2019) that can be found [here](https://ieeexplore.ieee.org/document/8868482).

This estimator uses a clustering method to identify underlying structure in the sample correlation matrix and then use the structure to regulirize the entries of the sample correlation estimator. 