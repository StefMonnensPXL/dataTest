import pandas as pd
import os
from datetime import datetime

def main():
    # Create directories within Project folder
    data_dir = 'data'
    metadata_dir = 'metadata'
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(metadata_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Sample data - replace with your actual data ingestion
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'value': [100, 200, 300]
    })
    
    # Save files in Project/data and Project/metadata
    data_file = os.path.join(data_dir, f'data_{timestamp}.csv')
    metadata_file = os.path.join(metadata_dir, f'metadata_{timestamp}.json')
    
    df.to_csv(data_file, index=False)
    
    # Create and save metadata
    metadata = {
        'timestamp': timestamp,
        'records': len(df),
        'columns': list(df.columns),
        'data_file': data_file
    }
    
    import json
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Ingested data saved to {data_file}")
    print(f"Metadata saved to {metadata_file}")

if __name__ == "__main__":
    main()