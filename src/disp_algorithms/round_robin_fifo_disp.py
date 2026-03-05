"""
Round Robin FIFO Dispatch Algorithm.

This module implements a Round Robin scheduling algorithm with a time quantum
where each process gets a fixed time slice to execute.
"""

from collections import deque
from typing import List, Dict


class RoundRobinDispatcher:
    """Round Robin dispatcher implementation with FIFO queue."""
    
    def __init__(self, time_quantum: int = 4):
        """
        Initialize the Round Robin dispatcher.
        
        Args:
            time_quantum: Time slice allocated to each process per turn (default: 4)
        """
        self.queue = deque()
        self.time_quantum = time_quantum
        self.execution_log = []
    
    def add_process(self, process_id: str, burst_time: int) -> None:
        """
        Add a process to the Round Robin queue.
        
        Args:
            process_id: Unique identifier for the process
            burst_time: Total CPU burst time required by the process
        """
        self.queue.append({"id": process_id, "burst_time": burst_time})
    
    def execute(self) -> Dict:
        """
        Execute all processes using Round Robin scheduling.
        
        Returns:
            Dictionary containing execution results with metrics like total time,
            average waiting time, and execution log.
        """
        current_time = 0
        process_times = {}  # Track waiting time for each process
        temp_queue = deque(self.queue)
        
        while temp_queue:
            process = temp_queue.popleft()
            process_id = process["id"]
            burst_time = process["burst_time"]
            
            # Initialize wait time if not present
            if process_id not in process_times:
                process_times[process_id] = {"wait_time": 0, "original_burst": burst_time}
            
            # Calculate execution time for this turn
            execution_time = min(burst_time, self.time_quantum)
            start_time = current_time
            current_time += execution_time
            
            self.execution_log.append({
                "process_id": process_id,
                "start_time": start_time,
                "end_time": current_time,
                "execution_time": execution_time,
                "remaining_time": max(0, burst_time - execution_time)
            })
            
            # If process still has remaining time, add it back to queue
            remaining_time = burst_time - execution_time
            if remaining_time > 0:
                temp_queue.append({"id": process_id, "burst_time": remaining_time})
                process_times[process_id]["wait_time"] += execution_time
            else:
                process_times[process_id]["wait_time"] += execution_time
        
        # Calculate average waiting time
        total_waiting_time = sum(p["wait_time"] for p in process_times.values())
        process_count = len(process_times)
        avg_waiting_time = total_waiting_time / process_count if process_count > 0 else 0
        
        return {
            "algorithm": "Round Robin (FIFO)",
            "time_quantum": self.time_quantum,
            "total_time": current_time,
            "average_waiting_time": avg_waiting_time,
            "execution_log": self.execution_log
        }
    
    def reset(self) -> None:
        """Reset the dispatcher for a new scheduling cycle."""
        self.queue.clear()
        self.execution_log.clear()
