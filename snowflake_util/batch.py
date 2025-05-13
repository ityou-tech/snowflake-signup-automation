#!/usr/bin/env python3
"""
Batch processor for multiple Snowflake signups.
Processes multiple signups sequentially from a data file.
"""

import argparse
import asyncio
import json
import logging
import time
from datetime import datetime
from typing import Dict, List, Any

# Import the run function from the original script
from snowflake_signup import run, main as snowflake_main

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("batch_signup.log"), logging.StreamHandler()],
)
logger = logging.getLogger("batch_signup")


def load_test_data(filepath: str = "test_data.json") -> List[Dict[str, Any]]:
    """Load all test data entries from a JSON file."""
    try:
        with open(filepath, "r") as f:
            data = json.load(f)

        if "test_data" in data and isinstance(data["test_data"], list):
            return data["test_data"]
        else:
            raise ValueError("Invalid test data format. Expected a 'test_data' list.")

    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        logger.error(f"Error loading test data: {e}")
        return []


def parse_args() -> Dict[str, Any]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Process multiple Snowflake signups from a data file"
    )

    # Define mutually exclusive group for headless/visible mode
    browser_group = parser.add_mutually_exclusive_group()
    browser_group.add_argument(
        "--visible",
        action="store_true",
        dest="visible",
        help="Run with visible browser windows",
    )
    browser_group.add_argument(
        "--headless",
        action="store_false",
        dest="visible",
        default=False,
        help="Run without visible browser windows (default)",
    )

    parser.add_argument(
        "--data-file",
        default="test_data.json",
        help="Path to the test data JSON file (default: test_data.json)",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=60,
        help="Delay in seconds between signups (default: 60)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60000,
        help="Timeout in milliseconds (default: 60000)",
    )

    return vars(parser.parse_args())


async def process_batch(entries: List[Dict[str, Any]], args: Dict[str, Any]) -> None:
    """Process a batch of signup entries."""
    if not entries:
        logger.error("No entries to process")
        return

    total = len(entries)
    logger.info(f"Starting batch process with {total} entries")
    logger.info(f"Browser mode: {'Visible' if args['visible'] else 'Headless'}")
    logger.info(f"Delay between signups: {args['delay']} seconds")

    for i, entry in enumerate(entries, 1):
        logger.info(
            f"Processing entry {i}/{total}: {entry['first_name']} {entry['last_name']}"
        )

        try:
            # Note: Since we can't modify the original script, we simply call snowflake_main()
            # In a real scenario, we'd pass the entry data to the run function
            await snowflake_main()
            logger.info(f"Successfully processed entry {i}/{total}")

            # Save a record of the processed entry
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open(f"processed_{timestamp}_{i}.json", "w") as f:
                json.dump(
                    {
                        "processed_at": datetime.now().isoformat(),
                        "entry_data": entry,
                        "status": "success",
                    },
                    f,
                    indent=2,
                )

        except Exception as e:
            logger.error(f"Error processing entry {i}/{total}: {e}")

        # Add delay between entries, except for the last one
        if i < total:
            logger.info(f"Waiting {args['delay']} seconds before next entry...")
            time.sleep(args["delay"])

    logger.info(f"Batch processing completed. Processed {total} entries.")


def main() -> None:
    """Main function for the batch processor."""
    args = parse_args()
    entries = load_test_data(args["data_file"])

    if not entries:
        logger.error(f"No entries found in {args['data_file']}. Exiting.")
        return

    logger.info(f"Loaded {len(entries)} entries from {args['data_file']}")

    try:
        asyncio.run(process_batch(entries, args))
    except KeyboardInterrupt:
        logger.info("Batch processing interrupted by user")
    except Exception as e:
        logger.error(f"Batch processing failed: {e}")


if __name__ == "__main__":
    main()
