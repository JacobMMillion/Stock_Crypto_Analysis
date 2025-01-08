from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
import pandas as pd
from train_model_generic import train_random_forest_model, print_model_statistics, predict_next_day

# Load data
df = pd.read_csv('labeled_stock_data.csv')

# Train-test split
train = df.iloc[:-400]  # Train on all data except the last 400
test = df.iloc[-400:]   # Test on the last 400 rows

# Define the predictors
predictors = ["open", "high", "low", "close", "volume"]
model_name = 'STOCK'

best_model = train_random_forest_model(predictors, train)

# Predict on the test set
predictions = best_model.predict(test[predictors])

# Print model stats
print_model_statistics(model_name, predictions,train, test)

# Predict on the next day's data
file_name = 'cleaned_stock_data.csv'
predict_next_day(file_name, predictors, best_model)