# Snowflake Signup Automation

> **IMPORTANT: FOR EDUCATIONAL PURPOSES ONLY**
>
> This script is provided for educational purposes only. The script demonstrates browser automation techniques and should only be used for legitimate learning purposes.
>
> Any misuse of this script is strictly against the Snowflake Self-Service On Demand Terms of Service (https://www.snowflake.com/en/legal/terms-of-service/self-service-on-demand-terms-of-service/).
>
> By using this script, you acknowledge that you're using it solely for educational purposes and assume all responsibility for any consequences of using this script.

This script automates the process of signing up for a Snowflake account using Playwright for browser automation. The default configuration selects the "Business Critical" edition of Snowflake and AWS as the cloud provider, but these settings can be customized.

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

### Configuration

The script now uses a configuration system that allows you to specify parameters in multiple ways:

1. **Command-line arguments**: Provide parameters directly when running the script
2. **Configuration file**: Use a JSON file to store configuration
3. **Environment variables**: Set `SNOWFLAKE_FIRST_NAME`, `SNOWFLAKE_EMAIL`, etc.
4. **Interactive prompts**: If required fields are missing, the script will prompt for input

A sample configuration file `snowflake_config.json.example` is provided. You can copy this to `snowflake_config.json` and modify it with your details:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "company": "Example Inc",
  "job_title": "Data Engineer",
  "cloud_provider": "Amazon Web Services",
  "edition": "Business Critical"
}
```

You can use the `--save-config` flag to save your command-line arguments to a config file:

```bash
snowflake-signup --first-name "John" --last-name "Doe" --email "john.doe@example.com" --save-config
```

### Command-line Options

- `--first-name`: First name for the signup form
- `--last-name`: Last name for the signup form
- `--email`: Email address for the signup form
- `--company`: Company name for the signup form
- `--job-title`: Job title for the signup form
- `--edition`: Snowflake edition (choices: "Standard", "Enterprise", "Business Critical"; default: "Business Critical")
- `--cloud-provider`: Cloud provider (choices: "Amazon Web Services", "Microsoft Azure", "Google Cloud Platform"; default: "Amazon Web Services")
- `--config-file`: Path to JSON configuration file
- `--save-config`: Save the provided arguments to a configuration file
- `--visible`: Run with a visible browser window (default behavior)
- `--headless`: Run without a visible browser window (mutually exclusive with --visible)
- `--timeout`: Set timeout in milliseconds (default: 60000, i.e., 1 minute)

## Notes

- The script will display a disclaimer and require confirmation before proceeding
- By default, the script runs with a visible browser. Use the `--headless` flag to run without a visible browser.
- The script handles cookie consent dialogs, form filling, dropdown selections, and multi-step signup processes.
- The script assumes the signup flow remains consistent. If Snowflake changes their signup process, the script may need to be updated.
- All personal information is provided by the user and not hardcoded in the script.

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