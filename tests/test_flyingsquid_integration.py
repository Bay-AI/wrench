import numpy as np
from wrench.labelmodel.flyingsquid import FlyingSquid


def test_flyingsquid_integration():
    label_model = FlyingSquid()

    n_train, n_test, n_lfs = 100, 20, 5

    label_matrix_train = np.random.choice([-1, 0, 1], size=(n_train, n_lfs))
    label_matrix_test = np.random.choice([-1, 0, 1], size=(n_test, n_lfs))
    y_train = np.random.choice([-1, 0, 1], size=(n_train, n_lfs))

    label_model.fit(dataset_train=label_matrix_train, dataset_valid=y_train)
    target_value = label_model.test(label_matrix_test, metric_fn="auc")
    assert target_value
