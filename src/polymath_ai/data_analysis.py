from typing import Dict, Any

import csv

try:
    import pandas as pd
except Exception:
    pd = None


def analyze_csv(path: str) -> Dict[str, Any]:
    """Return simple analysis of a CSV. If pandas available, uses it; otherwise falls back to csv and basic stats."""
    if pd is not None:
        df = pd.read_csv(path)
        out = {
            'rows': int(df.shape[0]),
            'columns': int(df.shape[1]),
            'describe': df.describe(include='all').to_dict()
        }
        return out

    # fallback
    with open(path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
    if not rows:
        return {'rows': 0, 'columns': 0}
    cols = rows[0].keys()
    numeric_stats = {}
    for c in cols:
        vals = []
        for r in rows:
            try:
                v = float(r[c])
                vals.append(v)
            except Exception:
                continue
        if vals:
            numeric_stats[c] = {
                'count': len(vals),
                'mean': sum(vals)/len(vals),
                'min': min(vals),
                'max': max(vals)
            }
    return {'rows': len(rows), 'columns': len(list(cols)), 'numeric': numeric_stats}
