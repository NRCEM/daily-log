import argparse
import json
from datetime import date, timedelta

def load_data():

    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2, ensure_ascii=False)


def add_log(entry):  
    if entry["text"].strip():
        data = load_data()
        data.append(entry)
        save_data(data)
        print(f'Successfully added: {entry["text"]} on {entry["date"]}')
    else:
        print("Error: log cannot be empty.")

def list_logs():

    data = load_data() 
    print("Logs:")
    for d in data:
        print(f'{d["date"]}: {d["text"]}')


def streak_logs(current):

    data = load_data()
    dates = set()
    streak = 0
    for d in data:
        dates.add(d["date"])
    while current.isoformat() in dates:
        streak += 1
        current -= timedelta(days=1)
    if streak == 1:
        print("Current streak: 1 day")
    else: print(f'Current streak: {streak} days')


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