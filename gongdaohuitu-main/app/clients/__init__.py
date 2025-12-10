from dotenv import load_dotenv
import os

# ✅ 自动加载项目根目录下的 .env 文件
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=env_path)
