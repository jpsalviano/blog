from src.config import settings


def test_settings():
    assert settings.app_name == "Salviano.dev API"
