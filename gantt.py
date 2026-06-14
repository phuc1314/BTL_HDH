import matplotlib.pyplot as plt

def draw_gantt(result):

    if len(result) == 0:
        return

    result.sort(key=lambda p: p.start_time)

    fig, ax = plt.subplots(figsize=(10, 2))

    y = 0.5
    height = 0.4

    if result[0].start_time > 0:
        idle_time = result[0].start_time
        ax.broken_barh([(0, idle_time)], (y, height), facecolors="lightgray", edgecolor="black")
        ax.text(idle_time / 2, y + height / 2, "IDLE", ha="center", va="center")

    for i in range(len(result)):

        p = result[i]

        ax.broken_barh([(p.start_time, p.burst_time)], (y, height), facecolors="skyblue", edgecolor="black")
        ax.text(p.start_time + p.burst_time / 2, y + height / 2, f"P{p.pid}", ha="center", va="center")

        if i < len(result) - 1:
            next_p = result[i + 1]

            if next_p.start_time > p.complete_time:
                idle_start = p.complete_time
                idle_length = next_p.start_time - p.complete_time

                ax.broken_barh([(idle_start, idle_length)], (y, height), facecolors="lightgray", edgecolor="black")
                ax.text(idle_start + idle_length / 2, y + height / 2, "IDLE", ha="center", va="center")

    times = [0]

    for p in result:
        if p.start_time not in times:
            times.append(p.start_time)

        if p.complete_time not in times:
            times.append(p.complete_time)

    times.sort()

    ax.set_xticks(times)
    ax.set_ylim(0, 2)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("SJF Non-Preemptive Gantt Chart")

    plt.tight_layout()
    plt.show()
