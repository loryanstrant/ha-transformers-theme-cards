"""
The Transformers Theme & Cards integration for Home Assistant.

This integration provides:
- Four Transformers-themed UI themes (Dark, Light, Silver, Dirty Metal)
- Eleven custom Lovelace cards with Transformers styling
- Authentic Transformers Movie font integration
- Automatic installation of all dependencies
- Automatic Lovelace resource registration

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
from homeassistant.components.lovelace import dashboard
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "transformers_theme_cards"

__version__ = "1.0.0"

CARDS_URL = "/local/transformers/transformers-cards.js"

# Define CONFIG_SCHEMA - this integration requires no configuration
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


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
    
    # Run file operations in executor to avoid blocking
    def install_files():
        """Install theme and www files."""
        try:
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
                # Note: This replaces the entire directory to ensure clean installation
                # If you have custom files, store them elsewhere
                source_transformers = source_www_dir / "transformers"
                if source_transformers.exists():
                    _LOGGER.info("Installing fonts and cards to www/transformers")
                    if www_transformers_dir.exists():
                        _LOGGER.debug("Removing existing www/transformers directory")
                        shutil.rmtree(www_transformers_dir)
                    shutil.copytree(source_transformers, www_transformers_dir)
        except PermissionError as err:
            _LOGGER.error(
                "Permission denied while installing files. Please check directory permissions: %s",
                err
            )
            return False
        except OSError as err:
            _LOGGER.error(
                "Failed to install files. Check disk space and permissions: %s",
                err
            )
            return False
        except Exception as err:
            _LOGGER.error(
                "Unexpected error during file installation: %s",
                err
            )
            return False
        
        return True
    
    # Run in executor to avoid blocking
    result = await hass.async_add_executor_job(install_files)
    
    if not result:
        _LOGGER.error("Transformers Theme & Cards integration setup failed")
        return False
    
    _LOGGER.info("Transformers Theme & Cards integration setup complete")
    _LOGGER.info("Themes installed to: %s", themes_dir)
    _LOGGER.info("Cards and fonts installed to: %s", www_transformers_dir)
    
    # Register the Lovelace resource
    _LOGGER.info("Registering Lovelace resource: %s", CARDS_URL)
    
    # Register static path for the cards
    hass.http.register_static_path(
        CARDS_URL,
        str(www_transformers_dir / "transformers-cards.js"),
        cache_headers=True
    )
    
    # Add the resource to Lovelace resources
    try:
        # Use the lovelace component to add extra JS URL
        if "lovelace" not in hass.data:
            hass.data["lovelace"] = {"resources": []}
        
        # Add our resource to the lovelace resources
        hass.components.frontend.add_extra_js_url(hass, CARDS_URL)
        
        _LOGGER.info("Lovelace resource registered successfully")
        _LOGGER.info("Transformers cards are now automatically available in Lovelace")
        
    except Exception as err:
        _LOGGER.warning(
            "Could not automatically register Lovelace resource: %s. "
            "You may need to add it manually via Settings > Dashboards > Resources",
            err
        )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
