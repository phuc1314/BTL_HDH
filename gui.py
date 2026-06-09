from tkinter import *
from scheduler import *

root = Tk()
root.geometry("900x650")

frame_title = Frame(root)
frame_title.pack(pady=10)
Label(frame_title, text="Process Scheduling",font=("Times New Roman",20,"bold")).pack()

frame_data = Frame(root)
frame_data.pack(pady=10)
label_num = Label(frame_data, text="Number of Processes:", font=("Times New Roman",10))
label_num.grid(row=0,column=0,padx=5)
entry_num = Entry(frame_data,width=30)
entry_num.grid(row=0,column=1,padx=5)

burst_entries = []
arrival_entries = []
frame_input = Frame(root)
frame_input.pack(pady=20)
def create_entries():
    n = int(entry_num.get())
    for i in range(n):
        label_brust = Label(frame_input,text=f"Burst Time for Process {i+1}:",font=("Times New Roman",10))
        label_brust.grid(row=i, column=0, padx=20, pady=5)
        burst_entry = Entry(frame_input)
        burst_entry.grid(row=i, column=1, padx=20)
        burst_entries.append(burst_entry)

        label_arrival = Label(frame_input,text=f"Arrival Time for Process {i+1}:",font=("Times New Roman",10))
        label_arrival.grid(row=i, column=2, padx=20, pady=5)
        arrival_entry = Entry(frame_input)
        arrival_entry.grid(row=i, column=3, padx=20)
        arrival_entries.append(arrival_entry)
button_input = Button(frame_data,text="Create Entries", command = create_entries)
button_input.grid(row=0,column=2,padx=20)

def calculate_schedule():
    processes = []
    for i in range(len(burst_entries)):
        burst = int(burst_entries[i].get())
        arrival = int(arrival_entries[i].get())
        process = Process(i + 1,burst,arrival)
        processes.append(process)

    result, avg_WT, avg_TAT = sjf_non_preemptive(processes)
    frame_result = Frame(root)
    frame_result.pack(pady = 20)
button_output = Button(frame_data, text = "Calculate Shedule", command = calculate_schedule)
button_output.grid(row = 0, column = 3, padx = 20)
root.mainloop()