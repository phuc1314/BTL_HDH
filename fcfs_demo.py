def fcfs(processes, n):
    t = 0
    gantt = []
    complete_set = {}
    tt_wt = 0
    tt_tat = 0
    processes.sort()
    while processes != []:
        if processes[0][0] > t:
            t+=1
            gantt.append("Idle")
            continue
        else:
            st = t
            process = processes.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct = t
            tt = ct - process[0]
            wt = tt - process[1]
            tt_wt += wt
            tt_tat += tt
            complete_set[pid] = [st, ct, tt, wt]
    avg_wt = tt_wt / n
    avg_tat = tt_tat/ n
    print(gantt)
    print(complete_set)
    print(f"Average Turnaround Time:{avg_tat}")
    print(f"Average Waiting Time: {avg_wt}")


if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        arrival = int(input(f"Enter arrival time for process {i + 1}: "))
        pid = i + 1 
        processes.append([arrival, burst,f"p{pid}"])
    fcfs(processes, n)    