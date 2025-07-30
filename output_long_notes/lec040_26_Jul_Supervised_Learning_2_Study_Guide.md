Here are the full lecture notes in markdown format:

**Supervised Learning**
=====================

### Classification vs Regression

* Supervised learning involves training a model on labeled data.
* There are two main types of supervised learning:
	+ **Classification**: Output variable is discrete/classes. Example: Email spam detection (Spam/Not Spam), Image recognition (Cat/Dog).
	+ **Regression**: Output variable is continuous. Example: Predicting temperature, house prices, stock prices.

### Regression Overview

* Regression is a supervised learning approach to predict continuous output values based on input features.
* Goal: Learn a function (f(x)) that maps input features (x) to a continuous output (y).
* Use Cases:
	+ Predicting house prices
	+ Stock market price prediction
	+ Weather forecasting
	+ Demand forecasting

### Linear Regression: Single Variable

* Models the relationship between a scalar dependent variable (y) and one independent variable (x) with a linear equation: [y = mx + c]
* Where:
	+ m is the slope
	+ c is the y-intercept
* Example: Predicting marks based on number of hours studied.

### Linear Regression: Multiple Variables (Multivariate Linear Regression)

* When multiple features influence the output, linear regression extends to multivariate form: [y = β0 + β1x1 + β2x2 + ... + βnxn]
* Where:
	+ x_i are features
	+ β_i are coefficients (weights)
	+ β0 is the intercept (bias)
* Example: Predicting student marks based on hours studied and hours slept.

### Mean Squared Error (MSE) as Loss Function

* The loss function measures how well the regression model fits the data.
* Mean Squared Error (MSE): [MSE = 1/n ∑(y_i - y_i)^2]
* Where:
	+ y_i is actual value
	+ y_i is predicted value
* Minimizing MSE leads to the best-fitting line.

### Problems with Linear Regression: Overfitting and Multicollinearity

* **Overfitting**: When the model learns the noise in the training data, resulting in poor performance on unseen data.
* **Multicollinearity**: When features are highly correlated, it makes the coefficients unstable and confused.
* Example of multicollinearity: Feature 2 is exactly 3 times Feature 1.

### Regularization in Regression: L1 and L2

* Regularization adds a penalty to the loss function to prevent overfitting and handle multicollinearity.
* Objective: Reduce the influence of irrelevant/noisy features by shrinking their coefficients.
* Penalty term added to loss function:
	+ **L1 Regularization (Lasso)**: Adds the sum of absolute values of coefficients: [Loss = MSE + λ ∑|β_j|]
	+ **L2 Regularization (Ridge)**: Adds the sum of squares of coefficients: [Loss = MSE + λ ∑β_j^2]
* Choosing (λ): Using cross-validation to select the value minimizing validation loss.

### Difference Between L1 and L2 Regularization

* **L1 Regularization (Lasso)**:
	+ Sum of absolute values of coefficients
	+ Can zero out coefficients; used for feature selection
* **L2 Regularization (Ridge)**:
	+ Sum of squares of coefficients
	+ Shrinks but never zeros; does not perform feature selection

### Polynomial Regression

* Polynomial regression is an extension of linear regression where the relationship between the independent variables and the dependent variable is modeled as an nth-degree polynomial.
* Equation for polynomial regression of degree 2: [y = β0 + β1x + β2x^2]
* If degree (n = 1), it's equivalent to linear regression.
* Useful when data shows a non-linear relationship.
* Example: Predicting salary based on years of experience where salary growth is not linear.

### Random Forest Regressor

* Random Forest is an ensemble learning method that builds multiple decision trees and aggregates their predictions to improve accuracy and reduce overfitting.
* Consists of many decision trees trained on random subsets of data and features (row sampling and feature sampling).
* Each tree predicts a value; the final prediction is the average of all trees' outputs.
* Advantages:
	+ Reduces overfitting common to single decision trees.
	+ More stable and accurate.
* Example Workflow:
	1. Randomly sample rows (with replacement) to train each tree.
	2. Randomly select subset of features for each tree.
	3. Train multiple decision trees.
	4. Predict new data by averaging predictions from all trees.

### Example Code (Random Forest Regressor)

```python
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data
california = fetch_california_housing()
X, y = california.data, california.target

# Split train-test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict
y_pred = rf.predict(X_test)
print(y_pred[:5])
```

I hope this helps! Let me know if you have any questions or need further clarification.