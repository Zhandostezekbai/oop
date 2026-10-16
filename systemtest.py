import time

class Process:
    def __init__(self, pid: int, name: str, execution_time: int):
        self._pid = pid
        self._name = name
        self._execution_time = execution_time
        self._state = "READY"  # Default initial state: READY, RUNNING, or TERMINATED

    # --- PID PROPERTY (Read-only) ---
    @property
    def pid(self) -> int:
        return self._pid

    # --- NAME PROPERTY ---
    @property
    def name(self) -> str:
        return self._name

    # --- EXECUTION TIME PROPERTY ---
    @property
    def execution_time(self) -> int:
        return self._execution_time

    @execution_time.setter
    def execution_time(self, value: int):
        if value <= 0:
            raise ValueError("Execution time must be greater than 0 seconds.")
        self._execution_time = value

    # --- STATE PROPERTY ---
    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str):
        valid_states = ["READY", "RUNNING", "TERMINATED"]
        if value.upper() not in valid_states:
            raise ValueError(f"Invalid OS state. Choose from: {valid_states}")
        self._state = value.upper()

    def get_info(self) -> str:
        """Returns standard process diagnostic data."""
        return f"[PID: {self.pid}] Name: {self.name} | State: {self.state}"


class SystemProcess(Process):
    def __init__(self, pid: int, name: str, execution_time: int, privilege_level: int):
        # super().__init__() passes common properties to the core Process class
        super().__init__(pid, name, execution_time)
        self._privilege_level = privilege_level  # Higher values mean higher kernel priority

    @property
    def privilege_level(self) -> int:
        return self._privilege_level

    # Overriding get_info to show kernel details
    def get_info(self) -> str:
        return f"[System Kernel] {super().get_info()} | Privilege: Level {self.privilege_level}"


class UserProcess(Process):
    def __init__(self, pid: int, name: str, execution_time: int, launched_by_user: str):
        # super().__init__() passes common properties to the core Process class
        super().__init__(pid, name, execution_time)
        self._launched_by_user = launched_by_user

    @property
    def launched_by_user(self) -> str:
        return self._launched_by_user

    # Overriding get_info to show user space details
    def get_info(self) -> str:
        return f"[User Space] {super().get_info()} | User: {self.launched_by_user}"


class CPUScheduler:
    """Simulates a very basic Operating System CPU Scheduler."""
    def __init__(self):
        self.queue = []

    def load_process(self, process: Process):
        self.queue.append(process)
        print(f"OS: Loaded process into RAM -> {process.name}")

    def run_all(self):
        print("\n=== OS CPU SCHEDULER STARTING EXECUTION ===")
        for proc in self.queue:
            print(proc.get_info())
            
            # Context switch state to RUNNING
            proc.state = "RUNNING"
            print(f"-> CPU allocating cycles to {proc.name} for {proc.execution_time}s...")
            time.sleep(0.5) # Simulating execution delay
            
            # Finish execution
            proc.state = "TERMINATED"
            print(f"-> Process {proc.name} finished smoothly.\n")
        print("=== ALL PROCESSES TERMINATED ===")


# ==========================================
# EXECUTION / TESTING
# ==========================================
if __name__ == "__main__":
    # 1. Initialize OS processes
    kernel_core = SystemProcess(pid=101, name="vmlinuz_core", execution_time=4, privilege_level=5)
    browser_app = UserProcess(pid=4002, name="chrome.exe", execution_time=2, launched_by_user="tanasheva")

    # 2. Boot up the CPU Scheduler simulation
    os_scheduler = CPUScheduler()
    os_scheduler.load_process(kernel_core)
    os_scheduler.load_process(browser_app)

    # 3. Simulate execution cycle
    os_scheduler.run_all()
