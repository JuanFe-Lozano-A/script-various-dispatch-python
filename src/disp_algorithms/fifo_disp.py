"""
FIFO (First In First Out) Dispatch Algorithm.

This module implements a simple FIFO scheduling algorithm where processes
are executed in the order they arrive in the queue.
"""

from collections import deque
from typing import List, Dict, Tuple


class FIFODispatcher:
    """First In First Out dispatcher implementation."""
    
    def __init__(self):
        """Initialize the FIFO dispatcher with an empty queue."""
        self.queue = deque()
        self.execution_log = []
    
    def add_process(self, process_id: str, burst_time: int) -> None:
        """
        Add a process to the FIFO queue.
        
        Args:
            process_id: Unique identifier for the process
            burst_time: CPU burst time required by the process
        """
        self.queue.append({"id": process_id, "burst_time": burst_time})
    
    def execute(self) -> Dict:
        """
        Execute all processes in FIFO order.
        
        Returns:
            Dictionary containing execution results with metrics like total time,
            average waiting time, and execution log.
        """
        current_time = 0
        total_waiting_time = 0
        process_count = len(self.queue)
        
        while self.queue:
            process = self.queue.popleft()
            start_time = current_time
            end_time = current_time + process["burst_time"]
            waiting_time = start_time
            total_waiting_time += waiting_time
            
            self.execution_log.append({
                "process_id": process["id"],
                "start_time": start_time,
                "end_time": end_time,
                "burst_time": process["burst_time"],
                "waiting_time": waiting_time
            })
            
            current_time = end_time
        
        avg_waiting_time = total_waiting_time / process_count if process_count > 0 else 0
        
        return {
            "algorithm": "FIFO",
            "total_time": current_time,
            "average_waiting_time": avg_waiting_time,
            "execution_log": self.execution_log
        }
    
    def reset(self) -> None:
        """Reset the dispatcher for a new scheduling cycle."""
        self.queue.clear()
        self.execution_log.clear()
