import sys
import time

class StepProgress:
    def __init__(self, total: int):
        self.total = total
        self.current = 0
        self.start_time = time.time()

    def update(self, step_name: str):
        """Advance progress by 1 and print the step name."""
        self.current += 1
        percent = (self.current / self.total) * 100

        elapsed = time.time() - self.start_time
        elapsed_str = f"{elapsed:.1f}s"

        bar_len = 30
        filled = int(self.current / self.total * bar_len)
        bar = "█" * filled + "-" * (bar_len - filled)

        msg = (
            f"\r▶️  Step {self.current}/{self.total} "
            f"[{bar}] {percent:5.1f}% | {step_name} | elapsed {elapsed_str}"
        )

        sys.stdout.write(msg)
        sys.stdout.flush()

        if self.current == self.total:
            print()  # final newline

    def finish(self):
        """Optional: print summary."""
        total_time = time.time() - self.start_time
        print(f"Completed all {self.total} steps in {total_time:.2f}s")
