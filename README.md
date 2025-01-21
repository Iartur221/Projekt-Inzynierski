# README: EEG-Net Project

## Opis projektu
EEG-Net to framework głębokiego uczenia zaprojektowany do analizy danych z elektroencefalogramu (EEG). Projekt implementuje 3 modele sieci neuronowych typu Siamese, które są dostosowane do klasyfikacji sygnałów EEG, wspierają preprocessing oraz zapewniają możliwości wizualizacji dla badań neuroinformatycznych. Zawiera tekst zarówno w języku polskim, jak i angielskim, a w kodzie mogą występować mieszane języki.

## Project Description
EEG-Net is a deep learning framework designed for analyzing electroencephalogram (EEG) data. The project implements 3 Siamese neural network models tailored for classifying EEG signals, supporting preprocessing, and providing visualization capabilities for neuroinformatics research. It contains both Polish and English language in markdown cells, in the code both may be mixed up.

## Funkcje
- **Preprocessing**: Obsługuje filtrowanie, normalizację i segmentację danych EEG.
- **Model Architektura**: Implementuje niestandardową architekturę opartą na modelu Siamese, zaprojektowaną dla danych czasowych EEG.
- **Trening i ocena**: Dostarcza procedury treningowe, metryki dokładności oraz wizualizacje wyników modelu.
- **Wizualizacja**: Zawiera narzędzia do rysowania wykresów dla fragmentów sygnałów EEG oraz metryk wydajności.

## Features
- **Preprocessing**: Supports filtering, normalization, and segmenting EEG data.
- **Model Architecture**: Implements a custom Siamese-based architecture designed for time-series EEG data.
- **Training & Evaluation**: Provides training routines, accuracy metrics, and visualizations for model performance.
- **Visualization**: Includes plotting utilities for EEG signal slices and performance metrics.

## Wymagania
Projekt wymaga następujących zależności:
- Python 3.9+
- PyTorch 1.13.1+
- NumPy
- Matplotlib
- Scikit-learn
- Pandas
- Tqdm
- Ipyfilechooser
- Graphviz

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

## Jak zacząć
1. Sklonuj to repozytorium:
   ```bash
   git clone https://github.com/Iartur221/Projekt-Inzynierski.git
   ```

2. Zainstaluj zależności

3. Otwórz Jupyter Notebook:
   ```bash
   jupyter notebook EEG-net.ipynb
    ```

4. Postępuj zgodnie z instrukcjami w notebooku, aby:
   - Przygotować dane EEG.
   - Skonfigurować parametry modelu.
   - Trenować i ocenić model.


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

## Użyte dane
Zbiór danych EEG użyty w projekcie składa się z 14 kanałów i jest nagrywany z częstotliwością 128 Hz. Dane te zostały zebrane od trzech różnych osób i stanowią podstawę do treningu oraz walidacji modelu.

## Used Data
The EEG dataset used in this project consists of 14 channels and is recorded at a frequency of 128 Hz. The data has been gathered from various sources and serves as the basis for training and validating the model.

## Zbiór danych
Upewnij się, że Twój zbiór danych EEG jest sformatowany jako pliki `.csv` o kształcie `(samples, channels)`.
Przy używaniu własnych danych pamiętaj, aby odpowiednio je przyciąć.

## Dataset
Ensure your EEG dataset is formatted as `.csv` files with shape `(samples, channels)`
When using your own data keep in mind of cutting your data correctly

## Przykład użycia
### Trening
Uruchom funkcję `train()` z danymi:
```python
train(model, model_name, pair_datasets, criterion, optimizer, scheduler, device, person, window_length, step_size, patience=3, min_delta=0.0):
```

## Usage Example
### Training
Run the `train()` function with your data:
```python
train(model, model_name, pair_datasets, criterion, optimizer, scheduler, device, person, window_length, step_size, patience=3, min_delta=0.0):
```

## Wkład
Zachęcamy do wniesienia wkładu w projekt poprzez zgłaszanie problemów lub tworzenie pull requestów. W przypadku większych zmian, prosimy o otwarcie dyskusji.

## Contribution
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open a discussion first.
