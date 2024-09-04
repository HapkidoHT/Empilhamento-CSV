import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def combine_csv_files(directory, progress_bar):
    # Lista para armazenar os DataFrames de cada arquivo CSV
    data_frames = []

    # Obter a lista de arquivos CSV no diretório
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    total_files = len(files)

    # Loop através de todos os arquivos no diretório
    for i, filename in enumerate(files):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)  # Usando pd.read_csv para ler arquivos CSV
        data_frames.append(df)

        # Atualizar a barra de progresso
        progress_bar['value'] = ((i + 1) / total_files) * 100
        root.update_idletasks()

    # Concatenar todos os DataFrames em um único DataFrame
    combined_df = pd.concat(data_frames, ignore_index=True)
    
    # Caminho para salvar o arquivo combinado no diretório selecionado
    save_path = os.path.join(directory, 'arquivo_combinado.csv')
    
    # Salvar o DataFrame combinado em um novo arquivo CSV
    combined_df.to_csv(save_path, index=False)

    return save_path


def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        try:
            progress_bar['value'] = 0
            save_path = combine_csv_files(directory, progress_bar)  # Alteração para combinar CSVs
            messagebox.showinfo("Sucesso", f"Os arquivos CSV foram combinados com sucesso!\nSalvo em: {save_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao combinar os arquivos CSV:\n{e}")


# Configurar a interface gráfica
root = tk.Tk()
root.title("Combinar Planilhas Excel")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Selecione o diretório onde estão as planilhas:")
label.pack(pady=10)

button = tk.Button(frame, text="Selecionar Diretório", command=select_directory)
button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=20)

root.mainloop()