class Process:
        def __init__(self, process_id, burst_time, arrival_time):
            self.pid = process_id
            self.burst_time = burst_time
            self.arrival_time = arrival_time

            self.start_time = 0
            self.complete_time = 0
            self.WT = 0 # Waiting Time
            self.TAT = 0 #Turnaround Time

def sjf_non_preemptive(processes):
    total_WT = 0
    total_TAT = 0
    busy_time = 0
    n = len(processes)
    completed = set()
    result = []
    current_time = 0
    while len(completed) < n:
        ready = []
        for process in processes:
            if process not in completed and process.arrival_time <= current_time:
                ready.append(process)
        if len(ready) == 0:
            current_time += 1
            continue
        # Select the process with the shortest burst time
        selected = min(ready,key=lambda x: (x.burst_time, x.arrival_time, x.pid))
        selected.start_time = current_time
        # Run the process until completion
        current_time += selected.burst_time
        selected.complete_time = current_time
        # Turnaround Time = Complete Time - Arrival Time
        selected.TAT = selected.complete_time - selected.arrival_time
        # Waiting Time = TAT - Burst Time
        selected.WT = selected.TAT - selected.burst_time
        total_WT += selected.WT
        total_TAT += selected.TAT
        busy_time += selected.burst_time
        completed.add(selected)
        result.append(selected)
    avg_WT = total_WT / n
    avg_TAT = total_TAT / n
    #CPU Utilization = (Total Burst Time / Total System Time) × 100%
    cpu_u = (busy_time/selected.complete_time) * 100
    #Throughput = Number of Processes / Total Time
    throughput = n / selected.complete_time
    return (
        result,
        avg_WT,
        avg_TAT,
        cpu_u,
        throughput
    )