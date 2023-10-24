# Gauss-Seidel Linear Equation Solver



A Python program for solving systems of linear equations using the Gauss-Seidel method. This program checks for diagonal dominance and, if needed, modifies the equations to ensure convergence. It also provides a user-friendly GUI for input and result display.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)


## Introduction

This Python program helps you solve systems of linear equations using the Gauss-Seidel method. It's designed to be user-friendly, offering a graphical user interface (GUI) for easy input and result visualization. Whether you have a diagonally dominant system or not, this program has you covered.

## Features

- **Gauss-Seidel Solver**: Easily solve systems of linear equations using the Gauss-Seidel method.

- **Diagonal Dominance Check**: Automatically checks if the input matrix is diagonally dominant. If not, it modifies the equations to ensure convergence.

- **User-Friendly GUI**: Provides a GUI for users to input matrix A, vector B, tolerance, and maximum iterations.

- **Results Display**: Shows the results of the solver, including the solution, iterations, and information about diagonal dominance.

- **Iteration Monitoring**: Displays intermediate results after each iteration, helping users track the progress of the solver.

- **Customizable Tolerance and Max Iterations**: Allows users to specify the tolerance and the maximum number of iterations.

- **Error Handling**: Includes error handling to catch and display any issues that may arise during the solving process.

- **README Template**: Offers a template for creating beautiful README files for other projects.

## Getting Started

### Prerequisites

To run this program, you need:

- Python (version 3.6 or higher)
- The `numpy` library
- The `tkinter` library (included with Python)

##Usage

    Launch the program using the provided installation instructions.
    Enter the coefficients of matrix A, vector B, tolerance, and maximum iterations.
    Click the "Solve" button.
    The program will display the results, including whether the equations are diagonally dominant, the solution, and iteration details.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo.git

##Acknowledgments

    NumPy - A fundamental package for scientific computing with Python.
    tkinter - The standard Python interface to the Tk GUI toolkit.
