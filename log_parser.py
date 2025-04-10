import argparse
import json
import re
from datetime import datetime


LOG_PATTERN = re.compile(r"\[(.*?)\] (\w+): (.*)")

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        timestamp_str, level, message = match.groups()
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return {"timestamp": timestamp, "level": level, "message": message}
    return None


def filter_logs(file_path, level=None, keyword=None, start=None, end=None):
    results = []

    with open(file_path, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if not parsed:
                continue

            if level and parsed["level"] != level:
                continue
            if keyword and keyword.lower() not in parsed["message"].lower():
                continue
            if start and parsed["timestamp"] < start:
                continue
            if end and parsed["timestamp"] > end:
                continue

            results.append({
                "timestamp": parsed["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                "level": parsed["level"],
                "message": parsed["message"]
            })

    return results


def main():
    parser = argparse.ArgumentParser(description="Log Parser")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--level", help="Log level to filter (e.g., ERROR)")
    parser.add_argument("--keyword", help="Keyword to search in message")
    parser.add_argument("--start", help="Start time (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--end", help="End time (YYYY-MM-DD HH:MM:SS)")

    args = parser.parse_args()

    start = datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S") if args.start else None
    end = datetime.strptime(args.end, "%Y-%m-%d %H:%M:%S") if args.end else None

    filtered_logs = filter_logs(args.file, args.level, args.keyword, start, end)
    print(json.dumps(filtered_logs, indent=2))


if __name__ == "__main__":
    main()
