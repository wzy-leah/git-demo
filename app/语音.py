import asyncio
import edge_tts

async def generate_chinese_speech(text, output_file):
    # 声音列表：zh-CN-XiaoxiaoNeural (女), zh-CN-YunxiNeural (男) 等
    voice = "zh-CN-XiaoxiaoNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"✅ 生成完毕: {output_file}")

# 调用
if __name__ == "__main__":
    text = input()
    asyncio.run(generate_chinese_speech(text, "edge_output.wav"))