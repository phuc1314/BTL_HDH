from tkinter import *
from tkinter import ttk
from scheduler import *

root = Tk()
root.title("Process Scheduling")
root.geometry("900x700")
root.config(bg="white")

# Title
frame_title = Frame(root, bg="white")
frame_title.pack(pady=15)
Label(frame_title, text="Process Scheduling", font=("Times New Roman", 20, "bold"), bg="white").pack()

# Input Section
frame_data = Frame(root, bg="white")
frame_data.pack(pady=10, padx=20, fill="x")

# Number of Processes and Create Entries Button
label_num = Label(frame_data, text="Number of Processes:", font=("Times New Roman", 10), bg="white")
label_num.grid(row=0, column=0, padx=5, sticky="w")
entry_num = Entry(frame_data, width=15, font=("Times New Roman", 10))
entry_num.grid(row=0, column=1, padx=5, sticky="w")

button_input = Button(frame_data, text="Create Entries", command=lambda: create_entries(), 
                      font=("Times New Roman", 9), bg="lightblue", padx=15)
button_input.grid(row=0, column=2, padx=20, sticky="w")

# Process Input Frame
burst_entries = []
arrival_entries = []
frame_input = Frame(root, bg="white")
frame_input.pack(pady=10, padx=20, fill="both", expand=True)

def create_entries():
    # Clear previous entries
    for widget in frame_input.winfo_children():
        widget.destroy()
    burst_entries.clear()
    arrival_entries.clear()
    
    try:
        n = int(entry_num.get())
        # Create entries for each process - arrange burst and arrival time side by side
        for i in range(n):
            # Burst Time
            label_burst = Label(frame_input, text=f"Burst Time for Process {i+1}:", 
                              font=("Times New Roman", 9), bg="white")
            label_burst.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            burst_entry = Entry(frame_input, width=12, font=("Times New Roman", 9))
            burst_entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            burst_entries.append(burst_entry)
            
            # Arrival Time
            label_arrival = Label(frame_input, text=f"Arrival Time for Process {i+1}:", 
                                font=("Times New Roman", 9), bg="white")
            label_arrival.grid(row=i, column=2, padx=10, pady=5, sticky="w")
            arrival_entry = Entry(frame_input, width=12, font=("Times New Roman", 9))
            arrival_entry.grid(row=i, column=3, padx=5, pady=5, sticky="w")
            arrival_entries.append(arrival_entry)
    except ValueError:
        pass

# Result Display Frame
frame_result = Frame(root, bg="white")
frame_result.pack(pady=10, padx=20, fill="both", expand=True)

# Table to display results
columns = ("Process ID", "Burst Time", "Arrival Time", "Waiting Time", "Turnaround Time")
tree = ttk.Treeview(frame_result, columns=columns, height=8, show="headings")
tree.pack(fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor="center")

# Average Waiting Time Label
label_avg = Label(frame_result, text="Average Waiting Time: -", 
                 font=("Times New Roman", 10, "bold"), bg="white")
label_avg.pack(pady=5)

def calculate_schedule():
    if not burst_entries or not arrival_entries:
        return
    
    try:
        processes = []
        for i in range(len(burst_entries)):
            burst = int(burst_entries[i].get())
            arrival = int(arrival_entries[i].get())
            process = Process(i + 1, burst, arrival)
            processes.append(process)
        
        result, avg_WT, avg_TAT = sjf_non_preemptive(processes)
        
        # Clear previous results
        for item in tree.get_children():
            tree.delete(item)
        
        # Display results in table
        for process in result:
            tree.insert("", "end", values=(
                process.pid,
                process.burst_time,
                process.arrival_time,
                process.WT,
                process.TAT
            ))
        
        # Update average waiting time
        label_avg.config(text=f"Average Waiting Time: {avg_WT:.1f}")
    except ValueError:
        pass

# Calculate Schedule Button
button_output = Button(root, text="Calculate Schedule", command=calculate_schedule,
                      font=("Times New Roman", 10), bg="lightgreen", padx=20, pady=5)
button_output.pack(pady=10)

root.mainloop()