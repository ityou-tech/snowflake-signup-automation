#!/bin/bash
# This script demonstrates how to set up and use the project with uv
set -e

VENV_DIR=".venv"

echo "Setting up Snowflake Signup Automation with uv"
echo "=============================================="

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Installing uv..."
    pip install uv
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in ./$VENV_DIR..."
    uv venv
else
    echo "Using existing virtual environment in ./$VENV_DIR"
fi

# Source the activation script based on shell type
if [ -n "$BASH_VERSION" ]; then
    echo "Activating virtual environment for bash..."
    source "$VENV_DIR/bin/activate"
elif [ -n "$ZSH_VERSION" ]; then
    echo "Activating virtual environment for zsh..."
    source "$VENV_DIR/bin/activate"
else
    echo "Please activate the virtual environment manually:"
    echo "source $VENV_DIR/bin/activate"
    exit 1
fi

# Check if activation worked
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Failed to activate virtual environment. Please activate it manually:"
    echo "source $VENV_DIR/bin/activate"
    exit 1
fi

echo "Installing project using uv..."
uv pip install -e .

echo "Installing Playwright browsers..."
python -m playwright install chromium

echo ""
echo "Setup complete! You can now use the Snowflake signup automation tools:"
echo ""
echo "Basic usage:"
echo "  snowflake-signup                 # Run the main signup script"
echo ""
echo "Generate test data:"
echo "  generate-test-data --count 5 --print  # Generate 5 test data entries and print them"
echo ""
echo "Process multiple signups:"
echo "  batch-signup --delay 30          # Process entries with 30 seconds delay between each"
echo ""
echo "For more information, see the README.md file."
echo ""
echo "Note: Remember to activate the virtual environment when you restart your terminal:"
echo "source $VENV_DIR/bin/activate"