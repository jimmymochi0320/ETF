import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from app.app_controller import AppController

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Layout-Aware PDF Translator")
        self.controller = AppController(self.add_log, self.update_progress)
        self._build()

    def _build(self):
        self.input_var=tk.StringVar(); self.output_var=tk.StringVar(); self.api_var=tk.StringVar(); self.service_var=tk.StringVar(value="dummy")
        self.ocr_var=tk.BooleanVar(value=False); self.overflow_var=tk.StringVar(value="0")
        frm=ttk.Frame(self.root,padding=10); frm.pack(fill='both',expand=True)
        for i,(lab,var,cb) in enumerate([
            ("Input PDF",self.input_var,self.pick_input),
            ("Output Dir",self.output_var,self.pick_output),
        ]):
            ttk.Label(frm,text=lab).grid(row=i,column=0,sticky='w'); ttk.Entry(frm,textvariable=var,width=50).grid(row=i,column=1,sticky='ew'); ttk.Button(frm,text="Browse",command=cb).grid(row=i,column=2)
        ttk.Label(frm,text="Translator").grid(row=2,column=0,sticky='w')
        ttk.Combobox(frm,textvariable=self.service_var,values=["dummy","openai","deepl"],state='readonly').grid(row=2,column=1,sticky='ew')
        ttk.Label(frm,text="API Key").grid(row=3,column=0,sticky='w'); ttk.Entry(frm,textvariable=self.api_var,show='*').grid(row=3,column=1,sticky='ew')
        ttk.Checkbutton(frm,text="Enable OCR",variable=self.ocr_var).grid(row=4,column=1,sticky='w')
        self.progress=ttk.Progressbar(frm,maximum=100); self.progress.grid(row=5,column=0,columnspan=3,sticky='ew',pady=6)
        ttk.Label(frm,text="Overflow").grid(row=6,column=0,sticky='w'); ttk.Label(frm,textvariable=self.overflow_var).grid(row=6,column=1,sticky='w')
        self.log=tk.Text(frm,height=14); self.log.grid(row=7,column=0,columnspan=3,sticky='nsew')
        ttk.Button(frm,text="Start",command=self.start).grid(row=8,column=2,sticky='e',pady=6)
        frm.columnconfigure(1,weight=1); frm.rowconfigure(7,weight=1)

    def pick_input(self): self.input_var.set(filedialog.askopenfilename(filetypes=[("PDF","*.pdf")]))
    def pick_output(self): self.output_var.set(filedialog.askdirectory())
    def add_log(self,msg): self.log.insert('end', msg + "\n"); self.log.see('end'); self.root.update_idletasks()
    def update_progress(self,cur,total): self.progress['value']=0 if total==0 else cur*100/total; self.root.update_idletasks()
    def start(self):
        try:
            res=self.controller.run(self.input_var.get(),self.output_var.get(),self.service_var.get(),self.api_var.get(),self.ocr_var.get())
            self.overflow_var.set(str(res.get('overflow_count',0)))
            messagebox.showinfo("Done",f"Output: {res['output_pdf']}")
        except Exception as e:
            self.add_log(f"ERROR: {e}")
            messagebox.showerror("Error",str(e))

def run_app():
    root=tk.Tk(); root.geometry('900x620'); App(root); root.mainloop()
