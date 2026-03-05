# CPU Dispatch Algorithm Tester

A comprehensive Python application for testing and comparing various CPU scheduling and dispatch algorithms. This project includes implementations of classic scheduling algorithms used in operating systems for process management.

## 📋 Features

- **Multiple Scheduling Algorithms**:
  - FIFO (First In First Out)
  - SJF (Shortest Job First)
  - Priority-based Scheduling
  - Round Robin with time quantum

- **Interactive CLI Menu**: User-friendly interface to test individual algorithms
- **Algorithm Comparison**: Side-by-side comparison of all algorithms
- **Custom Input**: Test algorithms with user-defined process parameters
- **Full Test Suite**: 17 passing test cases
- **Demo Script**: Non-interactive demonstration of all features

## 🚀 Quick Start

### No Installation Required!
This project has **zero external dependencies** - uses only Python standard library.

### Interactive CLI Mode
```bash
python3 src/main.py
```

### Run Demo
```bash
python3 demo.py
```

### Run Tests
```bash
python3 tests/run_all_tests.py
```

## 📦 Modern Package Setup

Uses `pyproject.toml` (PEP 517/518 standard) for project configuration and optional dependency management. See [requirements/](requirements/) folder for details.

## 📊 Algorithms Implemented

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **FIFO** | Processes execute in arrival order | Simple, fair scheduling |
| **SJF** | Shortest burst time first | Minimize waiting time |
| **Priority** | Higher priority executes first | Importance-based scheduling |
| **Round Robin** | Fixed time quantum per process | Interactive systems |

## 📁 Project Structure

```
src/
├── main.py                      # Interactive CLI menu
├── disp_algorithms/
    ├── fifo_disp.py            # FIFO implementation
    ├── sjf_disp.py             # SJF implementation
    ├── priority_disp.py        # Priority implementation
    └── round_robin_fifo_disp.py # Round Robin implementation

tests/
├── test_fifo.py                # 5 test cases
├── test_sjf.py                 # 6 test cases
├── test_priority.py            # 6 test cases
└── run_all_tests.py            # Test runner

demo.py                          # Demonstration script
```

## ✅ Test Coverage

- **FIFO Tests**: 5 cases ✓
- **SJF Tests**: 6 cases ✓
- **Priority Tests**: 6 cases ✓
- **Total**: 17 test cases - All passing ✓

## 💻 Sample Output

```
Algorithm:.................... SJF
Total Execution Time:......... 20 units
Average Waiting Time:......... 5.00 units

Execution Log:
Process    Start    End      Burst    Wait    
P3         0        2        2        0       
P2         2        6        4        2       
P4         6        12       6        6       
P1         12       20       8        12      
```

## 🎯 Key Features

✅ Fully commented code with docstrings
✅ Type hints for all functions
✅ Comprehensive test suite
✅ Interactive CLI menu
✅ Algorithm comparison
✅ Custom input support
✅ Detailed execution logs

## 📚 Learn About

- CPU scheduling algorithms
- Performance metrics analysis
- Algorithm comparison
- Python best practices
- Test-driven development

## 📄 License

MIT License