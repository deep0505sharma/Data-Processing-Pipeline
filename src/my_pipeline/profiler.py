import time
import logging

def profile_step(step_name: str, func, *args, **kwargs):
    """
    Measure execution time of a pipeline step.
    Logs duration in seconds.
    Returns the function's output.
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()

    duration = round(end - start, 4)
    logging.info(f"[PROFILE] {step_name} took {duration} seconds")

    return result

