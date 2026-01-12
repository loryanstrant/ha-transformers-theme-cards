# Transformers Theme & Cards for Home Assistant

[![License](https://img.shields.io/badge/License-MIT-e31e24?style=for-the-badge)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Compatible-41BDF5?style=for-the-badge&logo=home-assistant)](https://www.home-assistant.io/)
[![HACS](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)

A complete Transformers-themed integration for Home Assistant that combines beautiful themes and custom cards with authentic Transformers typography. Transform your Home Assistant interface with the iconic aesthetic of the Transformers franchise!

**This is a custom integration** that automatically installs themes, cards, and fonts when you add it to your Home Assistant configuration.

## ✨ Features

- **🎨 Four Complete Themes**: Dark, Light, Silver (Retro), and Dirty Metal (Modern) variants
- **🎴 11 Custom Cards**: Status, Sensor, Button, Text, Gauge, Clock, Weather, Light, Alarm, Picture, and Glance cards
- **🔤 Authentic Typography**: Official Transformers Movie font included and properly integrated
- **🚀 Single Installation**: Everything you need in one HACS integration
- **📦 All Dependencies Managed**: Theme files, cards, and fonts automatically installed

## 📸 Screenshots

### Themes
- **Transformers Dark**: Autobot-inspired blue accents with Decepticon red highlights
- **Transformers Light**: Bright, clean theme inspired by gleaming Cybertron metal
- **Transformers Silver**: Retro chrome aesthetic from classic G1 Transformers
- **Transformers Dirty Metal**: Battle-worn modern aesthetic from recent films

### Cards
All cards feature angular, tech-inspired designs with authentic Transformers styling and the iconic Transformers Movie font.

## 📋 Requirements

### Essential
- **Home Assistant**: 2024.1.0 or newer
- **[card-mod](https://github.com/thomasloven/lovelace-card-mod)**: **REQUIRED** for theme functionality

### Recommended Installation Method
- **[HACS](https://hacs.xyz/)**: Home Assistant Community Store

## 🔧 Installation

### Method 1: HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to the **Integrations** section
3. Click the **"+"** button in the bottom right
4. Search for **"Transformers Theme & Cards"**
5. Click **"Download"**
6. **Restart Home Assistant**
7. Add the integration to `configuration.yaml`:

```yaml
# Add to configuration.yaml
transformers_theme_cards:

# Also ensure themes are enabled
frontend:
  themes: !include_dir_merge_named themes
```

8. **Restart Home Assistant again**

The integration will automatically:
- Install all 4 theme files to `config/themes/`
- Install cards JavaScript to `config/www/transformers/`
- Install fonts to `config/www/transformers/fonts/`

**Why two restarts?**
- First restart: Loads the integration and installs files
- Second restart: Home Assistant reads the newly installed theme files

This is a one-time setup requirement. After the initial installation, no further restarts are needed for theme changes.

### Method 2: Manual Installation

1. Download this repository
2. Copy the `custom_components/transformers_theme_cards` folder to your Home Assistant `config/custom_components/` directory
3. Add to your `configuration.yaml`:

```yaml
transformers_theme_cards:

frontend:
  themes: !include_dir_merge_named themes
```

4. Restart Home Assistant twice (first to load integration, second to apply themes)

## 🎨 Using the Themes

### Installing card-mod (Required)

The themes require card-mod to function properly. Install it via HACS:

1. Open HACS → Frontend
2. Search for "card-mod"
3. Click "Install"
4. Restart Home Assistant

### Applying a Theme

**Option 1: Set for Your Profile**
1. Click on your username in the sidebar
2. Under "Theme", select one of:
   - `transformers-dark`
   - `transformers-light`
   - `transformers-silver`
   - `transformers-dirty-metal`

**Option 2: Apply to a Specific View**
1. Edit your dashboard
2. Click on a view (tab)
3. Click "Edit View"
4. Under "Theme", select your preferred variant
5. Save

**Option 3: Set as System Default**

Add to `configuration.yaml`:
```yaml
frontend:
  themes: !include_dir_merge_named themes
  default_theme: transformers-dark
```

## 🎴 Using the Cards

### Adding Cards as a Resource

The cards JavaScript is automatically available after installation. Add it as a resource:

1. Go to **Settings** → **Dashboards**
2. Click the **⋮** menu in the top right
3. Select **Resources**
4. Click **"+ Add Resource"**
5. Enter URL: `/local/transformers/transformers-cards.js`
6. Select Resource Type: **JavaScript Module**
7. Click **"Create"**

### Card Examples

#### Status Card
```yaml
type: custom:transformers-status-card
title: SYSTEM STATUS
entities:
  - entity: binary_sensor.front_door
    name: MAIN ENTRANCE
  - entity: sensor.temperature_living_room
    name: AMBIENT TEMP
message: ALL SYSTEMS OPERATIONAL
theme: autobot
```

#### Sensor Card
```yaml
type: custom:transformers-sensor-card
entity: sensor.cpu_temperature
name: CORE TEMPERATURE
unit: "°C"
show_graph: true
max: 100
```

#### Button Card
```yaml
type: custom:transformers-button-card
title: CONTROL PANEL
columns: 2
buttons:
  - entity: light.living_room
    name: ILLUMINATION
    icon: 💡
    action: toggle
  - entity: switch.coffee_maker
    name: BEVERAGE SYS
    action: toggle
```

#### Text Card
```yaml
type: custom:transformers-text-card
title: SYSTEM NOTICE
content: |
  ATTENTION: ALL AUTOBOTS
  
  MISSION BRIEFING AT 0800 HOURS
  REPORT TO COMMAND CENTER
```

For complete card documentation and all 11 card types, see the [Cards Documentation](docs/CARDS.md) (coming soon).

## 📁 Repository Structure

```
ha-transformers-theme-cards/
├── custom_components/
│   └── transformers_theme_cards/
│       ├── __init__.py                    # Integration setup logic
│       ├── manifest.json                  # Integration metadata
│       ├── services.yaml                  # Services definition
│       ├── themes/
│       │   └── transformers-themes.yaml   # All 4 theme variants
│       └── www/
│           └── transformers/
│               ├── fonts/
│               │   ├── TransformersMovie-y9Ad.ttf
│               │   └── transformers-fonts.css
│               └── transformers-cards.js  # All 11 cards bundled
├── hacs.json                               # HACS metadata
├── info.md                                 # HACS store display
├── README.md                               # This file
└── LICENSE
```

## 🔤 Font Integration

The **Transformers Movie font** is the cornerstone of this integration's authentic look.

### How It Works
- **Themes**: Load the font via card-mod from `/local/transformers/fonts/`
- **Cards**: Font is bundled with the cards JavaScript
- **Automatic**: No manual font installation needed!

### Font Location
The font is installed at: `/config/www/transformers/fonts/TransformersMovie-y9Ad.ttf`

This ensures both themes and cards have access to the same font file.

## 🎯 Theme Details

### Transformers Dark
- **Primary Color**: Deep Blue (#0d47a1) - Autobot blue
- **Accent Color**: Vibrant Red (#ff1744) - Decepticon red
- **Background**: Dark Metallic (#0a0e14)
- **Best For**: Nighttime viewing, OLED displays

### Transformers Light
- **Primary Color**: Bright Blue (#1976d2)
- **Accent Color**: Pink Energy (#ff4081)
- **Background**: Light Metallic (#f5f7fa)
- **Best For**: Daytime use, high ambient light

### Transformers Silver
- **Primary Color**: Chrome Silver (#c0c0c0)
- **Accent Color**: Classic Red (#e53935)
- **Background**: Dark Gunmetal (#1a1a1a)
- **Best For**: Retro G1 aesthetic, chrome effects

### Transformers Dirty Metal
- **Primary Color**: Gunmetal (#8b7355)
- **Accent Color**: Rust Orange (#d84315)
- **Background**: Weathered Black (#1c1814)
- **Best For**: Modern battle-worn aesthetic

## 🐛 Troubleshooting

### Themes Not Applied
1. Verify card-mod is installed
2. Restart Home Assistant after installation
3. Apply theme to view (not just profile)
4. Hard refresh browser (Ctrl+Shift+R / Cmd+Shift+R)

### Fonts Not Loading
1. Check that theme is applied to your view
2. Verify browser console (F12) for errors
3. Confirm `/local/transformers/fonts/` is accessible
4. Clear browser cache and reload

### Cards Not Working
1. Verify the resource is added correctly
2. Check resource path: `/local/transformers/transformers-cards.js`
3. Resource type must be "JavaScript Module"
4. Hard refresh browser

### Font Path Issues
The font is located at `/config/www/transformers/fonts/TransformersMovie-y9Ad.ttf` which maps to `/local/transformers/fonts/` in the browser. This path is used by both themes and cards.

## 🤝 Contributing

Contributions are welcome! This integration combines:
- Original cards from: [ha-transformers-cards](https://github.com/loryanstrant/ha-transformers-cards)
- Original theme from: [ha-transformers-theme](https://github.com/loryanstrant/ha-transformers-theme)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Font License
The Transformers Movie font is freeware for non-commercial use. Source: [FontSpace](https://www.fontspace.com/transformers-movie-font-f34560)

## 🙏 Acknowledgments

- Inspired by the Transformers franchise and Teletraan-I computer system
- Theme design influenced by Material Design principles
- Cards built with [Lit](https://lit.dev/) for optimal performance

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/loryanstrant/ha-transformers-theme-cards/issues)
- **Discussions**: [GitHub Discussions](https://github.com/loryanstrant/ha-transformers-theme-cards/discussions)

---

*"Freedom is the right of all sentient beings." - Optimus Prime*

**Transform your Home Assistant today!** 🤖⚡
