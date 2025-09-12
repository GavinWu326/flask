import pytest
import json
from app import app

@pytest.fixture
def client():
    """创建测试客户端"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """测试主页"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'Halowork' in response.data.decode('utf-8')

def test_health_check(client):
    """测试健康检查接口"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert 'version' in data

def test_app_info(client):
    """测试应用信息接口"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['app_name'] == 'Halowork'
    assert data['version'] == '1.0.0'
    assert 'environment' in data
    assert 'python_version' in data

def test_about_page(client):
    """测试关于页面"""
    response = client.get('/about')
    assert response.status_code == 200
    assert '关于 Halowork' in response.data.decode('utf-8')

def test_404_page(client):
    """测试404页面"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
