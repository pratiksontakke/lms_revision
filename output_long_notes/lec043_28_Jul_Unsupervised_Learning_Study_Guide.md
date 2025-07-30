Here are the full lecture notes in markdown format:

**Support Vector Machines (SVMs)**
=============================

### Introduction

* SVM is a supervised learning algorithm used for classification and regression tasks.
* It tries to find the optimal hyperplane that separates data points of different classes with the maximum margin.

### Maximum Margin

* In 2D space, the hyperplane is a line; in 3D, it is a plane, and in higher dimensions, it's called a hyperplane.
* Maximum margin means the distance between the hyperplane and the closest data points of any class (support vectors) is maximized.

### Support Vectors

* Support vectors are the data points closest to the decision boundary and define the position and orientation of the hyperplane.

### Mathematical Model

* The decision boundary (hyperplane) is defined by the equation: `[ w \* x + b = 0 ]`
* where `(w)` is the weight vector, `(x)` is the input feature vector, and `(b)` is the bias.
* For classification, the condition: `[ y_i (w \* x_i + b) >= 1 ]` must hold for all data points `(i)`, where `(y_i)` is the class label (+1 or -1).

### Prediction

* Given a new data point `(x)`, the predicted class (`\hat{y}`) is: `[ \hat{y} = sign(w \* x + b) ]`

**Unsupervised Learning Overview**
=====================================

### Introduction

* Unsupervised learning algorithms work with unlabeled data, i.e., the output classes/labels are not provided.
* The goal is to identify inherent patterns, groupings, or structures in the data.

### Common Tasks

* Clustering: Grouping data points into clusters based on similarity.
* Dimensionality Reduction: Reducing the number of features while preserving important information.

### Example Applications

* Customer segmentation in marketing.
* Fraud detection in finance.
* Various fields like cybersecurity, biology, NLP, and image processing.

**K-Means Clustering**
=====================

### Introduction

* K-Means is a popular clustering algorithm used to partition data points into `(k)` clusters based on feature similarity.

### How it Works

* Choose the number of clusters `(k)`.
* Initialize `(k)` centroids randomly.
* Assign each data point to the nearest centroid (using Euclidean distance).
* Recalculate the centroids as the mean of all points assigned to each cluster.
* Repeat steps 3 and 4 until converged (centroids no longer change).

### New Data Classification

* A new data point is assigned to the cluster whose centroid is nearest to it.

**Hierarchical Clustering**
=====================

### Introduction

* Hierarchical clustering builds a hierarchy (tree-like structure) of clusters without the need to specify the number of clusters `(k)` upfront.

### How it Works

* Computes a distance matrix capturing distances between every pair of data points.
* Iteratively merges the two closest clusters until all points are in a single cluster.
* The process can be visualized using a dendrogram to decide the optimal number of clusters.

**Dimensionality Reduction**
=====================

### Introduction

* Dimensionality reduction is the process of reducing the number of input variables (features) in a dataset, while preserving as much information as possible.

### Benefits

* Simplifying models.
* Reducing noise.
* Speeding up training.
* Visualization of high-dimensional data.

### Techniques

* Principal Component Analysis (PCA).
* t-SNE (t-Distributed Stochastic Neighbor Embedding).

**Principal Component Analysis (PCA)**
=====================================

### Introduction

* PCA transforms the original features into a smaller set of uncorrelated features called principal components.
* Preserves maximum variance in data.

### Steps

* Standardize the data.
* Compute covariance matrix.
* Calculate eigenvalues and eigenvectors.
* Sort eigenvectors by largest eigenvalues (top `(k)` components).
* Project the data onto these components.

**Example of PCA**
==================

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load data
X, y = load_iris(return_X_y=True)

# Initialize PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the PCA output
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.show()
```

This reduces the iris dataset from 4 features to 2 principal components for visualization.