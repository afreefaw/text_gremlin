import tkinter as tk
from tkinter import ttk, filedialog
from pathlib import Path
from typing import Optional, Set

from document_extractor.processor import DocumentProcessor

class TextGremlinGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Gremlin")
        self.root.geometry("600x500")
        
        # State variables
        self.input_path: Optional[Path] = Path("sample_docs").absolute()
        self.output_path: Optional[Path] = Path("output/extracted_text.json").absolute()
        self.selected_types: Set[str] = {"pdf", "pptx", "docx"}
        self.is_processing = False
        self.should_cancel = False
        self.processor = DocumentProcessor()
        
        # Set default paths in the GUI
        self.input_path_var = tk.StringVar(value=str(self.input_path))
        self.output_path_var = tk.StringVar(value=str(self.output_path))
        
        self._create_widgets()
        self._setup_layout()
    
    def _create_widgets(self):
        # Input section
        self.input_frame = ttk.LabelFrame(self.root, text="Input", padding="5")
        self.input_entry = ttk.Entry(
            self.input_frame,
            textvariable=self.input_path_var,
            width=50
        )
        self.input_button = ttk.Button(
            self.input_frame,
            text="Browse",
            command=self._browse_input
        )
        
        # Output section
        self.output_frame = ttk.LabelFrame(self.root, text="Output", padding="5")
        self.output_entry = ttk.Entry(
            self.output_frame,
            textvariable=self.output_path_var,
            width=50
        )
        self.output_button = ttk.Button(
            self.output_frame,
            text="Browse",
            command=self._browse_output
        )
        
        # Options section
        self.options_frame = ttk.LabelFrame(self.root, text="Options", padding="5")
        
        # File type checkboxes
        self.pdf_var = tk.BooleanVar(value=True)
        self.pdf_check = ttk.Checkbutton(
            self.options_frame,
            text="PDF",
            variable=self.pdf_var,
            command=lambda: self._update_types("pdf")
        )
        
        self.pptx_var = tk.BooleanVar(value=True)
        self.pptx_check = ttk.Checkbutton(
            self.options_frame,
            text="PPTX",
            variable=self.pptx_var,
            command=lambda: self._update_types("pptx")
        )
        
        self.docx_var = tk.BooleanVar(value=True)
        self.docx_check = ttk.Checkbutton(
            self.options_frame,
            text="DOCX",
            variable=self.docx_var,
            command=lambda: self._update_types("docx")
        )
        
        # Recursive option
        self.recursive_var = tk.BooleanVar(value=True)
        self.recursive_check = ttk.Checkbutton(
            self.options_frame,
            text="Include subfolders",
            variable=self.recursive_var
        )
        
        # Progress section
        self.progress_frame = ttk.LabelFrame(self.root, text="Progress", padding="5")
        self.progress_var = tk.StringVar(value="Ready")
        self.progress_label = ttk.Label(
            self.progress_frame,
            textvariable=self.progress_var
        )
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            mode='indeterminate'
        )
        
        # Control buttons
        self.button_frame = ttk.Frame(self.root)
        self.extract_button = ttk.Button(
            self.button_frame,
            text="Extract Text",
            command=self._start_extraction
        )
        self.cancel_button = ttk.Button(
            self.button_frame,
            text="Cancel",
            command=self._cancel_extraction,
            state="disabled"
        )
    
    def _setup_layout(self):
        # Input section
        self.input_frame.pack(fill="x", padx=5, pady=5)
        self.input_entry.pack(side="left", padx=5)
        self.input_button.pack(side="left", padx=5)
        
        # Output section
        self.output_frame.pack(fill="x", padx=5, pady=5)
        self.output_entry.pack(side="left", padx=5)
        self.output_button.pack(side="left", padx=5)
        
        # Options section
        self.options_frame.pack(fill="x", padx=5, pady=5)
        self.pdf_check.pack(side="left", padx=5)
        self.pptx_check.pack(side="left", padx=5)
        self.docx_check.pack(side="left", padx=5)
        self.recursive_check.pack(side="left", padx=20)
        
        # Progress section
        self.progress_frame.pack(fill="x", padx=5, pady=5)
        self.progress_label.pack(fill="x", padx=5, pady=2)
        self.progress_bar.pack(fill="x", padx=5, pady=2)
        
        # Control buttons
        self.button_frame.pack(fill="x", padx=5, pady=5)
        self.extract_button.pack(side="left", padx=5)
        self.cancel_button.pack(side="left", padx=5)
    
    def _browse_input(self):
        path = filedialog.askdirectory(title="Select Input Directory")
        if path:
            self.input_path = Path(path)
            self.input_path_var.set(str(self.input_path))
    
    def _browse_output(self):
        path = filedialog.asksaveasfilename(
            title="Select Output File",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if path:
            self.output_path = Path(path)
            self.output_path_var.set(str(self.output_path))
    
    def _update_types(self, file_type: str):
        if file_type == "pdf":
            if self.pdf_var.get():
                self.selected_types.add("pdf")
            else:
                self.selected_types.discard("pdf")
        elif file_type == "pptx":
            if self.pptx_var.get():
                self.selected_types.add("pptx")
            else:
                self.selected_types.discard("pptx")
        elif file_type == "docx":
            if self.docx_var.get():
                self.selected_types.add("docx")
            else:
                self.selected_types.discard("docx")
    
    def _start_extraction(self):
        if not self.input_path or not self.output_path:
            self.progress_var.set("Error: Please select input and output paths")
            return
        
        if not self.selected_types:
            self.progress_var.set("Error: Please select at least one file type")
            return
        
        self.is_processing = True
        self.should_cancel = False
        self.extract_button.configure(state="disabled")
        self.cancel_button.configure(state="normal")
        self.progress_bar.start(10)
        
        self._process_documents()
    
    def _cancel_extraction(self):
        self.should_cancel = True
        self.progress_var.set("Cancelling...")
    
    def _process_documents(self):
        try:
            doc_count = 0
            for doc in self.processor.process_documents(
                str(self.input_path),
                str(self.output_path),
                recursive=self.recursive_var.get(),
                file_types=list(self.selected_types)
            ):
                if self.should_cancel:
                    self.progress_var.set("Extraction cancelled")
                    break
                
                doc_count += 1
                self.progress_var.set(f"Processing: {doc['file_name']}")
                self.root.update()
            
            if not self.should_cancel:
                self.progress_var.set(f"Completed: {doc_count} documents processed")
        
        except Exception as e:
            self.progress_var.set(f"Error: {str(e)}")
        
        finally:
            self.is_processing = False
            self.progress_bar.stop()
            self.extract_button.configure(state="normal")
            self.cancel_button.configure(state="disabled")
            self.root.update()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TextGremlinGUI()
    app.run()