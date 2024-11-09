from datetime import datetime
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import create_app



@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })

    # アプリケーションコンテキストを使用してテスト用DBを作成
    with app.app_context():
        yield app  # テストの実行

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
