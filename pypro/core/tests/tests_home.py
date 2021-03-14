from django.test import Client


def test_status_code_ok(client: Client):
    response = client.get('/')
    assert response.status_code == 200


def test_if_template_is_used(client: Client):
    response = client.get('/')
    assert 'index.html' in (template.name for template in response.templates)
