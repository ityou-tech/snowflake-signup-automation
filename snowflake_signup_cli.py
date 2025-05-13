#!/usr/bin/env python3
"""
CLI wrapper for the Snowflake signup automation script.
Provides a command-line interface for the snowflake_signup.py script.
"""

import argparse
import asyncio
import sys
from typing import Dict, Any, Optional

# Import the run function from the original script
from snowflake_signup import run, main

def parse_args() -> Dict[str, Any]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Automate the Snowflake signup process using Playwright."
    )
    # Define mutually exclusive group for headless/visible mode
    browser_group = parser.add_mutually_exclusive_group()
    browser_group.add_argument(
        "--visible", action="store_true", default=True, help="Run with a visible browser window (default)"
    )
    browser_group.add_argument(
        "--headless", action="store_false", dest="visible", help="Run without a visible browser window"
    )
    
    # Define other arguments
    parser.add_argument(
        "--first-name", default="Enri", help="First name for the signup form (default: 'Enri')"
    )
    parser.add_argument(
        "--last-name", default="Peters", help="Last name for the signup form (default: 'Peters')"
    )
    parser.add_argument(
        "--email", default="enri@ityou.tech", help="Email address for the signup form (default: 'enri@ityou.tech')"
    )
    parser.add_argument(
        "--company", default="ITYOU.tech", help="Company name for the signup form (default: 'ITYOU.tech')"
    )
    parser.add_argument(
        "--job-title", default="IT Engineer", help="Job title for the signup form (default: 'IT Engineer')"
    )
    parser.add_argument(
        "--timeout", type=int, default=60000, help="Timeout in milliseconds (default: 60000)"
    )
    
    return vars(parser.parse_args())

def display_parameters(args: Dict[str, Any]) -> None:
    """Display the parameters being used for the signup process."""
    print("Running Snowflake signup automation with the following parameters:")
    print(f"  First Name: {args['first_name']}")
    print(f"  Last Name: {args['last_name']}")
    print(f"  Email: {args['email']}")
    print(f"  Company: {args['company']}")
    print(f"  Job Title: {args['job_title']}")
    print(f"  Browser Mode: {'Visible' if args['visible'] else 'Headless'}")
    print(f"  Timeout: {args['timeout']} ms")
    print("\nNote: These parameters are for display only. The original script uses default values.")
    print("To modify the actual values, update the snowflake_signup.py file directly.\n")

def main() -> None:
    """Main entry point for the CLI."""
    args = parse_args()
    display_parameters(args)
    
    # Simply call the main function from the original script
    # since we can't modify it to accept our parameters
    print("Starting Snowflake signup automation...")
    asyncio.run(main())

if __name__ == "__main__":
    main()