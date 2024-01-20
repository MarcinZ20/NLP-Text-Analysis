# NLP Text Analysis

`Created by: Marcin Zub`

## Overview
This project is part of the AGH UST course *Natural Language Processing in Artificial Intelligence Systems*. It focuses on text analysis using Natural Language Processing (NLP) techniques.

Texts that are being analyzed are:
1. `Manuskrypt Wojnicza` by unknown author
2. `One hundred years of solitude` by Gabriel Garcia Marquez

For each of them, the program performs the following operations:
1. Check weather or not it's following the Zipf law
2. Create the N-gram array with added incidence
3. Create the collocation table

## Project Structure

The project has the following structure:

- `src/`: Contains the source code for the project.
  - `analysis.ipynb`: Jupyter notebook for data analysis.
  - `data/`: Contains the project data
    - `output/`: Here are output files
    - `raw/`: Raw text files if needed
  - `models/`: Contains text model
    - `text.py`: Implements the text model with read functions 
  - `processing/`: Contains Python classes for data processing.
    - `zipf.py`: Implements the Zipf's law functionality.
  - `tests/`: Contains unit tests for the project.
- `requirements.txt`: Lists the Python dependencies required by the project.

## Getting Started

1. Clone the repository:

```sh
git clone https://github.com/MarcinZ20/NLP-Text-Analysis.git
```

2. Install the dependencies using pip:

```sh
pip install -r requirements.txt
```

3. Run the Jupyter notebook

```sh
jupyter notebook src/analysis.ipynb
```

#### License
This project is licensed under the terms of the LICENSE file.

#### More Information
For more information about the project, please refer to the src/analysis.ipynb and src/processing/zipf.py files.
