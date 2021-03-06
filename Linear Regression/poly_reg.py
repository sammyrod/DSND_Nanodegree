# TODO: Add import statements
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('Linear Regression/data_poly.csv')

print(train_data.head())

X = train_data[['Var_X']]
y = train_data[['Var_Y']]

print(X.head())
print(y.head())

# Create polynomial features
# TODO: Create a PolynomialFeatures object, then fit and transform the
# predictor feature
poly_feat = PolynomialFeatures()
X_poly = poly_feat.fit_transform(X)

# Make and fit the polynomial regression model
# TODO: Create a LinearRegression object and fit it to the polynomial predictor
# features
poly_model = LinearRegression()

poly_model.fit(X_poly, y)


# Once you've completed all of the steps, select Test Run to see your model
# predictions against the data, or select Submit Answer to check if the degree
# of the polynomial features is the same as ours!