"""Initialize Home Generative Agent integration."""

import logging
from homeassistant.core import HomeAssistant

from .langchain_core.main import run_assistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "home_generative_agent"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Home Generative Agent integration."""
    _LOGGER.info("Setting up Home Generative Agent...")

    # Run the LangChain NLP assistant
    await run_assistant(hass)

    _LOGGER.info("Home Generative Agent setup complete.")
    return True
