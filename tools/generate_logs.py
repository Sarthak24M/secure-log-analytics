import argparse
import random
import re
from pathlib import Path
from datetime import datetime, timedelta


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Generate synthetic Ubuntu authentication logs."
    )

    parser.add_argument(
        "--lines",
        type=int,
        required=True,
        help="Number of log entries to generate."
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility."
    )

    return parser.parse_args()


def load_logs():

    log_file = Path("data/raw/auth.log")

    if not log_file.exists():
        raise FileNotFoundError(f"Could not find {log_file}")

    with open(log_file, "r", encoding="utf-8") as file:
        return file.readlines()


def generate_timestamp(start_time, index):

    seconds = random.randint(1, 5)

    return start_time + timedelta(seconds=index * seconds)


def randomize_pid(line):

    return re.sub(
        r"\[(\d+)\]",
        lambda _: f"[{random.randint(1000, 99999)}]",
        line
    )


def replace_timestamp(line, new_timestamp):

    pattern = (
        r"^\d{4}-\d{2}-\d{2}"
        r"T\d{2}:\d{2}:\d{2}"
        r"(?:\.\d+)?"
        r"(?:Z|[+-]\d{2}:\d{2})?"
    )

    return re.sub(
        pattern,
        new_timestamp.isoformat(timespec="microseconds"),
        line,
        count=1
    )


def generate_logs(original_logs, total_lines):

    generated_logs = []

    start_time = datetime.now()

    for i in range(total_lines):

        line = random.choice(original_logs)

        line = randomize_pid(line)

        timestamp = generate_timestamp(start_time, i)

        line = replace_timestamp(line, timestamp)

        generated_logs.append(line)

    return generated_logs


def output_filename(lines):

    if lines >= 1000000:
        return f"auth_{lines // 1000000}m.log"

    if lines >= 1000:
        return f"auth_{lines // 1000}k.log"

    return f"auth_{lines}.log"


def save_logs(logs, filename):

    output_directory = Path("data/raw")

    output_directory.mkdir(parents=True, exist_ok=True)

    output_file = output_directory / filename

    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(logs)

    return output_file


def main():

    args = parse_arguments()

    if args.seed is not None:
        random.seed(args.seed)

    original_logs = load_logs()

    print(f"Loaded {len(original_logs)} original log entries.")

    synthetic_logs = generate_logs(
        original_logs,
        args.lines
    )

    filename = output_filename(args.lines)

    output_path = save_logs(
        synthetic_logs,
        filename
    )

    print(f"\nGenerated {len(synthetic_logs)} synthetic log entries.")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()