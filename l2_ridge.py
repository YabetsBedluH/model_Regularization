from sklearn.linear_model import Ridge

model = Ridge(alpha=0.1)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Weights:", model.coef_)
print("Bias:", model.intercept_)