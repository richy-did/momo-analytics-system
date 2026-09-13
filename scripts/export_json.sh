#!/usr/bin/env bash
python - <<'PY'
from etl.run import load_transactions, export_dashboard
records = load_transactions('data/raw/momo.xml')
export_dashboard(records)
print(f'Exported {len(records)} records')
PY
