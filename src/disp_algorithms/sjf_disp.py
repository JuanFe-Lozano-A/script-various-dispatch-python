"""
SJF (Shortest Job First) Dispatch Algorithm.

This module implements the Shortest Job First scheduling algorithm where
the process with the shortest burst time is executed first.
"""

from typing import List, Dict


class SJFDispatcher:
    """Shortest Job First dispatcher implementation."""
    
    def __init__(self):
        """Initialize the SJF dispatcher with an empty process list."""
        self.processes = []
        self.execution_log = []
    
    def add_process(self, process_id: str, burst_time: int) -> None:
        """
        Add a process to the SJF queue.
        
        Args:
            process_id: Unique identifier for the process
            burst_time: CPU burst time required by the process
        """
        self.processes.append({"id": process_id, "burst_time": burst_time})
    
    def execute(self) -> Dict:
        """
        Execute all processes in shortest job first order.
        
        Returns:
            Dictionary containing execution results with metrics like total time,
            average waiting time, and execution log.
        """
        # Sort processes by burst time (shortest first)
        sorted_processes = sorted(self.processes, key=lambda x: x["burst_time"])
        
        current_time = 0
        total_waiting_time = 0
        process_count = len(sorted_processes)
        
        for process in sorted_processes:
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
            "algorithm": "SJF",
            "total_time": current_time,
            "average_waiting_time": avg_waiting_time,
            "execution_log": self.execution_log
        }
    
    def reset(self) -> None:
        """Reset the dispatcher for a new scheduling cycle."""
        self.processes.clear()
        self.execution_log.clear()
