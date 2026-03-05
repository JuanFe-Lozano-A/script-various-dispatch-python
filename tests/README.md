# Test Suite Documentation

This directory contains comprehensive unit tests for all CPU dispatch algorithm implementations.

## Test Files

### 1. `test_fifo.py` - FIFO Dispatcher Tests
Tests the First In First Out (FIFO) scheduling algorithm.

**Test Cases:**
- `test_single_process`: Validates single process execution
- `test_multiple_processes_order`: Verifies FIFO maintains arrival order
- `test_equal_burst_times`: Tests processes with equal execution times
- `test_reset_dispatcher`: Confirms dispatcher reset functionality
- `test_large_burst_time`: Tests handling of large execution times

### 2. `test_sjf.py` - SJF Dispatcher Tests
Tests the Shortest Job First (SJF) scheduling algorithm.

**Test Cases:**
- `test_shortest_job_first_order`: Verifies correct ordering by burst time
- `test_single_process_sjf`: Validates single process execution
- `test_equal_burst_times_sjf`: Tests processes with equal burst times
- `test_sjf_improves_waiting_time`: Compares SJF vs FIFO performance
- `test_reset_dispatcher_sjf`: Confirms dispatcher reset functionality
- `test_many_processes`: Tests with multiple processes

### 3. `test_priority.py` - Priority Dispatcher Tests
Tests the Priority-based scheduling algorithm.

**Test Cases:**
- `test_priority_ordering`: Verifies correct ordering by priority
- `test_single_process_priority`: Validates single process execution
- `test_all_same_priority`: Tests tiebreaking with equal priorities
- `test_priority_levels`: Validates priority level comparison
- `test_reset_dispatcher_priority`: Confirms dispatcher reset functionality
- `test_mixed_priorities_and_burst_times`: Tests complex scheduling scenarios

## Running Tests

### Run All Tests
```bash
python3 run_all_tests.py
```

### Run Individual Test File
```bash
python3 test_fifo.py
python3 test_sjf.py
python3 test_priority.py
```

## Test Results

All tests validate:
- ✅ Correct process scheduling order
- ✅ Accurate execution timing calculations
- ✅ Proper waiting time calculations
- ✅ Dispatcher state management and reset functionality
- ✅ Edge cases (single process, equal times, many processes)

## Adding New Tests

When adding new algorithms or features:
1. Create a new test file following the naming convention: `test_<algorithm_name>.py`
2. Implement test classes inheriting the same structure
3. Include setup_method for initialization
4. Add individual test methods for each scenario
5. Implement run_all_tests() function at the module level
6. Update run_all_tests.py to include the new test file
