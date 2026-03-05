"""
Test suite for FIFO Dispatcher.

This module contains unit tests for the FIFO (First In First Out) dispatch
algorithm to verify correct functionality across various scenarios.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from disp_algorithms.fifo_disp import FIFODispatcher


class TestFIFODispatcher:
    """Test cases for FIFO Dispatcher."""
    
    def setup_method(self):
        """Initialize a fresh dispatcher instance before each test."""
        self.dispatcher = FIFODispatcher()
    
    def test_single_process(self):
        """
        Test FIFO with a single process.
        
        Expected: Process should execute from time 0 to 5 with 0 waiting time.
        """
        self.dispatcher.add_process("P1", 5)
        results = self.dispatcher.execute()
        
        assert results["total_time"] == 5, "Total time should be 5"
        assert results["average_waiting_time"] == 0, "Waiting time should be 0"
        assert len(results["execution_log"]) == 1, "Should have one execution log entry"
        print("✓ test_single_process passed")
    
    def test_multiple_processes_order(self):
        """
        Test FIFO maintains arrival order.
        
        Expected: Processes should execute in order P1->P2->P3 regardless of burst time.
        """
        self.dispatcher.add_process("P1", 5)
        self.dispatcher.add_process("P2", 3)
        self.dispatcher.add_process("P3", 8)
        results = self.dispatcher.execute()
        
        # Verify execution order
        assert results["execution_log"][0]["process_id"] == "P1", "P1 should execute first"
        assert results["execution_log"][1]["process_id"] == "P2", "P2 should execute second"
        assert results["execution_log"][2]["process_id"] == "P3", "P3 should execute third"
        
        # Verify total time: 5 + 3 + 8 = 16
        assert results["total_time"] == 16, "Total time should be 16"
        
        # Verify waiting times: P1=0, P2=5, P3=8, avg=(0+5+8)/3=4.33
        assert results["execution_log"][0]["waiting_time"] == 0
        assert results["execution_log"][1]["waiting_time"] == 5
        assert results["execution_log"][2]["waiting_time"] == 8
        
        print("✓ test_multiple_processes_order passed")
    
    def test_equal_burst_times(self):
        """
        Test FIFO with processes having equal burst times.
        
        Expected: All processes should maintain entry order with equal burst times.
        """
        self.dispatcher.add_process("P1", 4)
        self.dispatcher.add_process("P2", 4)
        self.dispatcher.add_process("P3", 4)
        results = self.dispatcher.execute()
        
        assert results["total_time"] == 12, "Total time should be 12"
        assert results["average_waiting_time"] == 4, "Average waiting time should be 4"
        
        print("✓ test_equal_burst_times passed")
    
    def test_reset_dispatcher(self):
        """
        Test that reset clears the dispatcher state.
        
        Expected: After reset, queue and execution log should be empty.
        """
        self.dispatcher.add_process("P1", 5)
        self.dispatcher.reset()
        
        assert len(self.dispatcher.queue) == 0, "Queue should be empty after reset"
        assert len(self.dispatcher.execution_log) == 0, "Execution log should be empty after reset"
        
        print("✓ test_reset_dispatcher passed")
    
    def test_large_burst_time(self):
        """
        Test FIFO with processes having large burst times.
        
        Expected: Should handle large values correctly.
        """
        self.dispatcher.add_process("P1", 100)
        self.dispatcher.add_process("P2", 50)
        results = self.dispatcher.execute()
        
        assert results["total_time"] == 150, "Total time should be 150"
        
        print("✓ test_large_burst_time passed")


def run_all_tests():
    """Execute all FIFO dispatcher tests."""
    print("\n" + "="*60)
    print("Running FIFO Dispatcher Tests...")
    print("="*60)
    
    test_suite = TestFIFODispatcher()
    
    try:
        test_suite.setup_method()
        test_suite.test_single_process()
        
        test_suite.setup_method()
        test_suite.test_multiple_processes_order()
        
        test_suite.setup_method()
        test_suite.test_equal_burst_times()
        
        test_suite.setup_method()
        test_suite.test_reset_dispatcher()
        
        test_suite.setup_method()
        test_suite.test_large_burst_time()
        
        print("\n" + "="*60)
        print("✓ All FIFO tests passed!")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
