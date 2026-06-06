import os
from pathlib import Path


def load_dotenv(path: str | None = None) -> None:
    candidates = [Path(path)] if path else [Path(__file__).parents[1] / ".env", Path(__file__).with_name(".env")]
    env_path = next((candidate for candidate in candidates if candidate and candidate.is_file()), None)
    if not env_path:
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load_dotenv()


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default)


APPIUM_SERVER = env("APPIUM_SERVER", "http://127.0.0.1:4723")
ANDROID_DEVICE = env("ANDROID_DEVICE", "127.0.0.1:5675")
ADB_PATH = env("ADB_PATH", "adb")
GMAIL_USERNAME_PREFIX = env("GMAIL_USERNAME_PREFIX", "")
PHONE_VERIFICATION_MODE = env("PHONE_VERIFICATION_MODE", "manual").lower()
ACCEPT_TERMS = env("ACCEPT_TERMS", "0").lower() in {"1", "true", "yes", "on"}

SMS_API_BASE = env("SMS_API_BASE", "http://www.firefox.fun/yhapi.ashx")
SMS_TOKEN = env("SMS_TOKEN", "")
SMS_PROJECT_ID_GMAIL = env("SMS_PROJECT_ID_GMAIL", "")
SMS_MAXPRICE_GMAIL = env("SMS_MAXPRICE_GMAIL", "20")
SMS_COUNTRY_BLACKLIST_GMAIL = [
    item.strip() for item in env("SMS_COUNTRY_BLACKLIST_GMAIL", "261,63").split(",") if item.strip()
]

HERO_SMS_API_BASE = env("HERO_SMS_API_BASE", "https://hero-sms.com/stubs/handler_api.php")
HERO_SMS_API_KEY = env("HERO_SMS_API_KEY", "")
HERO_SMS_SERVICE_GMAIL = env("HERO_SMS_SERVICE_GMAIL", "")
