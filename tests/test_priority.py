"""
Test suite for Priority Dispatcher.

This module contains unit tests for the Priority dispatch algorithm to verify
correct scheduling based on priority levels.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from disp_algorithms.priority_disp import PriorityDispatcher


class TestPriorityDispatcher:
    """Test cases for Priority Dispatcher."""
    
    def setup_method(self):
        """Initialize a fresh dispatcher instance before each test."""
        self.dispatcher = PriorityDispatcher()
    
    def test_priority_ordering(self):
        """
        Test that Priority dispatcher executes highest priority jobs first.
        
        Expected: Processes should execute in order of priority: P3(3)->P1(2)->P4(2)->P2(1)
        Note: When priorities are equal, order by burst time (ascending).
        """
        self.dispatcher.add_process("P1", 8, 2)      # priority 2, burst 8
        self.dispatcher.add_process("P2", 4, 1)      # priority 1, burst 4
        self.dispatcher.add_process("P3", 2, 3)      # priority 3, burst 2
        self.dispatcher.add_process("P4", 6, 2)      # priority 2, burst 6
        results = self.dispatcher.execute()
        
        # Verify execution order by priority (desc), then burst time (asc)
        execution_order = [log["process_id"] for log in results["execution_log"]]
        expected_order = ["P3", "P4", "P1", "P2"]  # Priority 3, 2,2 (burst 6<8), 1
        assert execution_order == expected_order, \
            f"Expected order {expected_order}, got {execution_order}"
        
        print("✓ test_priority_ordering passed")
    
    def test_single_process_priority(self):
        """
        Test Priority dispatcher with a single process.
        
        Expected: Process executes with 0 waiting time.
        """
        self.dispatcher.add_process("P1", 10, 5)
        results = self.dispatcher.execute()
        
        assert results["total_time"] == 10, "Total time should be 10"
        assert results["average_waiting_time"] == 0, "Waiting time should be 0"
        
        print("✓ test_single_process_priority passed")
    
    def test_all_same_priority(self):
        """
        Test Priority dispatcher when all processes have same priority.
        
        Expected: When priorities are equal, processes should be ordered by burst time (SJF tiebreaker).
        """
        self.dispatcher.add_process("P1", 8, 5)
        self.dispatcher.add_process("P2", 3, 5)
        self.dispatcher.add_process("P3", 6, 5)
        results = self.dispatcher.execute()
        
        # All have priority 5, so should be ordered by burst time: P2(3)->P3(6)->P1(8)
        execution_order = [log["process_id"] for log in results["execution_log"]]
        expected_order = ["P2", "P3", "P1"]
        assert execution_order == expected_order, \
            f"Expected order {expected_order}, got {execution_order}"
        
        assert results["total_time"] == 17, "Total time should be 17"
        
        print("✓ test_all_same_priority passed")
    
    def test_priority_levels(self):
        """
        Test that higher numerical priority values execute first.
        
        Expected: Priority 10 > Priority 5 > Priority 1
        """
        self.dispatcher.add_process("P_Low", 5, 1)      # Low priority
        self.dispatcher.add_process("P_High", 5, 10)    # High priority
        self.dispatcher.add_process("P_Med", 5, 5)      # Medium priority
        results = self.dispatcher.execute()
        
        execution_order = [log["process_id"] for log in results["execution_log"]]
        expected_order = ["P_High", "P_Med", "P_Low"]
        assert execution_order == expected_order, \
            f"Expected order {expected_order}, got {execution_order}"
        
        print("✓ test_priority_levels passed")
    
    def test_reset_dispatcher_priority(self):
        """
        Test that reset clears the dispatcher state.
        
        Expected: After reset, processes list and execution log should be empty.
        """
        self.dispatcher.add_process("P1", 5, 3)
        self.dispatcher.add_process("P2", 3, 2)
        self.dispatcher.reset()
        
        assert len(self.dispatcher.processes) == 0, "Processes list should be empty after reset"
        assert len(self.dispatcher.execution_log) == 0, "Execution log should be empty after reset"
        
        print("✓ test_reset_dispatcher_priority passed")
    
    def test_mixed_priorities_and_burst_times(self):
        """
        Test complex scenario with mixed priorities and burst times.
        
        Expected: Correct ordering by priority first, then burst time.
        """
        # Processes with various combinations
        self.dispatcher.add_process("P1", 10, 3)   # Mid priority, long burst
        self.dispatcher.add_process("P2", 2, 5)    # High priority, short burst
        self.dispatcher.add_process("P3", 8, 3)    # Mid priority, medium burst
        self.dispatcher.add_process("P4", 1, 2)    # Low priority, short burst
        self.dispatcher.add_process("P5", 5, 5)    # High priority, medium burst
        results = self.dispatcher.execute()
        
        # Expected order:
        # Priority 5: P2(burst 2), P5(burst 5)
        # Priority 3: P3(burst 8), P1(burst 10)
        # Priority 2: P4(burst 1)
        execution_order = [log["process_id"] for log in results["execution_log"]]
        expected_order = ["P2", "P5", "P3", "P1", "P4"]
        assert execution_order == expected_order, \
            f"Expected order {expected_order}, got {execution_order}"
        
        expected_total = 2 + 5 + 8 + 10 + 1  # Sum of all burst times
        assert results["total_time"] == expected_total, \
            f"Total time should be {expected_total}"
        
        print("✓ test_mixed_priorities_and_burst_times passed")


def run_all_tests():
    """Execute all Priority dispatcher tests."""
    print("\n" + "="*60)
    print("Running Priority Dispatcher Tests...")
    print("="*60)
    
    test_suite = TestPriorityDispatcher()
    
    try:
        test_suite.setup_method()
        test_suite.test_priority_ordering()
        
        test_suite.setup_method()
        test_suite.test_single_process_priority()
        
        test_suite.setup_method()
        test_suite.test_all_same_priority()
        
        test_suite.setup_method()
        test_suite.test_priority_levels()
        
        test_suite.setup_method()
        test_suite.test_reset_dispatcher_priority()
        
        test_suite.setup_method()
        test_suite.test_mixed_priorities_and_burst_times()
        
        print("\n" + "="*60)
        print("✓ All Priority tests passed!")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
