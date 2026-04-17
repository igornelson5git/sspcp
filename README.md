# Secondary Structure Prediction of Proteins (SSPCP)

**Author:** Igor Nelson
**Degree:** MSc in Computational Biology
**Institution:** University of Coimbra

---

## 📌 Overview

This project explores multiple machine learning and deep learning approaches for **protein secondary structure prediction**, culminating in a novel method:

> **SSPCP — Secondary Structure of Physicochemical Clustered Proteins**

The work compares traditional and deep learning models and introduces a clustering-based ensemble strategy that improves prediction performance.

# Secondary Structure Prediction of Proteins (SSPCP)

> ⚠️ **Important Setup Requirement**
>
> This project depends on external bioinformatics tools for feature extraction.
>
> - Install **PSI-BLAST** (NCBI BLAST+)
> - Download protein databases
> - Generate **PSSM matrices**
>
> 🔧 Version used: **NCBI BLAST+ 2.13.0+**
>
> https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.13.0/
>
> ⚠️ Without PSSM features, the models will not work.
---

## 🧬 Problem Statement

Protein secondary structure prediction is a fundamental challenge in bioinformatics. The goal is to classify each amino acid residue into one of three classes:

* **H** – α-helix
* **E** – β-sheet
* **C** – Coil

Despite advances, this remains difficult due to:

* Complex folding mechanisms
* Limited experimental data
* Ambiguity between structural classes

---

## 🚀 Methods Implemented

This project evaluates **five approaches**:

### 1. Baseline – SVM (RBF Kernel)

* Uses **PSSM features**
* Hyperparameters tuned:

  * `C = 10.0`
  * `gamma = 0.001`
* Sliding window size: `w = 13`

---

### 2. Convolutional Neural Network (CNN)

* Input: 2D PSSM matrices
* Architecture:

  * Conv Layer (500 filters, 5×5)
  * MaxPooling (2×2)
  * Conv Layer (100 filters, 2×2)
  * Dense (50 neurons)
  * Output (Softmax, 3 classes)
* Optimizer: Adam
* Loss: Categorical Cross-Entropy

---

### 3. Long Short-Term Memory (LSTM)

* Captures sequential dependencies in amino acids
* Architecture:

  * LSTM layers (400 → 600 units)
  * Dense layer (100 neurons)
  * Output layer (3 classes)

---

### 4. CNN + LSTM Ensemble

* Combines predictions:

  ```
  P = a * P_CNN + b * P_LSTM
  ```

  where:

  * `a = 0.42`
  * `b = 0.58`

---

### 5. SSPCP (Proposed Method) ⭐

A novel approach based on:

#### Step 1: Physicochemical Feature Extraction

* Amino acids grouped into **7 categories**
* Feature vector per protein:

  ```
  [length, %group1, %group2, ..., %group7]
  ```

#### Step 2: Dimensionality Reduction

* PCA (2 components)

#### Step 3: Protein Clustering

* Clustering based on physicochemical similarity

#### Step 4: Specialized CNN Models

* Each cluster → dedicated CNN

#### Step 5: Meta Neural Network

* Combines outputs from all CNNs

💡 **Key Idea:**
Proteins with similar physicochemical properties may share structural patterns.

---

## 📊 Dataset

* **Dataset:** 25pdb
* **Total proteins (after preprocessing):** 1427
* **Train/Test split:** 70% / 30%

### Preprocessing Steps:

* DSSP used for structure labeling
* Reduced from 8 → 3 classes (H, E, C)
* Removed:

  * Sequences < 30 amino acids
  * Duplicates

---

## 🔬 Feature Engineering

### PSSM (Position-Specific Scoring Matrix)

* Generated using **PSI-BLAST**
* Parameters:

  * Database: SwissProt
  * Iterations: 3
  * Threshold: 0.001

### Sliding Window

* Window size: `w = 13`
* Feature size:

  * ML: 260 (13 × 20)
  * CNN: 13 × 20 matrix

---

## 📈 Results (Q3 Accuracy)

| Method     | Q3 Score   |
| ---------- | ---------- |
| CNN        | 70.11%     |
| LSTM       | 69.25%     |
| CNN + LSTM | 70.71%     |
| **SSPCP**  | **70.91%** |

---

## 🧪 Practical Application

The SSPCP model was tested on:

* **Protein:** PET hydrolase (*Ideonella sakaiensis*)
* Accuracy: **73%**

### Observations:

* Errors occur near class transitions
* Performance limited by:

  * Dataset size
  * local sequence ambiguity

---

## 🧠 Key Insights

* PSSM features significantly improve performance
* Deep learning outperforms traditional ML
* Ensemble methods provide consistent gains
* Clustering + specialization (SSPCP) improves accuracy

---

## ⚠️ Limitations

* Limited dataset size
* Imbalanced classes (few β-sheets)
* High computational cost
* Incomplete reproducibility from referenced works

---

## 🔮 Future Work

* Use larger datasets (e.g., non-redundant DB)
* Improve clustering strategies
* Combine multiple model types per cluster
* Hyperparameter optimization per cluster
* Better handling of class imbalance

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* TensorFlow / Keras
* PSI-BLAST
* DSSP

---

## 📂 Project Structure (Suggested)

```
.
├── data/
├── models/
│   ├── svm/
│   ├── cnn/
│   ├── lstm/
│   └── sspcp/
├── preprocessing/
├── notebooks/
├── results/
├── README.md
└── requirements.txt
```

---

## 📜 References

Key references include:

* PSI-BLAST (Altschul et al.)
* DSSP (Kabsch & Sander)
* CNN + LSTM model (Cheng et al.)
* Physicochemical clustering (Shen et al.)

(See full list in paper)

---

## 🤝 Contributions

Feel free to:

* Open issues
* Submit pull requests
* Suggest improvements

---

## 📬 Contact

**Igor Nelson**
📧 [igornelson5@hotmail.com](mailto:igornelson5@hotmail.com)

---

⭐ If you find this project useful, consider starring the repo!
