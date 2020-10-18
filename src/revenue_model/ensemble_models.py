from itertools import combinations
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import roc_auc_score
from sklearn.metrics import mean_squared_error

best_voting_estimator = []


def ensemble_models(optimized_estimators, x_train, y_train, x_test, y_test, is_classifier, max_in_ensemble):
    print("Finding the best model ensemble...")
    all_estimator_combinations = []

    # Store combinations of length 2 to length max_in_ensemble of all estimators in a list
    for i in reversed(range(2, max_in_ensemble + 1)):
        temp_estimator_combinations = combinations(optimized_estimators, i)
        all_estimator_combinations.extend(temp_estimator_combinations)

    voting_estimators = []
    global best_voting_estimator

    if is_classifier:
        # Convert each element of all_estimator_combinations to a VotingClassifier() and store that VotingClassifier()
        # in the voting_estimators list
        for estimator_combination in all_estimator_combinations:
            names = []
            for estimator in estimator_combination:
                names.append(str(estimator))
            estimator_dict = dict(zip(names, estimator_combination))
            estimator_list = list(estimator_dict.items())
            voting_estimators.append(VotingClassifier(estimator_list))

        max_auc = -1

        # Find the voting classifier with the highest AUC
        for voting_estimator in voting_estimators:
            voting_estimator.fit(x_train, y_train)
            y_predictions = voting_estimator.predict(x_test)
            auc = roc_auc_score(y_test, y_predictions)

            if auc > max_auc:
                best_voting_estimator = voting_estimator
                max_auc = auc

        return best_voting_estimator

    else:
        # Convert each element of all_estimator_combinations to a VotingRegressor() and store that VotingRegressor()
        # in the voting_estimators list
        for estimator_combination in all_estimator_combinations:
            names = []
            for estimator in estimator_combination:
                names.append(str(estimator))
            estimator_dict = dict(zip(names, estimator_combination))
            estimator_list = list(estimator_dict.items())
            voting_estimators.append(VotingRegressor(estimator_list))

        max_score = -1

        # Find the voting regressor with the highest AUC
        for voting_estimator in voting_estimators:
            voting_estimator.fit(x_train, y_train)
            y_predictions = voting_estimator.predict(x_test)
            score = mean_squared_error(y_test.values, y_predictions)

            if score > max_score:
                best_voting_estimator = voting_estimator
                max_score = score

        return best_voting_estimator
