# Integration Setup Guide

## What This Integration Does

The Transformers Theme & Cards integration is a **custom Home Assistant integration** that automatically installs:

1. **Four Transformers themes** (Dark, Light, Silver, Dirty Metal)
2. **Eleven custom Lovelace cards** with Transformers styling
3. **Transformers Movie font** for authentic typography

## How It Works

When you add `transformers_theme_cards:` to your `configuration.yaml` and restart Home Assistant, the integration:

1. Copies all theme files from `custom_components/transformers_theme_cards/themes/` to `config/themes/`
2. Copies all www files (cards and fonts) from `custom_components/transformers_theme_cards/www/` to `config/www/transformers/`
3. Logs the installation paths for verification

## Installation via HACS

1. Install via HACS → Integrations
2. Add to `configuration.yaml`:
   ```yaml
   transformers_theme_cards:
   
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Restart Home Assistant **twice**:
   - First restart: Loads the integration and copies files
   - Second restart: Loads the themes into Home Assistant

## Post-Installation Steps

### 1. Install card-mod (Required)

The themes **require** card-mod to function properly:
1. HACS → Frontend
2. Search for "card-mod"
3. Install
4. Restart Home Assistant

### 2. Apply a Theme

**Option A: Profile-wide**
- Click your username → Theme → Select `transformers-dark` (or another variant)

**Option B: Per-view**
- Edit Dashboard → Edit View → Theme → Select variant

### 3. Add Cards Resource

To use the custom cards:
1. Settings → Dashboards → Resources (⋮ menu → Resources)
2. Add Resource:
   - URL: `/local/transformers/transformers-cards.js`
   - Resource Type: JavaScript Module
3. Click Create

## File Locations After Installation

After the integration runs, you'll find:

```
config/
├── themes/
│   └── transformers-themes.yaml          # Installed by integration
├── www/
│   └── transformers/                     # Installed by integration
│       ├── transformers-cards.js
│       └── fonts/
│           ├── TransformersMovie-y9Ad.ttf
│           └── transformers-fonts.css
└── custom_components/
    └── transformers_theme_cards/         # Installed by HACS
        ├── __init__.py
        ├── manifest.json
        ├── themes/                       # Source files
        └── www/                          # Source files
```

## Troubleshooting

### Themes Don't Appear

1. Verify `frontend:` configuration in `configuration.yaml`:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
2. Check logs for integration errors
3. Verify files exist in `config/themes/`
4. Restart Home Assistant twice

### Cards Don't Work

1. Verify resource is added correctly (URL and type)
2. Check browser console (F12) for errors
3. Verify file exists at `config/www/transformers/transformers-cards.js`
4. Hard refresh browser (Ctrl+Shift+R)

### Fonts Don't Load

1. Ensure theme is applied (not just selected)
2. Verify card-mod is installed
3. Check that font file exists at `config/www/transformers/fonts/TransformersMovie-y9Ad.ttf`
4. Clear browser cache

## Uninstalling

To remove the integration:

1. Remove `transformers_theme_cards:` from `configuration.yaml`
2. Remove the integration via HACS
3. Manually delete (if desired):
   - `config/themes/transformers-themes.yaml`
   - `config/www/transformers/` directory
4. Restart Home Assistant

## Development

This integration is built from:
- Cards: https://github.com/loryanstrant/ha-transformers-cards
- Theme: https://github.com/loryanstrant/ha-transformers-theme

Combined into a single custom integration for easy installation.
