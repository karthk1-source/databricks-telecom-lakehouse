import csv
import random
import uuid
from datetime import datetime, timedelta
from pathlib import Path

output_dir = Path("raw_data/telecom_events")
output_dir.mkdir(parents=True, exist_ok=True)

regions = ["Dallas", "Austin", "Houston", "Chicago", "New York", "Atlanta"]
network_types = ["4G", "5G", "LTE"]
device_types = ["iPhone", "Samsung", "Pixel", "Motorola"]
event_types = ["CALL", "DATA", "SMS"]

def generate_record():
    event_time = datetime.now() - timedelta(minutes=random.randint(0, 10080))

    return {
        "event_id": str(uuid.uuid4()),
        "customer_id": random.randint(100000, 999999),
        "cell_tower_id": f"TOWER_{random.randint(1, 500)}",
        "region": random.choice(regions),
        "network_type": random.choice(network_types),
        "device_type": random.choice(device_types),
        "event_type": random.choice(event_types),
        "event_timestamp": event_time.strftime("%Y-%m-%d %H:%M:%S"),
        "signal_strength": random.randint(-130, -40),
        "latency_ms": random.randint(10, 500),
        "dropped_call": random.choice([0, 0, 0, 1]),
        "data_usage_mb": round(random.uniform(0.1, 500.0), 2)
    }

for batch_id in range(1, 6):
    file_path = output_dir / f"telecom_events_batch_{batch_id}.csv"

    with open(file_path, "w", newline="") as csvfile:
        fieldnames = list(generate_record().keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(10000):
            writer.writerow(generate_record())

    print(f"Generated: {file_path}")