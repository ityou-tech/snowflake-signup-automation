# Snowflake Signup Automation

This script automates the process of signing up for a Snowflake account using Playwright for browser automation. The automation selects the "Business Critical" edition of Snowflake and AWS as the cloud provider.

## Requirements

- Python 3.7+
- Playwright
- uv (recommended for dependency management)

## Installation

The project uses Playwright for browser automation and uv for modern Python packaging.

### Using the Setup Script (Recommended)

The easiest way to set up the project is to use the provided setup script:

```bash
# Make the script executable
chmod +x setup-with-uv.sh

# Run the setup script
./setup-with-uv.sh
```

The script will:
1. Install uv if it's not already installed
2. Create and activate a Python virtual environment
3. Install the project and its dependencies using uv
4. Install Playwright browsers

### Manual Installation with uv

```bash
# Install uv if you don't have it
pip install uv

# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows

# Install project in development mode with uv
uv pip install -e .

# Install Playwright browsers
python -m playwright install chromium
```

## Usage

### Basic Usage

Run the script with the default values:

```bash
# Using the command-line script
snowflake-signup

# Or run the Python file directly
python snowflake_signup.py
```

### Advanced Usage with Command-Line Options

```bash
# Customize parameters (for display only)
snowflake-signup --first-name "John" --last-name "Doe" --email "john.doe@example.com" --company "Example Inc" --job-title "Data Engineer" --visible

# For running in headless mode
snowflake-signup --headless
```

Note: Command-line parameters are for display purposes only. To modify the actual values used in the automation, you need to edit the `snowflake_signup.py` file directly.

### Command-line Options

- `--first-name`: First name for the signup form (default: "Enri")
- `--last-name`: Last name for the signup form (default: "Peters")
- `--email`: Email address for the signup form (default: "enri@ityou.tech")
- `--company`: Company name for the signup form (default: "ITYOU.TECH")
- `--job-title`: Job title for the signup form (default: "IT Engineer")
- `--visible`: Run with a visible browser window (default behavior)
- `--headless`: Run without a visible browser window (mutually exclusive with --visible)
- `--timeout`: Set timeout in milliseconds (default: 60000, i.e., 1 minute)

## Notes

- The script will take a screenshot of the completed signup process and save it as `snowflake_signup_complete.png`
- By default, the script runs with a visible browser. Use the `--headless` flag to run without a visible browser.
- The script handles cookie consent dialogs, form filling, dropdown selections, and multi-step signup processes.
- The script assumes the signup flow remains consistent. If Snowflake changes their signup process, the script may need to be updated.

## Implementation Details

- Uses Playwright's synchronous API for browser automation
- Implements robust selectors with fallback mechanisms for resilience
- Handles retry logic for more reliable form interactions
- Captures screenshots at key steps for debugging purposes
- Provides detailed logging of the automation process

## Additional Utility Scripts

### Demo Script

Run a demo of the Snowflake signup automation with test credentials:

```bash
# Run with visible browser (default)
run-demo             

# Run in headless mode
run-demo --headless  

# Explicitly run with visible browser
run-demo --visible   

# Set custom timeout (2 minutes)
run-demo --timeout 120000  

# Use a custom test data file
run-demo --data-file custom_test_data.json
```

This script will run the signup process using sample test credentials and select the "Business Critical" edition.

#### Troubleshooting Demo Script

If you encounter issues with the demo:

1. Try increasing the timeout: `run-demo --timeout 120000`
2. Run with the visible browser to see what's happening: `run-demo --visible`
3. Check the screenshots saved during execution for debugging

### Test Data Generator

To generate random test data for the signup process:

```bash
# Generate a single test data set
generate-test-data

# Generate multiple test data sets
generate-test-data --count 5

# Generate and print to console
generate-test-data --print

# Save to a custom file
generate-test-data --output my_test_data.json
```

The generator creates random combinations of names, email addresses, company names, and job titles that can be used for testing the signup process without using real information.

### Batch Signup Processor

To process multiple signups in a batch from a data file:

```bash
# Run with default settings (60 second delay between signups)
batch-signup

# Run with custom settings
batch-signup --data-file my_test_data.json --delay 30 --visible
```

The batch processor:
- Processes each signup sequentially with configurable delays
- Maintains detailed logs in batch_signup.log
- Can run in headless mode (default) or with visible browser windows

## uv Support

This project fully supports [uv](https://github.com/astral-sh/uv), a faster Python package installer and resolver:

- All dependency specifications are compatible with uv
- The project includes uv configuration in pyproject.toml
- For best performance, we recommend using uv to install dependencies

### Easy Installation with Setup Script

The easiest way to set up the project with uv is to use the provided setup script:

```bash
# Make the script executable
chmod +x setup-with-uv.sh

# Run the setup script
./setup-with-uv.sh
```

The script will:
1. Install uv if it's not already installed
2. Create a Python virtual environment in `.venv`
3. Activate the virtual environment
4. Install the project and its dependencies using uv
5. Install the Playwright browser

### Manual Installation with uv

If you prefer to install manually:

```bash
# Install uv if you don't have it
pip install uv

# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows

# Install the project with uv
uv pip install -e .

# Install Playwright browsers
python -m playwright install chromium
```

### Configuration

The uv configuration is specified in `pyproject.toml`:

```toml
[tool.uv.resolution]
strategy = "consistent"
```

This ensures that uv uses a consistent resolution strategy for dependencies, which is important for maintaining compatibility across different environments.