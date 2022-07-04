![sms77.io Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "sms77.io Logo")

# Deprecated - please use [https://github.com/seven-io/home-assistant](https://github.com/seven-io/home-assistant).

## Official Home Assistant SMS Component

This integration adds the possibility of sending SMS via sms77.

## Installation

### Manually

Clone the repository to a folder called "custom_components" in your Home
Assistant root directory, e.g. `git clone https://github.com/seven-io/home-assistant-sms ~/.homeassistant/custom_components/sms77_sms`

### Via [HACS](https://hacs.xyz/)
- Navigate to HACS -> Integrations -> Custom repositories -> Add
- Set *Repository* to **https://github.com/seven-io/home-assistant-sms**
- Set *Type* to **Integration**
- Confirm form submission and the repository should be appended to the list

## Configuration

Add to `configuration.yaml` - usually in `~/.homeassistant/`:

```yaml
sms77_sms:

notify:
  - platform: sms77_sms
    sender: HomeAssist # defaults to hass - see https://help.sms77.io/en/set-sender-id
    name: sms77_sms
    api_key: INSERT_YOUR_SMS77_API_KEY_HERE # see https://help.sms77.io/en/api-key-access
    recipient: 01716992343 # or specify multiple numbers eg. [01771783130, 01716992343]
```

Check out the [example](./screenshots/automation_action_call_service.png) on how to
configure a service call on automation.

## Support

Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)
