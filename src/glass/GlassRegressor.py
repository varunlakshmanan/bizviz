from build_models import build_models
from optimize_hyperparams import optimize_hyperparams
from ensemble_models import ensemble_models
from sklearn.metrics import roc_auc_score

global ensemble


class GlassRegressor:
    def __init__(self):
        pass

    def fit(self, x_train, y_train, x_test, y_test, timeout=5, max_in_ensemble=4):
        is_classifier = False
        global ensemble
        ensemble = ensemble_models(optimize_hyperparams(build_models(is_classifier), x_train, y_train, timeout),
                                   x_train, y_train, x_test, y_test, is_classifier, max_in_ensemble)
        return ensemble

    def predict(self, x_test):
        y_predictions = ensemble.predict(x_test)
        return y_predictions

    def describe(self, x_test=None, y_test=None):
        if x_test is None or y_test is None:
            print(ensemble.get_params(self))
        else:
            y_predictions = ensemble.predict(x_test)
            auc = roc_auc_score(y_test, y_predictions)
            print("Highest AUC: " + str(auc))
            print(ensemble.get_params(self))
