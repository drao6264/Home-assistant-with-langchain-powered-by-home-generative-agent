# langchain_handler.py (Python Script in /config/python_scripts)
# This script is triggered by an automation and calls your LangChain-based NLP processor.

command = data.get("command", "")
if not command:
    logger.warning("No command provided to langchain_handler.")
    return

# Add the custom integration path
import sys
sys.path.append("/config/custom_components/home_generative_agent/langchain_core")

# Import the main processing function
from main import process_command

# Call the handler
process_command(hass, command)
