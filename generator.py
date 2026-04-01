#1APR2026
import random
import string

def generate_password(length):
    """生成指定长度的随机强密码"""
    # 准备密码的“原材料”
    letters = string.ascii_letters  # 包含所有大小写字母 (a-z, A-Z)
    numbers = string.digits         # 包含数字 (0-9)
    symbols = "!@#$%^&*"            # 包含常用特殊符号

    # 把所有原材料混合在一起
    all_characters = letters + numbers + symbols

    # 核心安全逻辑：从混合池中随机抽取指定数量的字符，拼成字符串
    password = "".join(random.choices(all_characters, k=length))
    return password

# --- 用户交互界面 ---
print("🔒 欢迎使用极简安全密码生成器 🔒")
print("-" * 35)

try:
    # 询问用户想要的密码长度
    user_length = int(input("请输入您需要的密码长度 (建议 12 位以上): "))
    
    # 基础的安全规则检查
    if user_length < 8:
        print("⚠️ 警告：密码短于 8 位非常容易被破解！已自动为您生成，但请谨慎使用。")
    
    # 调用函数生成密码
    final_password = generate_password(user_length)
    
    print("\n✅ 生成成功！")
    print(f"您的专属密码是: {final_password}")
    print("请妥善保管，不要保存在桌面文本文件里哦！")

except ValueError:
    # 防呆机制：如果用户输入的不是数字（比如输入了"abc"），系统不会崩溃，而是给出友好的提示
    print("\n❌ 错误：请输入有效的纯数字！")
