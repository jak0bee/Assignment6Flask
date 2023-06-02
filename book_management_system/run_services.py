import subprocess

services = [
    'api_gateway/book_gateway.py',
    'catalog_service/book_catalog.py',
    'inventory_service/book_inventory.py',
    'order_service/book_order.py'
]

processes = []
for service in services:
    processes.append(subprocess.Popen(['python3', service]))

print("All services started. Press Ctrl+C to terminate.")

try:
    for process in processes:
        process.wait()
except KeyboardInterrupt:
    print("Terminating services...")
    for process in processes:
        process.terminate()
