"""
The Transformers Theme & Cards integration for Home Assistant.

This integration provides:
- Four Transformers-themed UI themes (Dark, Light, Silver, Dirty Metal)
- Eleven custom Lovelace cards with Transformers styling
- Authentic Transformers Movie font integration
- Automatic installation of all dependencies

For more details about this integration, please refer to the documentation at
https://github.com/loryanstrant/ha-transformers-theme-cards
"""
from __future__ import annotations

import logging
from pathlib import Path
import shutil

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "transformers_theme_cards"

__version__ = "1.0.0"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Transformers Theme & Cards integration."""
    _LOGGER.info("Setting up Transformers Theme & Cards integration")
    
    # Get the integration directory
    integration_dir = Path(__file__).parent
    
    # Set up paths
    config_dir = Path(hass.config.path())
    themes_dir = config_dir / "themes"
    www_dir = config_dir / "www"
    www_transformers_dir = www_dir / "transformers"
    
    # Ensure directories exist
    themes_dir.mkdir(exist_ok=True)
    www_transformers_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy theme files
    source_themes_dir = integration_dir / "themes"
    if source_themes_dir.exists():
        for theme_file in source_themes_dir.glob("*.yaml"):
            dest_file = themes_dir / theme_file.name
            _LOGGER.info(f"Installing theme file: {theme_file.name}")
            shutil.copy2(theme_file, dest_file)
    
    # Copy www files (fonts and cards)
    source_www_dir = integration_dir / "www"
    if source_www_dir.exists():
        # Copy all files from www/transformers to config/www/transformers
        source_transformers = source_www_dir / "transformers"
        if source_transformers.exists():
            _LOGGER.info("Installing fonts and cards to www/transformers")
            if www_transformers_dir.exists():
                shutil.rmtree(www_transformers_dir)
            shutil.copytree(source_transformers, www_transformers_dir)
    
    _LOGGER.info("Transformers Theme & Cards integration setup complete")
    _LOGGER.info("Themes installed to: %s", themes_dir)
    _LOGGER.info("Cards and fonts installed to: %s", www_transformers_dir)
    _LOGGER.info("Please reload themes and add cards resource: /local/transformers/transformers-cards.js")
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
