"""
Test Runner - Execute all dispatcher tests

Run all test files to validate the dispatcher implementations.
"""

import sys
import subprocess
from pathlib import Path


def run_tests():
    """Run all test files in the tests directory."""
    test_dir = Path(__file__).parent
    test_files = sorted(test_dir.glob("test_*.py"))
    
    print("\n" + "="*70)
    print("RUNNING ALL DISPATCHER TESTS")
    print("="*70)
    
    failed_tests = []
    passed_tests = []
    
    for test_file in test_files:
        print(f"\nRunning {test_file.name}...")
        result = subprocess.run([sys.executable, str(test_file)], capture_output=True, text=True)
        
        if result.returncode == 0:
            passed_tests.append(test_file.name)
            print(result.stdout)
        else:
            failed_tests.append(test_file.name)
            print(f"FAILED: {test_file.name}")
            print(result.stdout)
            print(result.stderr)
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Passed: {len(passed_tests)}/{len(test_files)}")
    print(f"Failed: {len(failed_tests)}/{len(test_files)}")
    
    if passed_tests:
        print("\n✓ Passed Tests:")
        for test in passed_tests:
            print(f"  - {test}")
    
    if failed_tests:
        print("\n✗ Failed Tests:")
        for test in failed_tests:
            print(f"  - {test}")
        return False
    
    print("\n✓ All tests passed successfully!")
    return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
