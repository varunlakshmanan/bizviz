import optuna
from sklearn.model_selection import cross_val_score
import warnings

warnings.filterwarnings("ignore", "Solver terminated early.*")
warnings.filterwarnings("ignore", "Maximum number of iteration reached before*")


# All objective functions define a single trial in Optuna for each type of estimator
def dt_objective(trial, x, y, estimator):
    max_depth = int(trial.suggest_int("max_depth", 1, 15, 1))
    min_samples_split = trial.suggest_discrete_uniform("min_samples_split", 0.005, 0.5, 0.005)
    min_samples_leaf = trial.suggest_discrete_uniform("min_samples_leaf", 0.001, 0.1, 0.001)
    min_weight_fraction_leaf = trial.suggest_discrete_uniform("min_weight_fraction_leaf", 0.0, 0.5, 0.05)
    max_features = trial.suggest_discrete_uniform("max_features", 0.01, 0.25, 0.01)
    max_leaf_nodes = int(trial.suggest_int("max_leaf_nodes", 64, 512, 64))
    params = {
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "min_weight_fraction_leaf": min_weight_fraction_leaf,
        "max_features": max_features,
        "max_leaf_nodes": max_leaf_nodes
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def rf_objective(trial, x, y, estimator):
    n_estimators = int(trial.suggest_int("n_estimators", 50, 200, 50))
    max_depth = int(trial.suggest_int("max_depth", 1, 15, 1))
    min_samples_split = trial.suggest_discrete_uniform("min_samples_split", 0.005, 0.5, 0.005)
    min_samples_leaf = trial.suggest_discrete_uniform("min_samples_leaf", 0.001, 0.1, 0.001)
    min_weight_fraction_leaf = trial.suggest_discrete_uniform("min_weight_fraction_leaf", 0.0, 0.5, 0.05)
    max_features = trial.suggest_discrete_uniform("max_features", 0.01, 0.25, 0.01)
    max_leaf_nodes = int(trial.suggest_int("max_leaf_nodes", 64, 512, 64))
    params = {
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "min_weight_fraction_leaf": min_weight_fraction_leaf,
        "max_features": max_features,
        "max_leaf_nodes": max_leaf_nodes
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def ab_objective(trial, x, y, estimator):
    n_estimators = int(trial.suggest_int("n_estimators", 50, 200, 50))
    learning_rate = trial.suggest_discrete_uniform("learning_rate", 0.001, 1, 0.0001)
    params = {
        "n_estimators": n_estimators,
        "learning_rate": learning_rate,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def bag_objective(trial, x, y, estimator):
    n_estimators = int(trial.suggest_int("n_estimators", 50, 200, 50))
    max_samples = trial.suggest_discrete_uniform("max_samples", 0.01, 1.0, 0.01)
    max_features = trial.suggest_discrete_uniform("max_features", 0.01, 0.25, 0.01)
    params = {
        "n_estimators": n_estimators,
        "max_samples": max_samples,
        "max_features": max_features
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def et_objective(trial, x, y, estimator):
    n_estimators = int(trial.suggest_int("n_estimators", 50, 200, 50))
    max_depth = int(trial.suggest_int("max_depth", 1, 15, 1))
    min_samples_split = trial.suggest_discrete_uniform("min_samples_split", 0.005, 0.5, 0.005)
    min_samples_leaf = trial.suggest_discrete_uniform("min_samples_leaf", 0.001, 0.1, 0.001)
    min_weight_fraction_leaf = trial.suggest_discrete_uniform("min_weight_fraction_leaf", 0.0, 0.5, 0.05)
    max_features = trial.suggest_discrete_uniform("max_features", 0.01, 0.25, 0.01)
    max_leaf_nodes = int(trial.suggest_int("max_leaf_nodes", 64, 512, 64))
    params = {
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "min_weight_fraction_leaf": min_weight_fraction_leaf,
        "max_features": max_features,
        "max_leaf_nodes": max_leaf_nodes
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def gb_objective(trial, x, y, estimator):
    learning_rate = trial.suggest_discrete_uniform("learning_rate", 0.001, 1, 0.0001)
    n_estimators = int(trial.suggest_int("n_estimators", 50, 200, 50))
    min_samples_split = trial.suggest_discrete_uniform("min_samples_split", 0.005, 0.5, 0.005)
    min_samples_leaf = trial.suggest_discrete_uniform("min_samples_leaf", 0.001, 0.1, 0.001)
    min_weight_fraction_leaf = trial.suggest_discrete_uniform("min_weight_fraction_leaf", 0.0, 0.5, 0.05)
    max_depth = int(trial.suggest_int("max_depth", 1, 15, 1))
    max_features = trial.suggest_discrete_uniform("max_features", 0.01, 0.25, 0.01)
    max_leaf_nodes = int(trial.suggest_int("max_leaf_nodes", 64, 512, 64))
    params = {
        "learning_rate": learning_rate,
        "n_estimators": n_estimators,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "min_weight_fraction_leaf": min_weight_fraction_leaf,
        "max_depth": max_depth,
        "max_features": max_features,
        "max_leaf_nodes": max_leaf_nodes
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def gp_objective(trial, x, y, estimator):
    n_restarts_optimizer = int(trial.suggest_discrete_uniform("n_restarts_optimizer", 0, 100, 2))
    params = {
        "n_restarts_optimizer": n_restarts_optimizer
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def lr_objective(trial, x, y, estimator):
    penalty = trial.suggest_categorical("penalty", ["l2", "none"])
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-6), 10 ** (-2), 10 ** (-4))
    c = trial.suggest_discrete_uniform("C", 0.01, 10, 0.1)
    solver = trial.suggest_categorical("solver", ["newton-cg", "lbfgs", "sag", "saga"])
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 100, 9100, 1000))
    params = {
        "penalty": penalty,
        "tol": tol,
        "C": c,
        "solver": solver,
        "max_iter": max_iter
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def pa_objective(trial, x, y, estimator):
    c = trial.suggest_discrete_uniform("C", 0.01, 10, 0.1)
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 500, 5000, 500))
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    params = {
        "C": c,
        "max_iter": max_iter,
        "tol": tol,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def ridge_objective(trial, x, y, estimator):
    alpha = trial.suggest_discrete_uniform("alpha", 0.01, 10, 0.1)
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 500, 10000, 500))
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    solver = trial.suggest_categorical("solver", ["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga"])
    params = {
        "solver": solver,
        "alpha": alpha,
        "max_iter": max_iter,
        "tol": tol,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def sgd_objective(trial, x, y, estimator):
    penalty = trial.suggest_categorical("penalty", ["l2", "l1"])
    alpha = trial.suggest_discrete_uniform("alpha", 0.00001, 0.01, 0.001)
    l1_ratio = trial.suggest_discrete_uniform("l1_ratio", 0.01, 0.3, 0.01)
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 500, 20000, 500))
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    params = {
        "penalty": penalty,
        "alpha": alpha,
        "l1_ratio": l1_ratio,
        "max_iter": max_iter,
        "tol": tol,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def per_objective(trial, x, y, estimator):
    penalty = trial.suggest_categorical("penalty", ["l2", "l1", "elasticnet"])
    alpha = trial.suggest_discrete_uniform("alpha", 0.00001, 0.01, 0.001)
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 500, 5000, 500))
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    params = {
        "penalty": penalty,
        "alpha": alpha,
        "max_iter": max_iter,
        "tol": tol,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def sv_objective(trial, x, y, estimator):
    C = trial.suggest_discrete_uniform("C", 0.01, 10, 0.1)
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    params = {
        "C": C,
        "tol": tol,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def nu_sv_objective(trial, x, y, estimator):
    nu = trial.suggest_discrete_uniform("C", 0.01, 1, 0.01)
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    kernel = trial.suggest_categorical("kernel", ["linear", "poly", "rbf", "sigmoid"])
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 500, 20000, 500))
    params = {
        "nu": nu,
        "kernel": kernel,
        "tol": tol,
        "max_iter": max_iter,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def l_sv_objective(trial, x, y, estimator):
    C = trial.suggest_discrete_uniform("C", 0.01, 10, 0.1)
    tol = trial.suggest_discrete_uniform("tol", 10 ** (-5), 10 ** (-1), 10 ** (-3))
    max_iter = int(trial.suggest_discrete_uniform("max_iter", 500, 40000, 500))
    params = {
        "C": C,
        "tol": tol,
        "max_iter": max_iter,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def kn_objective(trial, x, y, estimator):
    n_neighbors = int(trial.suggest_int("n_neighbors", 1, 10, 1))
    weights = trial.suggest_categorical("weights", ["uniform", "distance"])
    algorithm = trial.suggest_categorical("algorithm", ["auto", "ball_tree", "kd_tree", "brute"])
    p = int(trial.suggest_discrete_uniform("p", 1, 10, 1))
    params = {
        "n_neighbors": n_neighbors,
        "weights": weights,
        "algorithm": algorithm,
        "p": p
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def bnb_objective(trial, x, y, estimator):
    alpha = trial.suggest_discrete_uniform("alpha", 0.0, 2.0, 0.001)
    binarize = trial.suggest_discrete_uniform("binarize", 0.0, 2.0, 0.001)
    params = {
        "alpha": alpha,
        "binarize": binarize,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def gnb_objective(trial, x, y, estimator):
    var_smoothing = trial.suggest_discrete_uniform("var_smoothing", 1 ** (-10), 1 ** (-8), 1 ** (-9))
    params = {
        "var_smoothing": var_smoothing,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def lda_objective(trial, x, y, estimator):
    solver = trial.suggest_categorical("solver", ["svd", "lsqr", "eigen"])
    params = {
        "solver": solver,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def qda_objective(trial, x, y, estimator):
    reg_param = trial.suggest_discrete_uniform("reg_param", 0.0, 1.0, 0.001)
    params = {
        "reg_param": reg_param,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def xgb_objective(trial, x, y, estimator):
    n_estimators = int(trial.suggest_int("n_estimators", 50, 500, 50))
    max_depth = int(trial.suggest_int("max_depth", 2, 32, 2))
    learning_rate = trial.suggest_discrete_uniform("learning_rate", 0.001, 0.5, 0.001)
    params = {
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "learning_rate": learning_rate,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


def lgbm_objective(trial, x, y, estimator):
    boosting_type = trial.suggest_categorical("boosting_type", ["gbdt", "dart", "goss"])
    num_leaves = int(trial.suggest_int("num_leaves", 8, 128, 1))
    max_depth = int(trial.suggest_int("max_depth", -1, 8, 1))
    learning_rate = trial.suggest_discrete_uniform("learning_rate", 0.001, 0.35, 0.001)
    n_estimators = int(trial.suggest_int("n_estimators", 50, 500, 50))
    params = {
        "boosting_type": boosting_type,
        "num_leaves": num_leaves,
        "max_depth": max_depth,
        "learning_rate": learning_rate,
        "n_estimators": n_estimators,
    }
    estimator.set_params(**params)
    score = cross_val_score(estimator, x, y)
    accuracy = score.mean()

    if accuracy < 0:
        score = cross_val_score(estimator, x, y, scoring="neg_mean_squared_error")
        accuracy = score.mean()
        return accuracy

    return accuracy


# Runs a study composed of the trials defined above for each estimator, and sets the best possible parameters for each estimator
def optimize_hyperparams(estimators, x, y, timeout):
    print("Optimizing hyperparameters...")
    optimized_estimators = []

    for estimator in estimators:
        if "DecisionTree" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: dt_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "RandomForest" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: rf_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "AdaBoost" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: ab_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "Bagging" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: bag_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "ExtraTrees" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: et_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "GradientBoosting" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: gb_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "GaussianProcess" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: gp_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "LogisticRegression" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: lr_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "PassiveAggressive" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: pa_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "Ridge" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: ridge_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "SGD" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: sgd_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "Perceptron" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: per_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "SVC()" == str(estimator) or "SVR()" == str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: sv_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "NuSVC" in str(estimator) or "NuSVR" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: nu_sv_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "LinearSVC" in str(estimator) or "LinearSVR" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: l_sv_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "KNeighbors" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: kn_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "BernoulliNB" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: bnb_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "GaussianNB" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: gnb_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "LinearDiscriminantAnalysis" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: lda_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        elif "QuadraticDiscriminantAnalysis" in str(estimator):
            optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
            study = optuna.create_study(direction="maximize")
            study.optimize(lambda trial: qda_objective(trial, x, y, estimator), timeout=timeout)
            estimator.set_params(**study.best_params)
            estimator.fit(x, y)
            optimized_estimators.append(estimator)
        # elif "XGB" in str(estimator):
        #     optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
        #     study = optuna.create_study(direction="maximize")
        #     study.optimize(lambda trial: xgb_objective(trial, x, y, estimator), timeout=timeout)
        #     estimator.set_params(**study.best_params)
        #     estimator.fit(x, y)
        #     optimized_estimators.append(estimator)
        # elif "LGBM" in str(estimator):
        #     optuna.logging.set_verbosity(verbosity=optuna.logging.CRITICAL)
        #     study = optuna.create_study(direction="maximize")
        #     study.optimize(lambda trial: lgbm_objective(trial, x, y, estimator), timeout=timeout)
        #     estimator.set_params(**study.best_params)
        #     estimator.fit(x, y)
        #     optimized_estimators.append(estimator)

    return optimized_estimators
