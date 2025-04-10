# practical_python
python log_parser.py --file logs.txt --start "2025-04-10 12:45:00" --end "2025-04-10 12:50:00"

python log_parser.py --file logs.txt --level ERROR --keyword Redis --start "2021-05-05 10:12:12"

Output:
[
  {
    "timestamp": "2025-04-10 12:47:01",
    "level": "ERROR",
    "message": "Timeout while connecting to Redis"
  }
]