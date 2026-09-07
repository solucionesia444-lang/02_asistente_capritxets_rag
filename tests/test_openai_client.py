import importlib
import sys

import dotenv
import pytest


def test_openai_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(dotenv, "load_dotenv", lambda: False)

    sys.modules.pop("app.core.openai_client", None)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        importlib.import_module("app.core.openai_client")