Here are the full lecture notes in markdown format:

**Introduction to Machine Learning and Supervised Learning**
=====================================================

Supervised Learning is a type of Machine Learning (ML) where the model is trained on a labeled dataset. This means for each input data, the output or the label is already known during training. The goal is to learn a mapping from inputs to outputs so that the model can predict labels on unseen data.

In ML, algorithms are broadly categorized into three types:

* **Supervised Learning**: Uses labeled data.
* **Unsupervised Learning**: Uses unlabeled data.
* **Reinforcement Learning**: Learning based on feedback/rewards.

**Classification vs Regression**
=============================

In supervised learning:

* **Classification** algorithms predict discrete labels such as 0 or 1, yes or no, spam or not spam.
* **Regression** algorithms predict continuous numerical values, such as house prices, temperature, etc.

Example classification task: Predict whether an email is spam or not spam.

Example regression task: Predict the price of a house based on its features like size and location.

**Common Supervised Learning Algorithms**
=====================================

Supervised learning algorithms are commonly used and vary depending on the task (classification or regression). Some algorithms can be used for both tasks.

* **Classification only**: Logistic Regression, Naive Bayes, Support Vector Machine (SVM)
* **Regression only**: Linear Regression, Ridge Regression, Lasso, Support Vector Regression (SVR)
* **Both classification and regression**: K-Nearest Neighbors (KNN), Decision Tree, Random Forest, Gradient Boosting, Neural Networks

**Logistic Regression**
=====================

Logistic Regression is a supervised classification algorithm used to predict the probability of a binary outcome (0 or 1). Unlike linear regression which predicts continuous values, logistic regression outputs probabilities between 0 and 1.

It applies a sigmoid (logistic) function to a linear combination of features.
The sigmoid function ensures output probability lies between 0 and 1.
Probability > 0.5 implies class 1, else class 0.
Mathematical Formulation:

Given features vector (X) and weights (W), bias (b):

[ z = W^T X + b ]

Sigmoid function:

[ σ(z) = \frac{1}{1 + e^{-z}} ]

Probability prediction:

[ \hat{y} = σ(z) ]

Loss function used is logistic loss and weights are optimized using Gradient Descent.

Example using sklearn:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
X = data.data
Y = data.target

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize & train model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, Y_train)

# Predict and evaluate
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

**Naive Bayes Classifier**
=====================

Naive Bayes (NB) is a probabilistic classification technique based on Bayes Theorem with the assumption of feature independence. Despite this 'naive' assumption, it often performs very well in practice.

Assumes features are conditionally independent given the class.
Computes the posterior probability for each class given the input features.
Picks the class with the highest posterior probability.
Bayes Theorem:

[ P(A|B) = \frac{P(B|A) P(A)}{P(B)} ]

Where:

(A) is the class label
(B) is the observed features

Example: Spam detection based on word frequencies in emails.

Example using sklearn:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize & train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = nb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

**K-Nearest Neighbors (KNN)**
=====================

K-Nearest Neighbors (KNN) is a simple, instance-based, non-parametric supervised learning algorithm used for classification.

To classify a new data point, it finds the 'k' closest data points (neighbors) in the training set using distance metrics (commonly Euclidean distance).
The class is decided by majority voting among the neighbors.
Euclidean distance between points (x1, y1) and (x2, y2):

[ \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} ]

Steps to predict class for new point:

Compute distance to all training points.
Select k closest neighbors.
Assign the class which is most common among neighbors.
Choosing k: Generally an odd number to avoid ties.

Example: Predicting if a person is fit or unfit based on height and weight using KNN.

Example code snippet using sklearn:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

**Decision Tree Classifier**
=====================

Decision Tree is a supervised learning algorithm that can be used for classification and regression.

It builds a flowchart-like tree structure where internal nodes represent tests on features, branches are outcomes, and leaf nodes represent class labels.
The tree is constructed by selecting features that result in the highest information gain (i.e., best split).
Key concepts:

Entropy: Measures the impurity or randomness in data. Lower entropy means the data is more pure. [ Entropy(S) = - \sum_{i=1}^c p_i \log_2(p_i) ] where (p_i) is the proportion of class i in dataset S.

Information Gain: Reduction in entropy after a dataset is split on a feature. [ IG(S, F) = Entropy(S) - , WeightedEntropy(S|F) ]

The feature with highest information gain is selected as the splitting attribute.

Example: Using weather conditions to decide whether to play tennis or not.

Example code snippet:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train decision tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

**Random State in Train/Test Split**
=====================================

When splitting data into training and testing sets, sklearn's train_test_split function uses randomness to shuffle and split the dataset.

By specifying random_state, you fix the randomness seed so the split is reproducible.
If random_state is not fixed, each run may produce different splits and hence different results.
Example:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)  # Fixed random seed
```

Why use 42? It is a popular informal standard in data science communities inspired by a pop culture reference from the book "The Hitchhiker's Guide to the Galaxy" where 42 is the "answer to the ultimate question of life, the universe, and everything". You can use any integer.