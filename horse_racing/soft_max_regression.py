import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Example: Load your data
# data = pd.read_csv('horse_race_data.csv')
# For demonstration, let's create a dummy dataset:
data = pd.DataFrame({
    'race_id': [1,1,1,2,2,2],
    'speed': [100, 98, 101, 95, 97, 96],
    'jockey_rating': [80, 85, 78, 90, 88, 86],
    'winner': [1, 0, 0, 0, 1, 0]
})

# Features to use
feature_cols = ['speed', 'jockey_rating']

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(data[feature_cols])

# The target: index of winner in each race
# For multinomial logistic regression, we want to predict which horse wins in each race.
# So, we need to reshape the data: one row per horse, target = winner (1 or 0)
y = data['winner']

# Fit the multinomial logistic regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X, y)

# Predict probabilities for each horse
probs = model.predict_proba(X)  # shape: (n_horses, 2) for binary outcome (win/lose)

# Attach probabilities to the original data
data['prob_lose'] = probs[:, 0]
data['prob_win'] = probs[:, 1]

print(data[['race_id', 'speed', 'jockey_rating', 'prob_win']])
