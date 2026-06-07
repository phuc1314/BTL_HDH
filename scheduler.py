class Process:
        def __init__(self, process_id, burst_time, arrival_time):
            self.process_id = process_id
            self.burst_time = burst_time
            self.arrival_time = arrival_time
            self.waiting_time = 0
            self.turnaround_time = 0

def sjf_non_preemptive(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    n = len(processes)
    completed = []
    result = []
    current_time = 0
    while len(completed) < n:
        ready_queue = []
        for process in processes:
            if process not in completed and process.arrival_time <= current_time:
                ready_queue.append(process)
        # CPU Idle
        if len(ready_queue) == 0:
            current_time += 1
            continue
        # Chọn process có burst time nhỏ nhất
        selected = min(
            ready_queue,
            key=lambda x: x.burst_time
        )
        # Waiting Time = Start Time - Arrival Time
        selected.waiting_time = current_time - selected.arrival_time
        # Chạy process đến hết
        current_time += selected.burst_time
        # Turnaround Time = Waiting Time + Burst Time
        selected.turnaround_time = selected.waiting_time + selected.burst_time
        total_waiting_time += selected.waiting_time
        total_turnaround_time += selected.turnaround_time
        completed.append(selected)
        result.append(selected)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    return (
        result,
        avg_waiting_time,
        avg_turnaround_time,
    )

