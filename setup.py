import setuptools


setuptools.setup(
    name="clustering_shrinkage_estimator",
    version="v0.0.3-beta",
    author="José Antonio Duarte Mendieta",
    author_email="jose.duarte@cimat.mx",
    description="Function to estimate the oracle RIE corrrelation estimator of a dataset",
    packages = ['csestimator'],
    install_requires=[
        "pandas",
        "numpy",
        "sklearn"
    ]
)