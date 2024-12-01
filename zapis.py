import csv
import time
from emokit.emotiv import Emotiv

# Ścieżka do pliku CSV
output_file = "eeg_data.csv"

# Funkcja do zapisu danych do pliku CSV
def write_csv_header(file_path, channels):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Nagłówki pliku CSV
        headers = ["Timestamp"] + channels
        writer.writerow(headers)

# Funkcja do zapisu sygnałów EEG
def save_eeg_data_to_csv(file_path, data, channels):
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        # Dane: czas + wartości z kanałów
        row = [time.time()] + [data[channel] for channel in channels]
        writer.writerow(row)

# Główna funkcja
def main():
    # Kanały EEG do zapisu (dostosuj do urządzenia)
    channels = ["F3", "F4", "P7", "P8", "T7", "T8", "O1", "O2"]
    
    # Utwórz plik CSV z nagłówkiem
    write_csv_header(output_file, channels)
    
    # Połącz się z headsetem Emotiv
    with Emotiv(display_output=False) as headset:
        print("Połączono z headsetem. Nagrywanie danych EEG...")
        try:
            # Zbieraj dane przez określony czas
            start_time = time.time()
            duration = 60  # Zbieranie danych przez 60 sekund
            while time.time() - start_time < duration:
                # Pobieranie pakietów danych
                packet = headset.dequeue()
                if packet:
                    # Zapis danych do pliku
                    save_eeg_data_to_csv(output_file, packet.sensors, channels)
        except KeyboardInterrupt:
            print("\nNagrywanie przerwane.")
        finally:
            print(f"Dane zapisane w pliku: {output_file}")

# Uruchom skrypt
if _name_ == "_main_":
    main()