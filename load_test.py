import concurrent.futures
import time
from client.rpc_client import RPCClient

HOST = "18.213.151.219"  # IP de tu worker2
PORT = 30007

def single_call(i):
    try:
        rpc = RPCClient(HOST, PORT, timeout=10.0)
        result = rpc.call("slow_task", 1) # Simula una tarea que tarda 1 seg
        return f"Petición {i}: OK"
    except Exception as e:
        return f"Petición {i}: Fallo - {e}"

if __name__ == "__main__":
    start_time = time.time()
    
    # Lanzamos 10 peticiones concurrentes
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(single_call, range(10)))
        
    for res in results:
        print(res)
        
    end_time = time.time()
    print(f"\nTiempo total para 10 peticiones concurrentes: {end_time - start_time:.2f} segundos")