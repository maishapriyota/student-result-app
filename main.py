import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class DatabaseEditorApp:
    def __init__(self, root, data_file):
        self.root = root
        self.root.title("Python")

        self.data_file = data_file
        self.records = self.load_data()

        self.current_index = 0

        self.create_widgets()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                records = json.load(file)
            return records
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")
            self.root.destroy()

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.records, file, indent=4)

    def update_record(self):
        index = self.current_index
        record = self.records[index]

        confirmed_identifier = self.confirmed_identifier_entry.get().strip()
        confirmed_results = self.confirmed_results_entry.get().strip().split(',')

        if confirmed_identifier:
            record['confirmed_identifier'] = confirmed_identifier
        if confirmed_results:
            record['confirmed_results'] = [int(result) for result in confirmed_results]

        self.records[index] = record
        self.save_data()
        messagebox.showinfo("Success", "Record updated successfully.")

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create buttons
        previous_button = ttk.Button(main_frame, text="Show Previous", command=self.show_previous)
        previous_button.grid(row=8, column=0, pady=10)

        next_button = ttk.Button(main_frame, text="Show Next", command=self.show_next)
        next_button.grid(row=8, column=4, pady=10)

        update_button = ttk.Button(main_frame, text="Update Record", command=self.update_record)
        update_button.grid(row=9, column=1, columnspan=2, pady=10)

        # Search button
        search_label = ttk.Label(main_frame, text="Search Identifier:")
        search_label.grid(row=10, column=0, pady=5, sticky=tk.W)
        self.search_entry = ttk.Entry(main_frame)
        self.search_entry.grid(row=10, column=1, pady=5, sticky=tk.W)
        search_button = ttk.Button(main_frame, text="Search", command=self.search_identifier)
        search_button.grid(row=10, column=2, pady=5, sticky=tk.W)

        self.display_record()

        # Function to update record display
    def display_record(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        record = self.records[self.current_index]
        identifier = record.get('identifier', '')
        results = ', '.join(map(str, record.get('results', [])))
        confirmed_identifier = record.get('confirmed_identifier', '')
        confirmed_results = ', '.join(map(str, record.get('confirmed_results', [])))

        # Identifier
        ttk.Label(main_frame, text=f"Identifier: {identifier}").grid(row=1, column=0, sticky=tk.W)
        
        # Results
        ttk.Label(main_frame, text=f"Results: {results}").grid(row=4, column=0, sticky=tk.W)

        # Entry for confirmed identifier
        ttk.Label(main_frame, text="Confirmed Identifier:").grid(row=2, column=0, sticky=tk.W)
        self.confirmed_identifier_entry = ttk.Entry(main_frame)
        self.confirmed_identifier_entry.grid(row=2, column=1, sticky=tk.W)
        self.confirmed_identifier_entry.insert(0, confirmed_identifier)

        
        # Entry for confirmed results
        ttk.Label(main_frame, text="Confirmed Results:").grid(row=5, column=0, sticky=tk.W)
        self.confirmed_results_entry = ttk.Entry(main_frame)
        self.confirmed_results_entry.grid(row=5, column=1, sticky=tk.W)
        self.confirmed_results_entry.insert(0, ', '.join(map(str, record.get('confirmed_results', []))))

        # Identifier image 1
        identifier_image_path = record.get("identifier_image", '')  # Assuming the key for identifier image is 'identifier_image'
        if identifier_image_path:
            image = Image.open("data/image_4.jpg")
            image = image.resize((250, 100))  # Adjust size as needed
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(main_frame, image=photo)
            image_label.grid(row=1, column=3, columnspan=2, rowspan= 2 )
            image_label.image = photo
        
        # Identifier image 2
        identifier_image_path = record.get("identifier_image", '')  # Assuming the key for identifier image is 'identifier_image'
        if identifier_image_path:
            image = Image.open("data/image_6.jpg")
            image = image.resize((550, 100))  # Adjust size as needed
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(main_frame, image=photo)
            image_label.grid(row=7, column=0, columnspan=5)
            image_label.image = photo

        # Function to show previous record
    def show_previous(self):
            if self.current_index > 0:
                self.current_index -= 1
                self.display_record()


        # Function to show next record
    def show_next(self):
            if self.current_index < len(self.records) - 1:
                self.current_index += 1
                self.display_record()


# Search button
    def search_identifier():
            search_id = self.search_entry.get().strip()
            for index, record in enumerate(self.records):
                if record.get('identifier') == search_id:
                    self.current_index = index
                    self.display_record()
                    return
            messagebox.showinfo("Not Found", "Identifier not found.")

        

        

if __name__ == "__main__":
    data_file = "data/data.json"
    root = tk.Tk()
    app = DatabaseEditorApp(root, data_file)
    root.mainloop()