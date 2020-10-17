# Trees
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

# Ensemble Methods
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor

# Gaussian Processes
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process import GaussianProcessRegressor

# Generalized Linear Models
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import Ridge
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Perceptron

# Support Vector Machines
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.svm import NuSVC
from sklearn.svm import NuSVR
from sklearn.svm import LinearSVC
from sklearn.svm import LinearSVR

# Nearest Neighbor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor

# Naive Bayes
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB

# Discriminant Analysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# XGBoost
from xgboost import XGBClassifier
from xgboost import XGBRegressor

# LightGBM
from lightgbm import LGBMClassifier
from lightgbm import LGBMRegressor

estimators = []


def build_models(is_classifier):
    print("Building models...")

    if is_classifier:
        decision_tree = DecisionTreeClassifier()
        random_forest = RandomForestClassifier()
        adaboost = AdaBoostClassifier()
        bagging = BaggingClassifier()
        extra_trees = ExtraTreesClassifier()
        gradient_boosting = GradientBoostingClassifier()
        gaussian_process_classifier = GaussianProcessClassifier()
        logistic_regression = LogisticRegression()
        passive_aggressive = PassiveAggressiveClassifier()
        ridge = RidgeClassifier()
        sgd = SGDClassifier()
        perceptron = Perceptron()
        svc = SVC()
        nu_svc = NuSVC()
        linear_svc = LinearSVC()
        k_neighbors = KNeighborsClassifier()
        bernoulli_nb = BernoulliNB()
        gaussian_nb = GaussianNB()
        linear_discriminant_analysis = LinearDiscriminantAnalysis()
        quadratic_discriminant_analysis = QuadraticDiscriminantAnalysis()
        xgb = XGBClassifier()
        lgbm = LGBMClassifier()

        estimators = [decision_tree, random_forest, adaboost, bagging, extra_trees, gradient_boosting,
                      gaussian_process_classifier, logistic_regression, passive_aggressive, ridge, sgd, perceptron, svc,
                      nu_svc, linear_svc, k_neighbors, bernoulli_nb, gaussian_nb, linear_discriminant_analysis,
                      quadratic_discriminant_analysis, xgb, lgbm]

    else:
        decision_tree = DecisionTreeRegressor()
        random_forest = RandomForestRegressor()
        adaboost = AdaBoostRegressor()
        bagging = BaggingRegressor()
        extra_trees = ExtraTreesRegressor()
        gradient_boosting = GradientBoostingRegressor()
        gaussian_process_regressor = GaussianProcessRegressor()
        lasso = Lasso()
        passive_aggressive = PassiveAggressiveRegressor()
        ridge = Ridge()
        sgd = SGDRegressor()
        svr = SVR()
        nu_svr = NuSVR()
        linear_svr = LinearSVR()
        k_neighbors = KNeighborsRegressor()
        xgb = XGBRegressor()
        lgbm = LGBMRegressor()

        estimators = [decision_tree, random_forest, adaboost, bagging, extra_trees, gradient_boosting,
                      gaussian_process_regressor, lasso, passive_aggressive, ridge, sgd, svr, nu_svr, linear_svr,
                      k_neighbors, xgb, lgbm]

    return estimators
