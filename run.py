#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hellowork 启动脚本
简化的应用启动入口
"""

from app import app
import os

if __name__ == '__main__':
    print("🔥 启动 Hellowork 应用...")
    print("📡 应用将在以下地址启动:")
    
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"   - 本地访问: http://127.0.0.1:{port}")
    print(f"   - 网络访问: http://{host}:{port}")
    print("📋 可用接口:")
    print(f"   - 健康检查: http://127.0.0.1:{port}/health")
    print(f"   - 应用信息: http://127.0.0.1:{port}/api/info")
    print("🛑 按 Ctrl+C 停止应用")
    print("-" * 50)
    
    try:
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n👋 Hellowork 应用已停止")
