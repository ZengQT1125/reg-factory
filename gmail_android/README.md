# Gmail Android Local Automation

This package drives the Gmail Android signup flow through Appium and a local Android emulator.

## Safety Boundary

The script stops at phone/SMS/CAPTCHA or additional Google security verification by default. Those steps must be completed by an operator. The `.env` file includes SMS provider placeholders for future compliant internal integrations, but the distributed script does not automate bypassing Google phone verification.

## Requirements

- Windows 10/11
- Python 3.11+
- Node.js 20+
- Android SDK Platform Tools (`adb`)
- BlueStacks or another Android emulator with ADB enabled
- Appium 2.x with `uiautomator2` driver
- Gmail installed in the emulator

Known local working versions:

- Python 3.12.4
- Node v20.20.2
- npm 10.8.2
- Appium 2.19.0
- UiAutomator2 driver 4.2.9

## Install

Run PowerShell from the project root:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install_all_windows.ps1
```

If your Android SDK is not in PATH, set `ADB_PATH` in `.env` or add `platform-tools` to PATH.

### BlueStacks Installer Bundle

The distributable may include a fixed BlueStacks installer under:

```text
offline\bluestacks\BlueStacksInstaller_*.exe
```

`scripts\install_all_windows.ps1` calls `scripts\install_bluestacks.ps1`, which installs or detects BlueStacks, enables ADB, configures a Pie 64-bit instance, sets the target display to `900x1600 @ 240 dpi`, and connects ADB on `127.0.0.1:5675`.

If the bundled installer is a small web/micro installer, the target machine still needs network access to download BlueStacks components. For fully offline installation, replace it with the approved full/offline BlueStacks installer before building the zip.

If the installer is not bundled, put the approved BlueStacks installer in `offline\bluestacks\` before running the script.

Direct BlueStacks-only install/config:

```powershell
.\scripts\install_bluestacks.ps1
```

## Emulator Setup

1. Run `.\scripts\install_all_windows.ps1`, or install BlueStacks manually.
2. Enable Android Debug Bridge in BlueStacks settings if the script did not do it.
3. Confirm the device:

```powershell
adb devices
```

Set `ANDROID_DEVICE` in `.env` if the device id is not `127.0.0.1:5675`.

## Start Appium

```powershell
.\scripts\start_appium.ps1
.\scripts\check_env.ps1
```

## Run

Default run stops at phone verification:

```powershell
python .\gmail_register_local.py
```

Wait while you manually complete phone verification, then continue:

```powershell
python .\gmail_register_local.py --wait-phone-verification
```

Resume after manual phone verification:

```powershell
python .\gmail_register_local.py --resume-after-phone
```

To let the script click the final Privacy and Terms and Google services confirmation after explicit operator consent:

```powershell
python .\gmail_register_local.py --resume-after-phone --accept-terms
```

## Environment

Copy `.env.example` to `.env`.

Important values:

- `APPIUM_SERVER`: default `http://127.0.0.1:4723`
- `ANDROID_DEVICE`: default `127.0.0.1:5675`
- `GMAIL_USERNAME_PREFIX`: optional username prefix
- `ACCEPT_TERMS`: `1` only after explicit consent

SMS provider placeholders are modeled after `reg-factory/common/sms.py`:

- `SMS_TOKEN`
- `SMS_PROJECT_ID_GMAIL`
- `HERO_SMS_API_KEY`
- `HERO_SMS_SERVICE_GMAIL`

They are reserved for future compliant integrations and are not enabled by default.

## Package Contents

- `gmail_register_local.py`: main Appium flow
- `appium_api.py`: local Appium helper API
- `config.py`: `.env` loader
- `.env.example`: configuration template
- `requirements.txt`: Python dependencies
- `scripts/`: install, check, start, run helpers
- `offline/bluestacks/`: optional fixed BlueStacks installer

Runtime logs, screenshots, XML dumps, `.env`, and `__pycache__` are excluded from the release zip.
