"""
CPU Dispatch Algorithms Package.

This package contains implementations of various CPU scheduling and dispatch
algorithms commonly used in operating systems for process scheduling.

Algorithms included:
- FIFO (First In First Out): Processes are executed in arrival order
- SJF (Shortest Job First): Processes are ordered by burst time
- Priority: Processes are scheduled based on priority levels
- Round Robin: Processes are executed in round-robin with time quantum
"""

from .fifo_disp import FIFODispatcher
from .sjf_disp import SJFDispatcher
from .priority_disp import PriorityDispatcher
from .round_robin_fifo_disp import RoundRobinDispatcher

__all__ = [
    "FIFODispatcher",
    "SJFDispatcher",
    "PriorityDispatcher",
    "RoundRobinDispatcher"
]
