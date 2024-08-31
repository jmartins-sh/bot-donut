# Tutorial

> All commands must be executed in the root directory of the repository

You must have installed python in your machine. After python's installation you have to create a virtual env for you, just execute the following command:

`python -m venv .venv`

When finished the env creation, install the packages from `requirements.txt` file, running the following command:

`pip install -r ./requirements.txt`

After that just run the command providing the right arguments:

1. Referral Link
2. Number of times to try to create the emails

`python ./main.py REFERRAL_LINK_HERE NUMBER_HERE`
