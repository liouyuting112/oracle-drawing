import os
import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr)
        return False
    return True

def main():
    print("🚀 正在準備上傳至 GitHub...")
    
    # 1. 檢查是否已安裝 git
    if not run_command("git --version"):
        print("❌ 未偵測到 Git，請先安裝 Git: https://git-scm.com/")
        return

    # 2. 初始化 Git (如果尚未初始化)
    if not os.path.exists(".git"):
        print("📁 初始化 Git 儲存庫...")
        run_command("git init")
    
    # 3. 新增所有檔案
    print("➕ 新增檔案至暫存區...")
    run_command("git add .")
    
    # 4. 提交變更
    print("💾 提交變更...")
    run_command('git commit -m "Initial commit for Digital Oracle Master 2.0 (Commercial Ready)"')
    
    print("\n" + "="*50)
    print("✅ 本地端封裝與提交已完成！")
    print("👉 請執行以下步驟將其推送到您的 GitHub：")
    print("1. 在 GitHub 上建立一個新的儲存庫 (Repository)")
    print("2. 執行指令：git remote add origin <您的_GitHub_網址>")
    print("3. 執行指令：git branch -M main")
    print("4. 執行指令：git push -u origin main")
    print("="*50)

if __name__ == "__main__":
    main()
