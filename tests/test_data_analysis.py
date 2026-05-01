import csv
from pathlib import Path
from polymath_ai.data_analysis import analyze_csv


def test_analyze_csv_numeric(tmp_path):
    p = tmp_path / "data.csv"
    with open(p, 'w', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(["a", "b"])
        writer.writerow(["1", "2"])
        writer.writerow(["3", "4"])
    r = analyze_csv(str(p))
    assert r['rows'] == 2
    assert r['columns'] == 2
    assert 'numeric' in r or 'describe' in r
