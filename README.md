# Retriv at BLP25 Task 2: Code Generation

Notebooks of our submissions on BLP (Bangla Language Processing) @ IJCNLP-AACL 2025, Task 2.

## Run locally

- Clone the repository

```bash
git clone git@github.com:NafiAsib/Retriv-BLP25-Task-2.git
```

- `cd` into the repository

```bash
cd Retriv-BLP25-Task-2
```

- Create development environment

```bash
python3.12 -m venv .venv    # create virtual environment
source .venv/bin/activate   # activate virtual environment
```

- Install dependencies

```bash
pip install -r requirements.txt # install all dependencis
```

- Download datasets

```bash
python download-datsets.py
```

*This script will download dataset CSV into `/data` directory*

- Change the following values to appropriate datasets location

```
PATH_TO_ORIGINAL_DEV_DATASET
PATH_TO_TRANSLATED_DATESET
PATH_TO_MBPP_CSV
```

> You may need to tweak the dependencies based on your hardware.

## Training



