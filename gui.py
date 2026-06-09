from tkinter import *
from tkinter import ttk
from scheduler import *


class SchedulingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Scheduling")
        self.root.geometry("900x700")
        self.root.config(bg="white")
        self.burst_entries = []
        self.arrival_entries = []
        
        # Title
        Label(Frame(root, bg="white"), text="Process Scheduling", 
              font=("Times New Roman", 20, "bold"), bg="white").pack(pady=15)
        
        # Input section
        frame = Frame(root, bg="white")
        frame.pack(pady=10, padx=20, fill="x")
        Label(frame, text="Number of Processes:", font=("Times New Roman", 10), bg="white").grid(row=0, column=0, padx=5)
        self.entry_num = Entry(frame, width=15, font=("Times New Roman", 10))
        self.entry_num.grid(row=0, column=1, padx=5)
        Button(frame, text="Create Entries", command=self.create_entries, bg="lightblue").grid(row=0, column=2, padx=20)
        
        # Process entries frame
        self.frame_input = Frame(root, bg="white")
        self.frame_input.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Result section
        frame_result = Frame(root, bg="white")
        frame_result.pack(pady=10, padx=20, fill="both", expand=True)
        
        cols = ("Process ID", "Burst Time", "Arrival Time", "Waiting Time", "Turnaround Time")
        self.tree = ttk.Treeview(frame_result, columns=cols, height=8, show="headings")
        self.tree.pack(fill="both", expand=True)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor="center")
        
        self.label_avg = Label(frame_result, text="Average Waiting Time: -", 
                              font=("Times New Roman", 10, "bold"), bg="white")
        self.label_avg.pack(pady=5)
        
        # Calculate button
        Button(root, text="Calculate Schedule", command=self.calculate_schedule,
               bg="lightgreen", padx=20, pady=5).pack(pady=10)
    
    def create_entries(self):
        for w in self.frame_input.winfo_children():
            w.destroy()
        self.burst_entries.clear()
        self.arrival_entries.clear()
        
        try:
            n = int(self.entry_num.get())
            for i in range(n):
                Label(self.frame_input, text=f"Burst Time for Process {i+1}:", 
                      font=("Times New Roman", 9), bg="white").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                burst_entry = Entry(self.frame_input, width=12)
                burst_entry.grid(row=i, column=1, padx=5, pady=5)
                self.burst_entries.append(burst_entry)
                
                Label(self.frame_input, text=f"Arrival Time for Process {i+1}:", 
                      font=("Times New Roman", 9), bg="white").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                arrival_entry = Entry(self.frame_input, width=12)
                arrival_entry.grid(row=i, column=3, padx=5, pady=5)
                self.arrival_entries.append(arrival_entry)
        except ValueError:
            pass
    
    def calculate_schedule(self):
        if not self.burst_entries:
            return
        try:
            processes = [Process(i + 1, int(self.burst_entries[i].get()), int(self.arrival_entries[i].get()))
                        for i in range(len(self.burst_entries))]
            result, avg_WT, _ = sjf_non_preemptive(processes)
            
            for item in self.tree.get_children():
                self.tree.delete(item)
            for p in result:
                self.tree.insert("", "end", values=(p.pid, p.burst_time, p.arrival_time, p.WT, p.TAT))
            self.label_avg.config(text=f"Average Waiting Time: {avg_WT:.1f}")
        except ValueError:
            pass


if __name__ == "__main__":
    # Create root window and initialize GUI
    root = Tk()
    app = SchedulingGUI(root)
    root.mainloop()
