import torch
from typing import Dict, Callable
from torchvision import transforms, datasets

import numpy as np

from sklearn.datasets import load_iris, load_wine, make_classification

BASE_DIR = "data/raw/"


def load_audit():
    """Load the audit dataset"""
    data = np.loadtxt(BASE_DIR + "audit_risk.csv", delimiter=",", comments="#")
    X = data[:, 0:-2]
    y = data[:, -1]
    return X, y


def load_diabetes():
    """
    The Pima Indians Diabetes Dataset involves predicting the onset of diabetes within 5 years in Pima Indians given medical details.

    It is a binary (2-class) classification problem. The number of observations for each class is not balanced. There are 768 observations with 8 input variables and 1 output variable. Missing values are believed to be encoded with zero values. The variable names are as follows:

    Number of times pregnant.
    Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
    Diastolic blood pressure (mm Hg).
    Triceps skinfold thickness (mm).
    2-Hour serum insulin (mu U/ml).
    Body mass index (weight in kg/(height in m)^2).
    Diabetes pedigree function.
    Age (years).
    Class variable (0 or 1).
    The baseline performance of predicting the most prevalent class is a classification accuracy of approximately 65%. Top results achieve a classification accuracy of approximately 77%.
    """
    data = np.loadtxt(BASE_DIR + "diabetes.csv", delimiter=",")
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y


def load_sonar():
    """
    The Sonar Dataset involves the prediction of whether or not an object is a mine or a rock given the strength of sonar returns at different angles.

    It is a binary (2-class) classification problem. The number of observations for each class is not balanced. There are 208 observations with 60 input variables and 1 output variable. The variable names are as follows:

    Sonar returns at different angles
    …
    Class (M for mine and R for rock)
    The baseline performance of predicting the most prevalent class is a classification accuracy of approximately 53%. Top results achieve a classification accuracy of approximately 88%.
    """
    data = np.loadtxt(BASE_DIR + "sonar.csv", delimiter=",")
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y


def load_wheat_2d():
    """
    The Wheat Seeds Dataset involves the prediction of species given measurements of seeds from different varieties of wheat.

    It is a binary (2-class) classification problem. The number of observations for each class is balanced. There are 210 observations with 7 input variables and 1 output variable. The variable names are as follows:

    Area.
    Perimeter.
    Compactness
    Length of kernel.
    Width of kernel.
    Asymmetry coefficient.
    Length of kernel groove.
    Class (1, 2, 3).
    The baseline performance of predicting the most prevalent class is a classification accuracy of approximately 28%.

    """
    data = np.loadtxt(BASE_DIR + "wheat.csv")
    X = data[:, 0:-1]
    y = data[:, -1]

    c0 = 1
    c1 = 3
    mask = (y == c0) | (y == c1)
    X = X[mask]
    y = y[mask]
    y[y == c0] = 0
    y[y == c1] = 1

    return X, y


def load_ionosphere():
    """
    The Ionosphere Dataset requires the prediction of structure in the atmosphere given radar returns targeting free electrons in the ionosphere.

It is a binary (2-class) classification problem. The number of observations for each class is not balanced. There are 351 observations with 34 input variables and 1 output variable. The variable names are as follows:

17 pairs of radar return data.
…
Class (g for good and b for bad).
The baseline performance of predicting the most prevalent class is a classification accuracy of approximately 64%. Top results achieve a classification accuracy of approximately 94%."""
    data = np.loadtxt(BASE_DIR + "ionosphere.csv", delimiter=",")
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y


def load_banknotes():
    """
    The Banknote Dataset involves predicting whether a given banknote is authentic given a number of measures taken from a photograph.

    It is a binary (2-class) classification problem. The number of observations for each class is not balanced. There are 1,372 observations with 4 input variables and 1 output variable. The variable names are as follows:

    Variance of Wavelet Transformed image (continuous).
    Skewness of Wavelet Transformed image (continuous).
    Kurtosis of Wavelet Transformed image (continuous).
    Entropy of image (continuous).
    Class (0 for authentic, 1 for inauthentic).
    The baseline performance of predicting the most prevalent class is a classification accuracy of approximately 50%.
    """
    data = np.loadtxt(BASE_DIR + "banknotes.csv", delimiter=",")
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y


def load_iris_3d():
    return load_iris(return_X_y=True)


def load_iris_2d():
    X, y = load_iris(return_X_y=True)
    mask = (y == 1) | (y == 2)
    X = X[mask]
    y = y[mask]
    y[y == 1] = 0
    y[y == 2] = 1
    return X, y


def load_wine_3d():
    X, y = load_wine(return_X_y=True)
    return X, y


def load_wine_2d():
    X, y = load_wine(return_X_y=True)
    mask = (y == 0) | (y == 2)
    X = X[mask]
    y = y[mask]
    y[y == 0] = 0
    y[y == 2] = 1
    return X, y


def make_load_synth(
    n_features,
    n_informative,
    n_redundant,
    n_clusters_per_class,
    class_sep,
    n_datapoints=3000,
) -> Callable:
    """
    Create a synthetic dataset.

    Args:
        n_features (int): Number of input features.
        n_informative (int): Number of informative input features.
        n_redundant (int): Number of redundant input features.
        n_clusters_per_class (int): Number of cluster per class.
        class_sep (float): Class separation factor.
        n_datapoints (int): Number of datapoints (default: 3000).

    Returns:
        Callable: Dataset loader which returns (X, y).
    """

    def load_synth():
        X, y = make_classification(
            n_samples=n_datapoints,
            n_features=n_features,
            n_informative=n_informative,
            n_redundant=n_redundant,
            n_classes=2,
            n_clusters_per_class=2,
            class_sep=class_sep,
            random_state=42,
        )
        return X, y

    return load_synth


def load_dataset_map() -> Dict[str, Callable]:
    """
    Get a map of datasets.

    Returns:
        Dict[str, Callable]: Key: Dataset name, Value: loader function which returns (X, y).
    """
    dss = {
        "iris-2d": load_iris_2d,
        "wine-2d": load_wine_2d,
        "diabetes": load_diabetes,
        "audit": load_audit,
        "banknotes": load_banknotes,
        "ionosphere": load_ionosphere,
        "sonar": load_sonar,
        "wheat-2d": load_wheat_2d,
    }
    for n_feats in [8, 64, 128, 256, 512, 1024, 2048]:
        dss["synth-" + str(n_feats) + "-easy"] = make_load_synth(
            n_features=n_feats,
            n_informative=n_feats,
            n_redundant=0,
            n_clusters_per_class=2,
            class_sep=0.5,
        )
        dss["synth-" + str(n_feats) + "-hard"] = make_load_synth(
            n_features=n_feats,
            n_informative=int(n_feats / 4),
            n_redundant=int(n_feats / 2),
            n_clusters_per_class=2,
            class_sep=0.01,
        )
    return dss


def get_mnist_loaders(use_cuda, ARGS):
    """
    Get the MNIST pytorch data loader.
    
    Args:
        use_cuda: Use cuda flag.
        ARGS: Arguments.
    """

    kwargs = {"num_workers": 1, "pin_memory": True} if use_cuda else {}

    # Train data loader
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            "../data",
            train=True,
            download=True,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
            ),
        ),
        batch_size=ARGS.batch_size,
        shuffle=True,
        **kwargs,
    )

    # Test data loader
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            "../data",
            train=False,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
            ),
        ),
        batch_size=ARGS.test_batch_size,
        shuffle=True,
        **kwargs,
    )
    return train_loader, test_loader
