![Sms77.io Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "Sms77.io Logo")

# Official Home Assistant SMS Component

## Installation

Add to `configuration.yaml` usually in `~/.homeassistant/`:

```yaml
sms77_sms:

notify:
  - platform: sms77_sms
    sender: HomeAssist # defaults to hass
    name: sms77_sms
    api_key: INSERT_YOUR_API_KEY_HERE!
    recipient: 01716992343 # or specify multiple numbers eg. [01771783130, 01716992343]
```

### Example

[Configure service call on automation](./screenshots/automation_action_call_service.png)

#### Support

Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](./LICENSE)