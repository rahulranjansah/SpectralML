## Description

This is a machine learning project of predicting Asteroids of SMASS survey using multiclass SVM model.

## Data type

Dataset used is Visible wavelength spectroscopy (typically 0.45-0.95 micron) for 1341 asteroids from the second phase of the SMASS survey (SMASS II).

DATA STRUCTURE WITHIN EACH FILE WITHIN SMASS DATA SET [2]

Each file has three tab-separated columns, with the format:
- Column 1: Wavelength (in microns)
- Column 2: Relative reflectance, normalized at 0.55 micron
- Column 3: Uncertainty in the relative reflectance

## Analysis process and result
Given imbalanced dataset stratified splitting, proper weighing, standard scaling, hyper-tuning using SVM kernel with certain punishment index is used to tackle the problem of Multiclass SVM classification. We considered:
- Column 1: Wavelength (in microns)
- Column 2: Relative reflectance, normalized at 0.55 micron

Producing different metrics and F1_score of 0.95.

## Source

Dataset accessed from [http://smass.mit.edu/smass.html](http://smass.mit.edu/smass.html)

## Future

We will be using more robust Machine Learning models to make the model more robust.