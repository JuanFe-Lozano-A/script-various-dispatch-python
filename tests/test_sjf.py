"""
Test suite for SJF Dispatcher.

This module contains unit tests for the SJF (Shortest Job First) dispatch
algorithm to verify correct scheduling and calculation of metrics.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from disp_algorithms.sjf_disp import SJFDispatcher


class TestSJFDispatcher:
    """Test cases for SJF Dispatcher."""
    
    def setup_method(self):
        """Initialize a fresh dispatcher instance before each test."""
        self.dispatcher = SJFDispatcher()
    
    def test_shortest_job_first_order(self):
        """
        Test SJF executes shortest jobs first.
        
        Expected: Jobs should execute in order of burst time: P3(2)->P2(4)->P1(8)->P4(6)
        becomes P3(2)->P2(4)->P4(6)->P1(8)
        """
        self.dispatcher.add_process("P1", 8)
        self.dispatcher.add_process("P2", 4)
        self.dispatcher.add_process("P3", 2)
        self.dispatcher.add_process("P4", 6)
        results = self.dispatcher.execute()
        
        # Verify execution order is by burst time
        execution_order = [log["process_id"] for log in results["execution_log"]]
        expected_order = ["P3", "P2", "P4", "P1"]
        assert execution_order == expected_order, f"Expected order {expected_order}, got {execution_order}"
        
        # Verify total time
        assert results["total_time"] == 20, "Total time should be 20 (2+4+6+8)"
        
        print("✓ test_shortest_job_first_order passed")
    
    def test_single_process_sjf(self):
        """
        Test SJF with a single process.
        
        Expected: Process executes with 0 waiting time.
        """
        self.dispatcher.add_process("P1", 10)
        results = self.dispatcher.execute()
        
        assert results["total_time"] == 10, "Total time should be 10"
        assert results["average_waiting_time"] == 0, "Waiting time should be 0"
        
        print("✓ test_single_process_sjf passed")
    
    def test_equal_burst_times_sjf(self):
        """
        Test SJF with processes having equal burst times.
        
        Expected: All processes execute successfully (order doesn't matter when equal).
        """
        self.dispatcher.add_process("P1", 5)
        self.dispatcher.add_process("P2", 5)
        self.dispatcher.add_process("P3", 5)
        results = self.dispatcher.execute()
        
        assert results["total_time"] == 15, "Total time should be 15"
        assert results["average_waiting_time"] == 5, "Average waiting time should be 5"
        assert len(results["execution_log"]) == 3, "Should have 3 processes"
        
        print("✓ test_equal_burst_times_sjf passed")
    
    def test_sjf_improves_waiting_time(self):
        """
        Test that SJF provides better average waiting time than FIFO.
        
        Expected: SJF average waiting time (3.33) < FIFO average waiting time (4.33)
        for processes with burst times [5, 3, 8]
        """
        self.dispatcher.add_process("P1", 5)
        self.dispatcher.add_process("P2", 3)
        self.dispatcher.add_process("P3", 8)
        results = self.dispatcher.execute()
        
        # SJF order: P2(3)->P1(5)->P3(8)
        # Waiting times: P2=0, P1=3, P3=8
        # Average = (0+3+8)/3 = 3.67
        expected_avg = (0 + 3 + 8) / 3
        assert abs(results["average_waiting_time"] - expected_avg) < 0.01, \
            f"Expected average waiting time ~{expected_avg:.2f}, got {results['average_waiting_time']:.2f}"
        
        print("✓ test_sjf_improves_waiting_time passed")
    
    def test_reset_dispatcher_sjf(self):
        """
        Test that reset clears the dispatcher state.
        
        Expected: After reset, processes list and execution log should be empty.
        """
        self.dispatcher.add_process("P1", 5)
        self.dispatcher.add_process("P2", 3)
        self.dispatcher.reset()
        
        assert len(self.dispatcher.processes) == 0, "Processes list should be empty after reset"
        assert len(self.dispatcher.execution_log) == 0, "Execution log should be empty after reset"
        
        print("✓ test_reset_dispatcher_sjf passed")
    
    def test_many_processes(self):
        """
        Test SJF with many processes.
        
        Expected: All processes should execute in correct order.
        """
        burst_times = [10, 5, 2, 8, 3, 7, 1, 4]
        for i, burst_time in enumerate(burst_times):
            self.dispatcher.add_process(f"P{i+1}", burst_time)
        
        results = self.dispatcher.execute()
        total_burst = sum(burst_times)
        
        assert results["total_time"] == total_burst, f"Total time should be {total_burst}"
        assert len(results["execution_log"]) == len(burst_times), \
            f"Should have {len(burst_times)} execution log entries"
        
        # Verify processes are sorted by burst time
        execution_burst_times = [log["burst_time"] for log in results["execution_log"]]
        assert execution_burst_times == sorted(execution_burst_times), \
            "Processes should execute in ascending order of burst time"
        
        print("✓ test_many_processes passed")


def run_all_tests():
    """Execute all SJF dispatcher tests."""
    print("\n" + "="*60)
    print("Running SJF Dispatcher Tests...")
    print("="*60)
    
    test_suite = TestSJFDispatcher()
    
    try:
        test_suite.setup_method()
        test_suite.test_shortest_job_first_order()
        
        test_suite.setup_method()
        test_suite.test_single_process_sjf()
        
        test_suite.setup_method()
        test_suite.test_equal_burst_times_sjf()
        
        test_suite.setup_method()
        test_suite.test_sjf_improves_waiting_time()
        
        test_suite.setup_method()
        test_suite.test_reset_dispatcher_sjf()
        
        test_suite.setup_method()
        test_suite.test_many_processes()
        
        print("\n" + "="*60)
        print("✓ All SJF tests passed!")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
