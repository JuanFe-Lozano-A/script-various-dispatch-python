"""
CPU Dispatch Algorithm Tester - Main Module.

This module provides a command-line interface to test various CPU scheduling
and dispatch algorithms including FIFO, SJF, Priority, and Round Robin.
"""

import sys
from typing import List, Dict
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from disp_algorithms.fifo_disp import FIFODispatcher
from disp_algorithms.sjf_disp import SJFDispatcher
from disp_algorithms.priority_disp import PriorityDispatcher
from disp_algorithms.round_robin_fifo_disp import RoundRobinDispatcher


class DispatcherTester:
    """Main application class for testing dispatch algorithms."""
    
    def __init__(self):
        """Initialize the tester with all available dispatchers."""
        # Initialize all dispatcher instances
        self.fifo = FIFODispatcher()
        self.sjf = SJFDispatcher()
        self.priority = PriorityDispatcher()
        self.round_robin = RoundRobinDispatcher(time_quantum=4)
        
        # Store test data for easy reuse
        self.test_data = []
    
    def print_menu(self) -> None:
        """Display the main menu options."""
        print("\n" + "="*60)
        print("         CPU DISPATCH ALGORITHM TESTER")
        print("="*60)
        print("1. Test FIFO Dispatcher")
        print("2. Test SJF (Shortest Job First) Dispatcher")
        print("3. Test Priority Dispatcher")
        print("4. Test Round Robin Dispatcher")
        print("5. Compare All Algorithms")
        print("6. Test with Custom Input")
        print("0. Exit")
        print("="*60)
    
    def add_test_process(self, process_id: str, burst_time: int, priority: int = 1) -> None:
        """
        Add a process to the test data.
        
        Args:
            process_id: Unique process identifier
            burst_time: CPU burst time for the process
            priority: Priority level (optional, default=1)
        """
        self.test_data.append({
            "id": process_id,
            "burst_time": burst_time,
            "priority": priority
        })
    
    def load_sample_data(self) -> None:
        """Load sample test data with predefined processes."""
        self.test_data = [
            {"id": "P1", "burst_time": 8, "priority": 2},
            {"id": "P2", "burst_time": 4, "priority": 1},
            {"id": "P3", "burst_time": 2, "priority": 3},
            {"id": "P4", "burst_time": 6, "priority": 2},
        ]
    
    def display_results(self, results: Dict) -> None:
        """
        Display formatted execution results.
        
        Args:
            results: Dictionary containing execution results from a dispatcher
        """
        print(f"\n{'Algorithm:':.<30} {results['algorithm']}")
        if 'time_quantum' in results:
            print(f"{'Time Quantum:':.<30} {results['time_quantum']}")
        print(f"{'Total Execution Time:':.<30} {results['total_time']} units")
        print(f"{'Average Waiting Time:':.<30} {results['average_waiting_time']:.2f} units")
        
        # Display execution log in a formatted table
        print("\nExecution Log:")
        print("-" * 80)
        if results['algorithm'] == 'Priority':
            print(f"{'Process':<10} {'Start':<8} {'End':<8} {'Burst':<8} {'Priority':<10} {'Wait':<8}")
            for log in results['execution_log']:
                print(f"{log['process_id']:<10} {log['start_time']:<8} {log['end_time']:<8} "
                      f"{log['burst_time']:<8} {log['priority']:<10} {log['waiting_time']:<8}")
        elif results['algorithm'] == 'Round Robin (FIFO)':
            print(f"{'Process':<10} {'Start':<8} {'End':<8} {'Exec Time':<12} {'Remaining':<10}")
            for log in results['execution_log']:
                print(f"{log['process_id']:<10} {log['start_time']:<8} {log['end_time']:<8} "
                      f"{log['execution_time']:<12} {log['remaining_time']:<10}")
        else:
            print(f"{'Process':<10} {'Start':<8} {'End':<8} {'Burst':<8} {'Wait':<8}")
            for log in results['execution_log']:
                print(f"{log['process_id']:<10} {log['start_time']:<8} {log['end_time']:<8} "
                      f"{log['burst_time']:<8} {log['waiting_time']:<8}")
        print("-" * 80)
    
    def test_fifo(self) -> None:
        """Test the FIFO dispatcher with sample data."""
        print("\n>>> Testing FIFO Dispatcher")
        self.load_sample_data()
        self.fifo.reset()
        
        # Add all test processes to FIFO
        for process in self.test_data:
            self.fifo.add_process(process["id"], process["burst_time"])
        
        # Execute and display results
        results = self.fifo.execute()
        self.display_results(results)
    
    def test_sjf(self) -> None:
        """Test the SJF dispatcher with sample data."""
        print("\n>>> Testing SJF (Shortest Job First) Dispatcher")
        self.load_sample_data()
        self.sjf.reset()
        
        # Add all test processes to SJF
        for process in self.test_data:
            self.sjf.add_process(process["id"], process["burst_time"])
        
        # Execute and display results
        results = self.sjf.execute()
        self.display_results(results)
    
    def test_priority(self) -> None:
        """Test the Priority dispatcher with sample data."""
        print("\n>>> Testing Priority Dispatcher")
        self.load_sample_data()
        self.priority.reset()
        
        # Add all test processes to Priority
        for process in self.test_data:
            self.priority.add_process(process["id"], process["burst_time"], process["priority"])
        
        # Execute and display results
        results = self.priority.execute()
        self.display_results(results)
    
    def test_round_robin(self) -> None:
        """Test the Round Robin dispatcher with sample data."""
        print("\n>>> Testing Round Robin Dispatcher")
        self.load_sample_data()
        self.round_robin.reset()
        
        # Add all test processes to Round Robin
        for process in self.test_data:
            self.round_robin.add_process(process["id"], process["burst_time"])
        
        # Execute and display results
        results = self.round_robin.execute()
        self.display_results(results)
    
    def compare_all_algorithms(self) -> None:
        """Compare all algorithms side by side with the same test data."""
        print("\n>>> Comparing All Algorithms")
        print("Using same test data for fair comparison...\n")
        
        self.load_sample_data()
        
        # Execute each algorithm
        self.fifo.reset()
        self.sjf.reset()
        self.priority.reset()
        self.round_robin.reset()
        
        for process in self.test_data:
            self.fifo.add_process(process["id"], process["burst_time"])
            self.sjf.add_process(process["id"], process["burst_time"])
            self.priority.add_process(process["id"], process["burst_time"], process["priority"])
            self.round_robin.add_process(process["id"], process["burst_time"])
        
        fifo_results = self.fifo.execute()
        sjf_results = self.sjf.execute()
        priority_results = self.priority.execute()
        rr_results = self.round_robin.execute()
        
        # Display comparison summary
        print("\n" + "="*70)
        print(f"{'Algorithm':<25} {'Total Time':<20} {'Avg Wait Time':<20}")
        print("="*70)
        print(f"{fifo_results['algorithm']:<25} {fifo_results['total_time']:<20} "
              f"{fifo_results['average_waiting_time']:<20.2f}")
        print(f"{sjf_results['algorithm']:<25} {sjf_results['total_time']:<20} "
              f"{sjf_results['average_waiting_time']:<20.2f}")
        print(f"{priority_results['algorithm']:<25} {priority_results['total_time']:<20} "
              f"{priority_results['average_waiting_time']:<20.2f}")
        print(f"{rr_results['algorithm']:<25} {rr_results['total_time']:<20} "
              f"{rr_results['average_waiting_time']:<20.2f}")
        print("="*70)
        
        # Find best algorithm
        all_results = [fifo_results, sjf_results, priority_results, rr_results]
        best_by_time = min(all_results, key=lambda x: x['total_time'])
        best_by_wait = min(all_results, key=lambda x: x['average_waiting_time'])
        
        print(f"\nBest Total Time: {best_by_time['algorithm']}")
        print(f"Best Average Wait Time: {best_by_wait['algorithm']}")
    
    def test_custom_input(self) -> None:
        """Allow user to input custom process data and test all algorithms."""
        print("\n>>> Custom Input Mode")
        print("Enter process data (or 'done' when finished)")
        
        self.test_data.clear()
        process_count = 0
        
        while True:
            try:
                process_id = input(f"\nProcess {process_count + 1} ID (or 'done'): ").strip()
                
                if process_id.lower() == 'done':
                    if process_count == 0:
                        print("At least one process is required!")
                        continue
                    break
                
                burst_time = int(input(f"Burst time for {process_id}: "))
                priority = int(input(f"Priority for {process_id} (1-10): "))
                
                if burst_time <= 0 or priority <= 0:
                    print("Burst time and priority must be positive!")
                    continue
                
                self.add_test_process(process_id, burst_time, priority)
                process_count += 1
                
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        
        # Test all algorithms with custom data
        print("\n" + "="*60)
        print("Testing All Algorithms with Custom Data")
        print("="*60)
        
        self.fifo.reset()
        self.sjf.reset()
        self.priority.reset()
        self.round_robin.reset()
        
        for process in self.test_data:
            self.fifo.add_process(process["id"], process["burst_time"])
            self.sjf.add_process(process["id"], process["burst_time"])
            self.priority.add_process(process["id"], process["burst_time"], process["priority"])
            self.round_robin.add_process(process["id"], process["burst_time"])
        
        self.display_results(self.fifo.execute())
        self.display_results(self.sjf.execute())
        self.display_results(self.priority.execute())
        self.display_results(self.round_robin.execute())
    
    def run(self) -> None:
        """Main application loop - display menu and handle user input."""
        while True:
            self.print_menu()
            choice = input("\nEnter your choice (0-6): ").strip()
            
            if choice == '0':
                print("\nExiting... Goodbye!")
                break
            elif choice == '1':
                self.test_fifo()
            elif choice == '2':
                self.test_sjf()
            elif choice == '3':
                self.test_priority()
            elif choice == '4':
                self.test_round_robin()
            elif choice == '5':
                self.compare_all_algorithms()
            elif choice == '6':
                self.test_custom_input()
            else:
                print("Invalid choice! Please enter a number between 0 and 6.")
            
            # Ask if user wants to continue
            if choice != '0':
                input("\nPress Enter to continue...")


def main() -> None:
    """Entry point for the dispatch algorithm tester application."""
    try:
        tester = DispatcherTester()
        tester.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
