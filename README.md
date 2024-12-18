# MeowCare
AI Diagnosis Technology for Eye Diseases Using Cat Eye Images


# Project Overview

## UI Files
These files are responsible for rendering the user interface. They are auto-generated from files located in the `UI` folder:
- `mainwindow.py`
- `logindialog.py`
- `resultdialog.py`
- `diagdialog.py`
- `catdialog.py`
- `imgFrame.py`

## Controllers
These files handle button events and user interactions:
- `loginctrl.py`
- `mainctrl.py`
- `resultctrl.py`
- `diagctrl.py`
- `catctrl.py`

## Database Interaction
- `petdb.py`: A class for working with the database.

## Model Preparation
- `tabmodel.py`: A class for preparing data for display.
- `callmodel.py`: A class for handling the AI model. It loads the model from a file, sets the image, and performs analysis in the `exec` method.

## Utilities
- `importIMG.py`: Loads images of diseases.
- `parseJSON.py`: Loads the model into the database. This is a separate module that loads all data into the database from JSON and image files.

# Analysis Workflow
The analyzer is launched in the `startClick` method in `diagctrl.py`. It works as follows:
1. An instance of the `catPredictor` class from `callmodel.py` is created.
2. The `exec` method is executed, and the results are saved to the database.
3. These results are then read from the database and displayed in the `resultdialog`.
