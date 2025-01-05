from openai import OpenAI

client = OpenAI(api_key="0", base_url="http://0.0.0.0:8000/v1")
messages = [{"role": "user", "content": "Do you know anon?"}]
result = client.chat.completions.create(messages=messages, model="/mnt/sda/zzh/Qwen2.5-14B-Instruct")
print(result.choices[0].message)
