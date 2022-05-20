import numpy as np
from sklearn.cluster import KMeans
import numpy.linalg as LA
import pandas as pd


def get_optimal_K(R_matrix, N, T):
    q = N/T
    lambda_plus = (1 + np.sqrt(q))**2
    lambdas_i = LA.eigvals(R_matrix)
    K = np.sum(lambdas_i > lambda_plus)
    return K

def get_S_matrix(R_matrix, labels):
    label, count_label = np.unique(labels, return_counts=True)
    S_matrix = np.zeros((len(label), len(label)))
    for i in label:
        for j in label:
            if i == j:
                constant = 1/(count_label[i]* (count_label[i]-1))
                S_matrix[i,j] = (constant *(R_matrix[labels == i][:,labels == j] - np.identity(count_label[i])).sum())
            else:
                constant = 1/(2* count_label[i]*count_label[j])

                S_matrix[i,j] = (constant *(R_matrix[labels == i][:,labels == j]).sum())
    return S_matrix

def get_R_tilde(S_matrix, labels):
    label = np.unique(labels)
    R_tilde_matrix = np.zeros((len(labels),len(labels)))
    for i in range(len(labels)):
        for j in range(i,len(labels)):
            R_tilde_matrix[i,j] = R_tilde_matrix[j,i] = S_matrix[labels[i], labels[j]]
    return R_tilde_matrix

def get_R_clust(R_matrix, R_tilde_matrix, alpha):
    if not(0<=alpha and 1>= alpha):
        return np.NaN
    return alpha*R_tilde_matrix + (1-alpha)*R_matrix

def get_shrinkage_est(X_matrix, alpha):
    if not(0<=alpha and 1>= alpha):
        print("the value of alpha should be between 0 and 1")
        return np.NaN
    R_matrix = np.corrcoef(X_matrix.T)
    D_matrix = 1 - R_matrix
    N = X_matrix.shape[1]
    T = X_matrix.shape[0]
    K = get_optimal_K(R_matrix,N,T)
    # NOTA, AQUÍ SE USA UN RANDOM STATE DIFERENTE PARA HACER LOS CLUSTERINGS, LO QUE PUEDE OCASIONAR QUE
    # LAS INSTANCIAS NO SIEMPRE SEAN ASIGNADAS AL MISMO CLUSTER Y POR LO TANTO NO SIEMPRE SE OBTENGA EL MISMO RESULTADO
    # AL EJECUTAR LA FUNCIÓN. SE ESTABLECE RANDOM STATE PARA REPRODUCIR RESULTADOS.
    if K ==1 :
        K=2
    C_kmeans = KMeans(n_clusters=K, random_state = 0, init='k-means++').fit(D_matrix)
    S_matrix = get_S_matrix(R_matrix, C_kmeans.labels_)
    R_tilde = get_R_tilde(S_matrix, C_kmeans.labels_)
    shrink_est = (alpha*R_tilde + (1-alpha)*R_matrix)
    np.fill_diagonal(shrink_est, 1) 
    return shrink_est

