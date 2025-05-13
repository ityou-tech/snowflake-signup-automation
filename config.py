"""
Configuration for Snowflake signup automation.

This file contains configuration settings for the Snowflake signup automation.
"""

# Default settings - these are intentionally empty and should be filled by the user
DEFAULT_CONFIG = {
    "first_name": "",
    "last_name": "",
    "email": "",
    "company": "",
    "job_title": "",
    "cloud_provider": "Amazon Web Services",  # Options: "Amazon Web Services", "Microsoft Azure", "Google Cloud Platform"
    "edition": "Business Critical",  # Options: "Standard", "Enterprise", "Business Critical"
}

# Educational purpose disclaimer
DISCLAIMER = """
IMPORTANT: EDUCATIONAL PURPOSE ONLY

This script is provided for EDUCATIONAL PURPOSES ONLY. The script demonstrates
browser automation techniques and should only be used for legitimate learning purposes.

Any misuse of this script is strictly against the Snowflake Self-Service On Demand 
Terms of Service (https://www.snowflake.com/en/legal/terms-of-service/self-service-on-demand-terms-of-service/).

By using this script, you acknowledge:
1. You're using it solely for educational purposes
2. You will not use it to violate any terms of service
3. You understand that automated signup may violate Snowflake's terms
4. You assume all responsibility for any consequences of using this script

The author(s) of this script are not responsible for any misuse or resulting consequences.
"""


def print_disclaimer():
    """Print the educational purpose disclaimer."""
    print("\n" + "=" * 80)
    print(DISCLAIMER)
    print("=" * 80 + "\n")

    # Ask for confirmation with keyboard interrupt handling
    try:
        response = input(
            "Do you understand and agree to use this ONLY for educational purposes? (yes/no): "
        )
        if response.lower() not in ["yes", "y"]:
            print("Exiting as agreement was not confirmed.")
            return False
        return True
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        return False
