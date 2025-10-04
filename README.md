# Retriv at BLP25 Task 2: Code Generation

This repository contains the notebooks and code for our submissions to [**BLP (Bangla Language Processing) Task 2**](https://blp-workshop.github.io/) at IJCNLP-AACL 2025. It focuses on [**Bangla-to-Python code generation**](https://noshinulfat.github.io/blp25_code_generation_task/#/home), evaluating multiple large language models using both **original Bangla prompts** and **translated prompts**, and includes experiments with **QLoRA fine-tuning** to enhance model performance.



### Repository Structure
```
.
├── download-datasets.py
├── few-shots-bengali-original
├── few-shot-translated
├── qlora
├── README.md
└── requirements.txt
```


### Folder Descriptions

- **`download-datasets.py`**  
  Script to download and prepare datasets used for training, evaluation, and few-shot prompting.

- **`few-shots-bengali-original/`**  
  Few-shot prompting experiments using the **original Bangla instructions**.  
  Subfolders correspond to different models:
  - `codegemma-7b/prompt.ipynb`
  - `llama-3.1/prompt.ipynb`
  - `phi-4/prompt.ipynb`
  - `qwen2.5/prompt.ipynb`
  - `qwen3/prompt.ipynb`
  - `reasonflux/prompt.ipynb`

- **`few-shot-translated/`**  
  Few-shot prompting experiments with **translated (English) prompts**.  
  Structure mirrors `few-shots-bengali-original/`.

- **`qlora/`**  
  QLoRA fine-tuning experiments using **Qwen-2.5 Coder**:
  - `fine-tune.ipynb`: Fine-tuning with QLoRA.
  - `get-csv-from-pickle.ipynb`: Convert model outputs from pickle to CSV.
  - `inference_normal.ipynb`: Standard inference.
  - `inference_feedback_guided.ipynb`: Inference with feedback-guided approach.

- **`requirements.txt`**  
  Python dependencies for notebooks and scripts.

---

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

## Citation
```
@InProceedings{BLP2025:task2:Retriv,
    author = {Asib, K M Nafi and Saha, Sourav and Hoque, Mohammed Moshiul},
    title = "Retriv at BLP-2025 Task 2:Test-Driven Feedback-Guided Framework for Bangla-to-Python Code Generation",
    booktitle = "Proceedings of the 2nd Workshop on Bangla Language Processing (BLP 2025)",
    month = dec,
    year = "2025",
    address = "Mumbai, India",
    publisher = "Association for Computational Linguistics",
}
```