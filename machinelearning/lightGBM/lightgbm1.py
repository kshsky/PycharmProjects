from lightgbm import LGBMClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, train_test_split

param_grid = {
    'n_estimators': [10, 100],
    'boosting_type': ['gbdt'],
    'num_leaves': [8, 10],
    'subsample': [0.8, 0.95],
    'is_unbalance': [True, False],
    'min_split_gain': [0.01, 0.02, 0.05]
}

lgb = LGBMClassifier(
    random_state=42,
    early_stopping_rounds=10,
    eval_metric='auc',
    verbose_eval=20
)

grid_search = GridSearchCV(
    lgb,
    param_grid=param_grid,
    scoring='roc_auc',
    cv=5,
    n_jobs=-1,
    verbose=1
)

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=42
)

grid_search.fit(
    X_train,
    y_train,
    eval_set=(X_test, y_test)
)

best_model = grid_search.best_estimator_

# ---------------- my added code -----------------------#
# inspect current parameters
params = best_model.get_params()
print(params)

# remove early_stopping_rounds
params["early_stopping_rounds"] = None
best_model.set_params(**params)
# ------------------------------------------------------#

best_model.fit(X_train, y_train)