![Sms77.io Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "Sms77.io Logo")

# Official Home Assistant SMS Component

## Installation

Clone the repository to a folder called "custom_components" in your Home
Assistant root directory, e.g. `git clone https://github.com/sms77io/home-assistant-sms ~/.homeassistant/custom_components/sms77_sms`

## Configuration

Add to `configuration.yaml` - usually in `~/.homeassistant/`:

```yaml
sms77_sms:

notify:
  - platform: sms77_sms
    sender: HomeAssist # defaults to hass
    name: sms77_sms
    api_key: INSERT_YOUR_SMS77_API_KEY_HERE
    recipient: 01716992343 # or specify multiple numbers eg. [01771783130, 01716992343]
```

Check out the [example](./screenshots/automation_action_call_service.png) on how to
configure a service call on automation.

## Support

Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)