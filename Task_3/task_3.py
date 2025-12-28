import sys

def parse_log_line(line):
    parts = line.strip().split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path):
    logs = []
    try:
        file = open(file_path, "r", encoding="utf-8")
        for line in file:
            logs.append(parse_log_line(line))
        file.close()
    except FileNotFoundError:
        print("Файл не знайдено")
    return logs

def filter_logs_by_level(logs, level):
    level= level.upper()
    result = []
    for log in logs:
        if log["level"] == level:
            result.append(log)
    return result

def count_logs_by_level(logs):
    counts = {}
    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1
    return counts

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in counts:
        print(f"{level:<16} | {counts[level]}")
        
def display_log_details(logs, level):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python log_analyzer.py <logfile> [level]")
        return
    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        display_log_details(filtered, level)



if __name__ == "__main__":
    main()
