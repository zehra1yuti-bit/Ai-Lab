"""Lab 2 - Python essentials for AI: functions, lists, dicts, classes, files, exceptions."""
import csv
from pathlib import Path

def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Cannot compute the mean of an empty list")
    return sum(values) / len(values)

def median(values: list[float]) -> float:
    """Calculates the median for both odd and even lists of numbers."""
    if not values:
        raise ValueError("Cannot compute the median of an empty list")
    
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_vals[mid]
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0

def normalize(values: list[float]) -> list[float]:
    """Min-max scaling to the range 0..1."""
    low, high = min(values), max(values)
    if low == high:
        return [0.0 for _ in values]
    return [(v - low) / (high - low) for v in values]

class Dataset:
    """Loads a CSV file into a list of dictionaries."""

    def __init__(self, path: str):
        self.path = Path(path)
        self.rows: list[dict] = []

    def load(self) -> None:
        try:
            with self.path.open(encoding="utf-8") as f:
                self.rows = list(csv.DictReader(f))
        except FileNotFoundError:
            print(f"File not found: {self.path}")

    def column(self, name: str) -> list[float]:
        values = []
        for row in self.rows:
            try:
                values.append(float(row[name]))
            except (ValueError, KeyError):
                pass  # Skip missing or invalid values
        return values

    def summary(self, name: str) -> dict:
        """Returns a dictionary with min, max, and mean of a column."""
        col_data = self.column(name)
        if not col_data:
            return {"min": None, "max": None, "mean": None}
        return {
            "min": min(col_data),
            "max": max(col_data),
            "mean": mean(col_data)
        }


if __name__ == "__main__":
    scores = [55, 70, 90, 62, 81]
    print("Mean:", mean(scores))
    print("Median (Odd list):", median(scores))
    print("Median (Even list):", median([55, 70, 81, 90]))
    print("Normalized:", [round(x, 2) for x in normalize(scores)])

    # Exercise 2.1: Scores above average & Pass/Fail mapping (threshold 60)
    avg_score = mean(scores)
    above_avg = [s for s in scores if s > avg_score]
    pass_fail = {s: ("pass" if s >= 60 else "fail") for s in scores}
    print("Scores above average:", above_avg)
    print("Pass/Fail dictionary:", pass_fail)

    # Loading dataset and testing summary method
    data = Dataset("data/students.csv")
    data.load()
    
    hours = data.column("study_hours")
    print(f"\nLoaded {len(data.rows)} rows; mean study hours = {mean(hours):.2f}")
    
    # Print summaries for attendance and final score
    print("Study Hours Summary:", data.summary("study_hours"))
    print("Final Score Summary:", data.summary("final_score"))

    # Writing output summary file
    Path("output").mkdir(exist_ok=True)
    Path("output/summary.txt").write_text(f"rows={len(data.rows)}\n", encoding="utf-8")
    print("Wrote output/summary.txt")