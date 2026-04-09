# flask

<div align="center">

轻量级 Flask 示例项目，内置页面路由、健康检查、应用信息接口、测试用例和 Docker 部署配置，适合用于 CI/CD 流程演示。

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.3-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Pytest-Tested-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
</p>

</div>

## 项目概览

这个仓库实际运行的是一个名为 `Hellowork` 的 Flask Web 应用。它保留了最常见的后端基础能力：模板页面、JSON API、健康检查、环境变量配置、自动化测试和容器化部署，因此非常适合作为以下场景的起点：

- Flask 入门项目
- GitHub Actions / CI/CD 流程验证
- 容器化部署演示
- Web 服务健康检查与监控示例

## 功能一览

| 功能 | 说明 |
| --- | --- |
| 首页 | `GET /`，渲染模板页面并展示当前时间 |
| 关于页 | `GET /about`，展示项目介绍页面 |
| 健康检查 | `GET /health`，便于监控和部署探活 |
| 应用信息 | `GET /api/info`，返回版本、环境、Python 信息 |
| 自动化测试 | `pytest` 覆盖核心页面和 API |
| Docker 化 | 提供生产向 Gunicorn 启动方式 |

## 项目结构

```text
flask
├── app.py
├── run.py
├── test_app.py
├── requirements.txt
├── Dockerfile
└── templates
    ├── base.html
    ├── index.html
    └── about.html
```

## 快速开始

### 1. 安装依赖

```bash
git clone https://github.com/GavinWu326/flask.git
cd flask
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows 可使用：

```bash
venv\Scripts\activate
```

### 2. 启动应用

```bash
python app.py
```

默认访问地址：

- `http://localhost:5000/`
- `http://localhost:5000/health`
- `http://localhost:5000/api/info`

## 环境变量

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `FLASK_HOST` | `0.0.0.0` | 服务监听地址 |
| `FLASK_PORT` | `5000` | 服务端口 |
| `FLASK_DEBUG` | `False` | 是否开启调试模式 |
| `FLASK_ENV` | `development` | 运行环境标识 |

示例：

```bash
export FLASK_ENV=production
export FLASK_PORT=5000
python app.py
```

## API 示例

### 健康检查

```http
GET /health
```

返回示例：

```json
{
  "status": "healthy",
  "message": "Hellowork应用运行正常",
  "timestamp": "2026-04-09T12:00:00",
  "version": "1.0.0"
}
```

### 应用信息

```http
GET /api/info
```

返回示例：

```json
{
  "app_name": "Hellowork",
  "version": "1.0.0",
  "environment": "development",
  "python_version": "3.x",
  "description": "这是一个用于测试CI/CD流程的Flask项目"
}
```

## 测试

项目自带基础测试，可以直接运行：

```bash
pytest
```

测试覆盖了：

- 首页与关于页是否可访问
- 健康检查接口返回结构
- 应用信息接口字段
- 不存在页面的 404 行为

## Docker 部署

### 构建镜像

```bash
docker build -t hellowork-flask .
```

### 运行容器

```bash
docker run -p 5000:5000 hellowork-flask
```

容器内会使用 Gunicorn 启动应用，并自带 `/health` 探活检查。

## 适用场景

- 用作最小可运行 Flask 模板
- 测试 CI/CD 构建、部署与探活流程
- 演示 Gunicorn + Docker 的基础部署方式

## License

MIT
