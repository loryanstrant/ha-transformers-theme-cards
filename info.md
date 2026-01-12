# Transformers Theme & Cards

A complete Transformers-themed **custom integration** for Home Assistant combining beautiful themes and custom cards with authentic Transformers typography.

**This integration automatically installs all files** when you add it to your configuration.

## What's Included

### 🎨 Four Complete Themes
- **Transformers Dark** - Autobot blue with Decepticon red accents
- **Transformers Light** - Bright Cybertron aesthetic
- **Transformers Silver** - Retro G1 chrome styling
- **Transformers Dirty Metal** - Battle-worn modern look

### 🎴 11 Custom Cards
Status, Sensor, Button, Text, Gauge, Clock, Weather, Light, Alarm, Picture, and Glance cards with Transformers styling.

### 🔤 Authentic Font
Official Transformers Movie font automatically installed for both themes and cards.

## Installation Steps

1. **Install this integration via HACS** (you're doing it now!)
2. **Add to your `configuration.yaml`**:
   ```yaml
   transformers_theme_cards:
   
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. **Restart Home Assistant** (twice - once to load integration, once to apply themes)
4. **Install card-mod** (REQUIRED - search in HACS Frontend section)
5. **Apply a theme** from your profile or dashboard view settings
6. **Use the cards** - They're automatically registered, no manual resource addition needed!

## Quick Start

After installation, apply a theme:
- Go to your profile (click your username)
- Select theme: `transformers-dark`, `transformers-light`, `transformers-silver`, or `transformers-dirty-metal`

Then add a card to your dashboard:
```yaml
type: custom:transformers-status-card
title: SYSTEM STATUS
entities:
  - entity: binary_sensor.front_door
    name: MAIN ENTRANCE
message: ALL SYSTEMS OPERATIONAL
```

## Important Notes

⚠️ **card-mod is REQUIRED** for themes to work properly. Install it from HACS Frontend section.

✅ **Font is automatic** - No manual installation needed. The font is included and will load automatically.

✅ **Cards are automatic** - No need to manually add resources. Cards are automatically registered!

## Support

- [Full Documentation](https://github.com/loryanstrant/ha-transformers-theme-cards)
- [Report Issues](https://github.com/loryanstrant/ha-transformers-theme-cards/issues)

---

*"Freedom is the right of all sentient beings." - Optimus Prime*
