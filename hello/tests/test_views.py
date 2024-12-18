import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_hello_world(client):
    # 使用 reverse 反轉 'hello_world' 路徑
    url = reverse("hello_world")
    response = client.get(url)

    # 檢查 HTTP 狀態碼
    assert response.status_code == 200

    # 檢查回應內容
    assert response.content.decode() == "Hello, World!"
