#!/usr/bin/env python3
"""
Demo script to showcase the CPU Dispatch Algorithm Tester CLI.

This script demonstrates the main menu functionality without requiring
interactive user input.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from main import DispatcherTester


def main():
    """Run the demo showcasing all features of the dispatcher tester."""
    print("\n" + "="*70)
    print("CPU DISPATCH ALGORITHM TESTER - DEMO")
    print("="*70)
    
    tester = DispatcherTester()
    
    # Load sample data for all demos
    tester.load_sample_data()
    print("\nLoaded sample test data:")
    for process in tester.test_data:
        print(f"  {process['id']}: Burst Time={process['burst_time']}, Priority={process['priority']}")
    
    # Demo 1: FIFO
    print("\n" + "-"*70)
    print("1. FIFO (First In First Out) Dispatcher")
    print("-"*70)
    tester.test_fifo()
    
    # Demo 2: SJF
    print("\n" + "-"*70)
    print("2. SJF (Shortest Job First) Dispatcher")
    print("-"*70)
    tester.test_sjf()
    
    # Demo 3: Priority
    print("\n" + "-"*70)
    print("3. Priority Dispatcher")
    print("-"*70)
    tester.test_priority()
    
    # Demo 4: Round Robin
    print("\n" + "-"*70)
    print("4. Round Robin Dispatcher")
    print("-"*70)
    tester.test_round_robin()
    
    # Demo 5: Comparison
    print("\n" + "-"*70)
    print("5. Algorithm Comparison")
    print("-"*70)
    tester.compare_all_algorithms()
    
    print("\n" + "="*70)
    print("Demo completed! Run 'python3 src/main.py' for interactive mode.")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)
