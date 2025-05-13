#!/usr/bin/env python3
"""
Demo script for the Snowflake signup automation.
Runs the signup process with sample test credentials.
"""

import argparse
import asyncio
import json
import random
from pathlib import Path
from typing import Dict, Any, Optional

# Import the run function from the original script
from snowflake_signup import run, main

def load_test_data(filepath: str = "test_data.json") -> Dict[str, Any]:
    """Load test data from a JSON file."""
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        
        # Return a random entry from the test data
        if "test_data" in data and len(data["test_data"]) > 0:
            return random.choice(data["test_data"])
        else:
            raise ValueError("No test data entries found in the file")
    
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        print(f"Error loading test data: {e}")
        print("Using default test data instead")
        
        # Return default test data
        return {
            "first_name": "Demo",
            "last_name": "User",
            "email": f"demo{random.randint(100, 999)}@example.com",
            "company": "Demo Company",
            "job_title": "Test Engineer",
        }

def parse_args() -> Dict[str, Any]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run a demo of the Snowflake signup automation"
    )
    
    # Define mutually exclusive group for headless/visible mode
    browser_group = parser.add_mutually_exclusive_group()
    browser_group.add_argument(
        "--visible", action="store_true", default=True, help="Run with a visible browser window (default)"
    )
    browser_group.add_argument(
        "--headless", action="store_false", dest="visible", help="Run without a visible browser window"
    )
    
    parser.add_argument(
        "--timeout", type=int, default=60000, help="Timeout in milliseconds (default: 60000)"
    )
    parser.add_argument(
        "--data-file", default="test_data.json", help="Path to the test data JSON file (default: test_data.json)"
    )
    
    return vars(parser.parse_args())

def display_test_data(test_data: Dict[str, str]) -> None:
    """Display the test data being used."""
    print("Running Snowflake signup demo with the following test data:")
    print(f"  First Name: {test_data['first_name']}")
    print(f"  Last Name: {test_data['last_name']}")
    print(f"  Email: {test_data['email']}")
    print(f"  Company: {test_data['company']}")
    print(f"  Job Title: {test_data['job_title']}")
    print("\nNote: These values are for display only. The original script uses its own default values.")
    print("To modify the actual values, update the snowflake_signup.py file directly.\n")

def main() -> None:
    """Main function for the demo script."""
    args = parse_args()
    test_data = load_test_data(args["data_file"])
    display_test_data(test_data)
    
    print("Starting Snowflake signup demo...")
    print(f"Browser mode: {'Visible' if args['visible'] else 'Headless'}")
    print(f"Timeout: {args['timeout']} ms")
    
    # Simply call the main function from the original script
    # since we can't modify it to accept our parameters
    asyncio.run(main())

if __name__ == "__main__":
    main()