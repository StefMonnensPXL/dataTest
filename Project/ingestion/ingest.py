import os
import pandas as pd
from datetime import datetime
import json

DATA_DIR = "../data"
META_DIR = "../metadata"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)

# Voorbeeld: nieuwe data genereren (of van een externe bron halen)
new_data = pd.DataFrame({
    "id": [1, 2, 3],
    "value": [10, 20, 30]
})

# Timestamp voor versieing
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
data_file = f"{DATA_DIR}/data_{timestamp}.csv"
new_data.to_csv(data_file, index=False)

# Metadata voor data lineage
metadata = {
    "file": os.path.basename(data_file),
    "timestamp": timestamp,
    "num_rows": len(new_data),
    "columns": list(new_data.columns)
}

with open(f"{META_DIR}/metadata_{timestamp}.json", "w") as f:
    json.dump(metadata, f, indent=2)

print(f"Ingested data saved to {data_file}")
print(f"Metadata saved to {META_DIR}/metadata_{timestamp}.json")
