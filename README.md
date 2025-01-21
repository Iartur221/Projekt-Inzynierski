# README: EEG-Net Project

## Project Description
EEG-Net is a deep learning framework designed for analyzing electroencephalogram (EEG) data. The project implements 3 Siamese neural network models tailored for classifying EEG signals, supporting preprocessing, and providing visualization capabilities for neuroinformatics research.

## Features
- **Preprocessing**: Supports filtering, normalization, and segmenting EEG data.
- **Model Architecture**: Implements a custom Siamese-based architecture designed for time-series EEG data.
- **Training & Evaluation**: Provides training routines, accuracy metrics, and visualizations for model performance.
- **Visualization**: Includes plotting utilities for EEG signal slices and performance metrics.

## Requirements
The project requires the following dependencies:
- Python 3.9+
- PyTorch 1.13.1+
- NumPy
- Matplotlib
- Scikit-learn
- Pandas
- Tqdm
- Ipyfilechooser
- Graphviz

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/Iartur221/Projekt-Inzynierski.git
   ```

2. Install dependencies

3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook EEG-net.ipynb
   ```

4. Follow the instructions within the notebook to:
   - Preprocess your EEG dataset.
   - Configure model parameters.
   - Train and evaluate the model.

## Dataset
Ensure your EEG dataset is formatted as `.csv` or `.mat` files with shape `(samples, channels)`
When using your own data keep in mind of cutting your data correctly

## Usage Example
### Training
Run the `train()` function with your data:
```python
train(model, model_name, pair_datasets, criterion, optimizer, scheduler, device, person, window_length, step_size, patience=3, min_delta=0.0):
```

## Contribution
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open a discussion first.
