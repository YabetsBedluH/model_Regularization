"# model_Regularization" 
Apply regularization:

L1: subtract a small fixed amount from each weight (toward zero), which can make some weights exactly zero.
L2: multiply each weight by a value slightly less than 1, shrinking all weights but rarely making any exactly zero.

Which one should you use?

Situation                           Usually better
Many irrelevant features             Lasso (L1)
Most features are useful             Ridge (L2)
Want automatic feature selection     Lasso (L1)
Want stable predictions              Ridge (L2)
Highly correlated features           Ridge (L2)

In real machine learning projects, Ridge is often the safer default
Lasso is especially useful when you have lots of features and suspect many of them are unnecessary.
