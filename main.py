import argparse
import json
from datetime import date, timedelta

def add_log(text):  

    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    with open("data.json", "w", encoding="utf-8") as f:
        data.append(text)
        json.dump(data, f, indent = 2, ensure_ascii=False)


def list_logs():

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for d in data:
            print(f'{d["date"]}: {d["text"]}')


def streak_logs(current):

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        dates = set()
        streak = 0
        for d in data:
            dates.add(d["date"])
        while current.isoformat() in dates:
            streak += 1
            current -= timedelta(days=1)
        print(streak)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        dest = "command",
        required = True
    )

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")
    list_parser = subparsers.add_parser("list")
    streak_parser = subparsers.add_parser("streak")

    args = parser.parse_args()

    if args.command == "add":
        d = {"text": args.text}
        d["date"] = date.today().isoformat()
        add_log(d)
    elif args.command == "list":
        list_logs()
    elif args.command == "streak":
        streak_logs(date.today())

    #add
    #list
    #streak