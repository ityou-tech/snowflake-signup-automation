#!/usr/bin/env python3
"""
CLI wrapper for the Snowflake signup automation script.
Provides a command-line interface for the snowflake_signup.py script.

EDUCATIONAL PURPOSE ONLY: This script is provided for educational purposes only.
Misuse is against Snowflake's Terms of Service.
"""

import argparse
import asyncio
import json
import os
from typing import Dict, Any, Optional
from playwright.async_api import async_playwright

# Import from the main script and config
from snowflake_signup import run
from config import DEFAULT_CONFIG, print_disclaimer


def parse_args() -> Dict[str, Any]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Automate the Snowflake signup process using Playwright. FOR EDUCATIONAL PURPOSES ONLY."
    )
    # Define mutually exclusive group for headless/visible mode
    browser_group = parser.add_mutually_exclusive_group()
    browser_group.add_argument(
        "--visible",
        action="store_true",
        default=True,
        help="Run with a visible browser window (default)",
    )
    browser_group.add_argument(
        "--headless",
        action="store_false",
        dest="visible",
        help="Run without a visible browser window",
    )

    # Define other arguments
    parser.add_argument("--first-name", help="First name for the signup form")
    parser.add_argument("--last-name", help="Last name for the signup form")
    parser.add_argument("--email", help="Email address for the signup form")
    parser.add_argument("--company", help="Company name for the signup form")
    parser.add_argument("--job-title", help="Job title for the signup form")
    parser.add_argument(
        "--edition",
        choices=["Standard", "Enterprise", "Business Critical"],
        default="Business Critical",
        help="Snowflake edition (default: Business Critical)",
    )
    parser.add_argument(
        "--cloud-provider",
        choices=["Amazon Web Services", "Microsoft Azure", "Google Cloud Platform"],
        default="Amazon Web Services",
        help="Cloud provider (default: Amazon Web Services)",
    )
    parser.add_argument("--config-file", help="Path to JSON configuration file")
    parser.add_argument(
        "--timeout",
        type=int,
        default=60000,
        help="Timeout in milliseconds (default: 60000)",
    )
    parser.add_argument(
        "--save-config",
        action="store_true",
        help="Save provided arguments to config file",
    )

    return vars(parser.parse_args())


def load_config_from_args(args: Dict[str, Any]) -> Dict[str, Any]:
    """Load configuration from command-line arguments, file, and/or environment variables."""
    config = DEFAULT_CONFIG.copy()

    # First, try to load from specified config file
    if args.get("config_file") and os.path.exists(args["config_file"]):
        try:
            with open(args["config_file"], "r") as f:
                file_config = json.load(f)
                config.update({k: v for k, v in file_config.items() if v})
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config file: {e}")

    # Then, override with environment variables
    for key in config.keys():
        env_var = f"SNOWFLAKE_{key.upper()}"
        if os.environ.get(env_var):
            config[key] = os.environ.get(env_var)

    # Finally, override with command-line arguments
    for key, value in args.items():
        if key in config and value is not None:
            config[key] = value

    # Save config if requested
    if args.get("save_config"):
        save_path = args.get("config_file") or "snowflake_config.json"
        try:
            with open(save_path, "w") as f:
                json.dump(config, f, indent=2)
                print(f"Configuration saved to {save_path}")
        except IOError as e:
            print(f"Error saving configuration: {e}")

    return config


def display_parameters(config: Dict[str, Any]) -> None:
    """Display the parameters being used for the signup process."""
    print("\nRunning Snowflake signup automation with the following parameters:")
    for key, value in config.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()


async def _async_cli_main() -> None:
    """Async implementation of the main CLI functionality."""
    try:
        # Parse arguments and load configuration
        args = parse_args()
        config = load_config_from_args(args)

        # Check for required fields
        missing = [k for k, v in config.items() if not v]
        if missing:
            print(f"Missing required fields: {', '.join(missing)}")
            for field in missing:
                try:
                    config[field] = input(f"Please enter {field.replace('_', ' ')}: ")
                except KeyboardInterrupt:
                    print("\nInput cancelled by user. Exiting.")
                    return

        display_parameters(config)

        # Run the main automation
        print("Starting Snowflake signup automation...")
        async with async_playwright() as playwright:
            await run(playwright, config)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")


def cli_main() -> None:
    """Main entry point for the CLI."""
    try:
        # Show disclaimer and get confirmation
        if not print_disclaimer():
            return

        # Run the async main function
        asyncio.run(_async_cli_main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        return


if __name__ == "__main__":
    cli_main()
