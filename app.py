from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """主页路由"""
    return render_template('index.html', 
                         title='Halowork项目', 
                         current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/health')
def health_check():
    """健康检查接口，用于CI/CD流程监控"""
    return jsonify({
        'status': 'healthy',
        'message': 'Halowork应用运行正常',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/info')
def app_info():
    """应用信息接口"""
    return jsonify({
        'app_name': 'Halowork',
        'version': '1.0.0',
        'environment': os.environ.get('FLASK_ENV', 'development'),
        'python_version': os.sys.version,
        'description': '这是一个用于测试CI/CD流程的Flask项目'
    })

@app.route('/about')
def about():
    """关于页面"""
    return render_template('about.html', title='关于Halowork')

if __name__ == '__main__':
    # 从环境变量获取配置，便于部署
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)
