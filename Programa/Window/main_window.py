import tkinter as tk
import csv
from tkinter import ttk, filedialog
from Programa.Compiler.util import match_lexema


class Window:
    def __init__(self, master):
        self.master = master
        master.title("Automatas II - Proyecto Final")

        # Etiqueta con el nombre del programa
        self.title = tk.Label(master, text="Analizador Léxico")
        self.title.pack()

        # Barra para examinar archivos
        self.search_button = tk.Button(master, text="Examinar Archivos", command=self.file_search)
        self.search_button.pack()

        # Botón para abrir la siguiente ventana
        self.lex_button = tk.Button(master, text="Tabla", command=self.lex_table)
        self.lex_button.pack()

    def file_search(self):
        file_path = filedialog.askopenfilename(title="Seleccionar Archivo",initialdir='./Programa')
        print("Ruta del archivo seleccionado:", file_path)
        self.file_content = self.read_file(file_path)
        print("Contenido del archivo:", self.file_content)
        self.write_file(self.file_content)

    # lex table
    def lex_table(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        ruta_archivo = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[("Archivos CSV", "*.csv")])

        if not ruta_archivo:
            return  # El usuario canceló la selección

        # Crear la segunda ventana
        ventana2 = tk.Toplevel(self.master)
        ventana2.title("Tabla de léxemas")

        # Crear la tabla con el contenido del archivo CSV
        tabla = ttk.Treeview(ventana2)
        tabla["columns"] = ("#1", "#2")  # Definir las columnas

        # Configurar las columnas
        tabla.column("#0", width=50, minwidth=50, stretch=tk.NO)
        tabla.column("#1", width=150, minwidth=150, stretch=tk.NO)
        tabla.column("#2", width=150, minwidth=150, stretch=tk.NO)
        tabla.heading("#0", text="Índice")
        tabla.heading("#1", text="Símbolo Antes de Coma")
        tabla.heading("#2", text="Después de Coma")

        # Leer el contenido del archivo CSV
        with open(ruta_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for i, fila in enumerate(lector_csv):
                if len(fila) == 2:
                    antes_coma, despues_coma = fila
                    print(fila)
                    tabla.insert( "", i , text=i, values=(antes_coma, despues_coma))
                else:
                    print(f"La fila {i+1} no tiene el formato esperado")

        tabla.pack(expand=True, fill="both")

    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = [line.strip() for line in file.readlines()]
            return {word: match_lexema(word) for line in content for word in line.split()}
        except Exception as e:
            print("Error al leer el archivo:", e)
            return []
    def write_file(self, content, file_path='./Programa/lexemas.csv'):
        """
        Escribe el contenido en un archivo.

        Parameters:
            content (str): El contenido a escribir en el archivo.
            file_path (str): Ruta del archivo. Por defecto, './Programa/lexemas.txt'.
        
        Raises:
            FileNotFoundError: Si el directorio no existe.
            PermissionError: Si no se tienen permisos para escribir en el archivo.
        """
        try:            
            with open(file_path, 'w', encoding='utf-8') as file:
                for key, value in content.items():
                    file.write(f"{key},{value}\n")
        except FileNotFoundError:
            raise FileNotFoundError(f"El directorio para {file_path} no existe.")
        except PermissionError:
            raise PermissionError(f"No se tienen permisos para escribir en {file_path}.")
        except Exception as e:
            print(f"Error al escribir el archivo: {e}")
            # Puedes decidir si quieres propagar o manejar el error de alguna otra manera


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
