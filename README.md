# MT Exercise 4: Layer Normalization for Transformer Models

This repo is just a collection of scripts showing how to install [JoeyNMT](https://github.com/joeynmt/joeynmt), download
data and train & evaluate models.

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

🧑‍🤝‍🧑 Clone this repository or your fork thereof in the desired place:

    git clone https://github.com/nneva/mt-exercise-4

💻 Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

⬇️ Download Moses for post-processing:

    ./scripts/download_install_packages.sh

⬇️ Download data:

    ./scripts/download_preprocessed_data.sh

Before training a model, you need to install `joeynmt` within the virtual environment. Please refer to the exercise instructions for the details.


⚙️ Set up for model train:

Clone this repository or your fork thereof to a separate directory:

    git clone https://github.com/nneva/joeynmt

Make sure to git checkout the respective branch.

Then go back to the **mt-exercise-4** directory.

From there run the following command to install a modified version of `joeynmt`:

    python -m pip install ../joeynmt

Make a copy of the baseline configuration in `configs` and rename it accordingly.

Make sure that `models` directory is empty, since overwriting is disabled. Or enable overwriting. 😁 

🤸 Train a model:

First rename where/what is necessary, then run:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

On cpu [2.5 GHz Quad-Core Intel Core i7, 4 cores] approx. training time **per 1 epoch**: 2 hours.

On cpu [VM Standard_D32d, 32 cores] approx. training time **per 10 epochs**: 2 hours. 🙃

Log files are reordered manually.

To get table and chart:

    python scripts/visualization.py

📝 Evaluate a trained model with

    ./scripts/evaluate.sh
