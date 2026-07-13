from sklearn.linear_model import Lasso


model = Lasso(alpha=0.1)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
#alpha is the regularization parameter (λ)

print("Weights:", model.coef_)
print("Bias:", model.intercept_) 
