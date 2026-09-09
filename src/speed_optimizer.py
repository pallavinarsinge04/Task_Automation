import time
import functools
import concurrent.futures
import os

def measure_execution_time(func):
    """
    Decorator to measure and log the execution time of any function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"[Performance] Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result, execution_time
    return wrapper

def process_file_batch_parallel(file_paths, processing_function):
    """
    Optimizes performance by processing multiple files concurrently using Multi-threading.
    Reduces total execution time compared to standard sequential loops.
    """
    start_time = time.perf_counter()
    results = []
    
    # Use ThreadPoolExecutor for concurrent I/O file operations
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(processing_function, file_path) for file_path in file_paths if os.path.exists(file_path)]
        for future in concurrent.futures.as_completed(futures):
            try:
                res = future.result()
                results.append(res)
            except Exception as e:
                print(f"[Error] Parallel task failed: {e}")
                
    total_time = time.perf_counter() - start_time
    print(f"[Batch Optimization] Processed {len(results)} items in {total_time:.4f} seconds using multi-threading.")
    return results, total_time