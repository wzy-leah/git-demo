import requests
import json
import time

API_KEY = "sk-mlwwrcybentdyfjuvcubhjweugcbjsskgvqrtuwpbnoecmqf"

url = "https://api.siliconflow.cn/v1/images/generations"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "Kwai-Kolors/Kolors",
    
    "prompt": "一只穿着汉服的猫，在故宫的红墙下，赛博朋克风格，霓虹灯",
    
    "image_size": "1024x1024",
    "batch_size": 1
}

print("正在使用 Kolors (可图) 生成中文提示词图片...")

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data['data'][0]['url']
        print(f"✅ 图片生成成功！")
        print(f"图片链接: {image_url}")
        
        img_data = requests.get(image_url).content
        file_name = f"chinese_result_{int(time.time())}.jpg"
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        print(f"✅ 图片已保存为: {file_name}")
    else:
        print("❌ 请求失败:", response.text)

except Exception as e:
    print(f"❌ 发生错误: {e}")