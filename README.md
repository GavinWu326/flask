# 🔥 Halowork - CI/CD 测试项目

一个专为测试持续集成和持续部署(CI/CD)流程而设计的 Flask Web 应用程序。

## 📋 项目概述

Halowork 是一个简洁而功能完整的 Flask 应用，包含了验证 CI/CD 流程所需的所有基础组件：
- 健康检查接口
- 应用信息API
- 现代化Web界面
- 环境变量配置支持

## 🚀 快速开始

### 环境要求
- Python 3.7+
- pip

### 安装和运行

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd halowork
   ```

2. **创建虚拟环境** (推荐)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **运行应用**
   ```bash
   python app.py
   ```

应用将在 http://localhost:5000 启动

## 🔧 环境变量配置

支持以下环境变量进行配置：

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `FLASK_HOST` | 0.0.0.0 | 应用监听地址 |
| `FLASK_PORT` | 5000 | 应用监听端口 |
| `FLASK_DEBUG` | False | 调试模式开关 |
| `FLASK_ENV` | development | 运行环境 |

## 📡 API 接口

### 健康检查
- **URL**: `/health`
- **方法**: GET
- **用途**: 用于负载均衡器和监控系统检查应用状态

### 应用信息
- **URL**: `/api/info`
- **方法**: GET
- **用途**: 获取应用版本、环境等信息

## 🐳 Docker 部署

创建 Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

构建和运行:
```bash
docker build -t halowork .
docker run -p 5000:5000 halowork
```

## 🔄 CI/CD 集成示例

### GitHub Actions

创建 `.github/workflows/deploy.yml`:
```yaml
name: Deploy Halowork

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Health check
      run: |
        python app.py &
        sleep 5
        curl http://localhost:5000/health
```

## 🧪 测试

项目包含基础的测试框架：

```bash
# 运行测试
pytest

# 生成测试覆盖率报告
pytest --cov=app
```

## 📂 项目结构

```
halowork/
├── app.py              # Flask 主应用文件
├── requirements.txt    # Python 依赖
├── README.md          # 项目说明
├── templates/         # HTML 模板
│   ├── base.html      # 基础模板
│   ├── index.html     # 首页
│   └── about.html     # 关于页面
└── .github/           # CI/CD 配置 (可选)
    └── workflows/
        └── deploy.yml
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

MIT License

---

⭐ 如果这个项目对您有帮助，请给个 Star！
