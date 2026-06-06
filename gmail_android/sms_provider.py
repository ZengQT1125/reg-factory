"""
Environment-driven SMS provider placeholder.

This mirrors the provider shape used by reg-factory/common/sms.py so the project
can be merged later without hardcoding secrets. It is intentionally not wired
into Gmail phone verification by default.
"""

from dataclasses import dataclass

import requests

from config import (
    HERO_SMS_API_BASE,
    HERO_SMS_API_KEY,
    HERO_SMS_SERVICE_GMAIL,
    SMS_API_BASE,
    SMS_PROJECT_ID_GMAIL,
    SMS_TOKEN,
)


@dataclass
class SmsNumber:
    phone: str
    country_code: str
    activation_id: str
    provider: str


class SmsProviderError(RuntimeError):
    pass


def configured() -> bool:
    return bool((SMS_TOKEN and SMS_PROJECT_ID_GMAIL) or (HERO_SMS_API_KEY and HERO_SMS_SERVICE_GMAIL))


def require_configured() -> None:
    if not configured():
        raise SmsProviderError("SMS provider is not configured. Fill .env first.")


def request_number() -> SmsNumber:
    require_configured()
    if SMS_TOKEN and SMS_PROJECT_ID_GMAIL:
        return _request_firefox_number()
    return _request_hero_number()


def _request_firefox_number() -> SmsNumber:
    response = requests.get(
        SMS_API_BASE,
        params={
            "act": "getPhone",
            "token": SMS_TOKEN,
            "iid": SMS_PROJECT_ID_GMAIL,
            "did": "",
            "country": "",
            "dock": "",
            "otpmode": "",
            "maxPrice": "20",
            "mobile": "",
            "pushUrl": "",
        },
        timeout=30,
    )
    parts = response.text.strip().split("|")
    if parts[0] == "1" and len(parts) >= 8:
        return SmsNumber(phone=parts[7], country_code=parts[4], activation_id=parts[1], provider="firefox")
    raise SmsProviderError(f"firefox SMS provider returned: {response.text.strip()}")


def _request_hero_number() -> SmsNumber:
    response = requests.get(
        HERO_SMS_API_BASE,
        params={"api_key": HERO_SMS_API_KEY, "action": "getNumber", "service": HERO_SMS_SERVICE_GMAIL},
        timeout=30,
    )
    text = response.text.strip()
    if text.startswith("ACCESS_NUMBER:"):
        _, activation_id, full_phone = text.split(":")[:3]
        return SmsNumber(phone=full_phone, country_code="", activation_id=f"hero_{activation_id}", provider="hero")
    raise SmsProviderError(f"hero SMS provider returned: {text}")
