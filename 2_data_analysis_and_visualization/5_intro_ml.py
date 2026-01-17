"""
Confusion Matrix and Quadrant Interpretation

A confusion matrix is a performance evaluation tool for classification models. It compares the actual class labels with the predicted class labels, allowing us to understand where the model performs correctly and where it makes errors.

Standard confusion matrix layout
* Rows represent the actual class
* Columns represent the predicted class

                        Predicted Positive     Predicted Negative
                    -----------------------------------------------
Actual Positive        |     TP                |      FN
                    -----------------------------------------------
Actual Negative        |     FP                |      TN
                    -----------------------------------------------


Quadrant-wise explanation:

First Quadrant — True Positives (TP)
This quadrant represents instances where the model correctly predicts a positive outcome.

Example (customer purchase prediction):
Customers who were predicted to make a purchase and actually made one.

Importance:
This quadrant reflects the model’s ability to correctly identify potential buyers, which is crucial for effective targeting and efficient resource allocation.
---
Second Quadrant — False Negatives (FN)
This quadrant represents instances where the model incorrectly predicts a negative outcome when the actual outcome is positive.
Also known as Type II errors.

Example:
Customers who were predicted not to make a purchase but actually did.

Importance:
This quadrant highlights missed opportunities. A high number of false negatives means potential customers are being overlooked.
---
Third Quadrant — False Positives (FP)
This quadrant represents instances where the model incorrectly predicts a positive outcome when the actual outcome is negative.
Also known as Type I errors.

Example:
Customers who were predicted to make a purchase but did not.

Importance:
False positives can lead to wasted resources, such as unnecessary marketing efforts directed at uninterested customers.
---
Fourth Quadrant — True Negatives (TN)
This quadrant represents instances where the model correctly predicts a negative outcome.

Example:
Customers who were predicted not to make a purchase and indeed did not.

Importance:
This quadrant reflects the model’s ability to correctly filter out uninterested customers, helping businesses avoid unnecessary costs.



Key Metrics:
Accuracy measures overall correctness but can be misleading with imbalanced data.
Accuracy = (Number of Correct Predictions) / (Total Number of Predictions)
Precision focuses on how reliable positive predictions are, helping reduce false alarms.
Precision = (True Positives) / (True Positives + False Positives)
Recall (Sensitivity) measures how well the model identifies actual positive cases, minimizing missed opportunities.
Recall = (True Positives) / (True Positives + False Negatives)
F1-score balances precision and recall, especially when both false positives and false negatives matter.
F1-Score = 2 * (Precision * Recall) / (Precision + Recall)
ROC-AUC: The Receiver Operating Characteristic Area Under the Curve (ROC-AUC) evaluates the model's ability to distinguish between positive and negative classes across different classification thresholds.



The basic unit of an artificial neural network is the neuron, often called a perceptron.
a neuron can be broken down into three key components:
Inputs: The neuron receives multiple input signals, each representing a feature or piece of information relevant to the task at hand. These inputs are typically numerical values.
Weights: Each input signal is associated with a weight, which determines the strength or importance of that input. The weights are adjustable parameters that are learned during the training process.
Activation function: The neuron applies an activation function to the weighted sum of its inputs. This function introduces non-linearity into the network, allowing it to learn complex relationships in the data
Depth and complexity
The number of hidden layers in a network is called its "depth."

Innovative techniques like regularization, which prevents overfitting by adding constraints to the learning process, are being explored. Transfer learning, a method that leverages knowledge gained from one task to improve performance on another, is also showing promise.
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(x_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(x_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
