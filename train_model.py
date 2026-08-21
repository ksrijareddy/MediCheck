import pandas as pd
from sklearn.model_selection
import train_test_split
from sklearn.tree import 
DecisionTreeClassifier
from sklearn.metrices import accuracy_score
import pickle

# Load the dataset
data = pd.read_csv("data/symptoms.csv")

# Seperate features and target
X = data.drop("risk_level", axis=1)
y = data["risk_level"]

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
  X,
  y,
  test_size=0.2,
  random_state=42
)

# Create the machine learning model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model accuracy:", accuracy)

# Save the training model
with open("model.pkl", "wb") as
file:
    pickle.dump(model, file)
print("Model saved succesfully!")




