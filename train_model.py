import pandas as pd # type: ignore
import pickle
from sklearn.model_selection import train_test_split # type: ignore 
df = pd.read_csv("car.csv")
df['Car_Age'] = 2025 - df['year']
df.drop(['name','year'], axis=1, inplace=True)
df = pd.get_dummies(df, drop_first=True)
X = df.drop('selling_price', axis=1)
y = df['selling_price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
#LinearRegression
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.metrics import r2_score # type: ignore
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
score= r2_score(y_test, pred)
print("Linear Regression R2:", score)
#Decision tree
from sklearn.tree import DecisionTreeRegressor # type: ignore
model1 = DecisionTreeRegressor(random_state=42)
model1.fit(X_train, y_train)
pred = model1.predict(X_test)
score1 = r2_score(y_test, pred)
print("Decision Tree R2:", score1)
#RandomForest
from sklearn.ensemble import RandomForestRegressor  # type: ignore
model2 = RandomForestRegressor(n_estimators=300,random_state=42)
model2.fit(X_train, y_train)
pred = model2.predict(X_test)
score2 = r2_score(y_test, pred)
print("Random Forest R2:", score2)
#GradientBoosting
from sklearn.ensemble import GradientBoostingRegressor# type: ignore
model3= GradientBoostingRegressor(random_state=42)
model3.fit(X_train, y_train)
pred = model3.predict(X_test)
score3 = r2_score(y_test, pred)
print("Gradient Boosting R2:", score3)
#ExtraTrees
from sklearn.ensemble import ExtraTreesRegressor# type: ignore
model4 = ExtraTreesRegressor(n_estimators=300,random_state=42)
model4.fit(X_train, y_train)
pred = model4.predict(X_test)
score4 = r2_score(y_test, pred)
print("Extra Trees R2:", score4)
#the Random Forest is have high R2 score so R.F is selected 
pickle.dump(model2,open("model.pkl", "wb"))
pickle.dump(X.columns,open("features.pkl", "wb"))
print(X.columns.tolist())