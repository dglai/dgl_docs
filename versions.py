import json
import sys

def generate_branch_json(branches, output_file='branches.json'):
    # 构建 JSON 数据结构
    data = {
        "branches": [{"name": branch, "url": f"/dgl_docs/en/{branch}/"} for branch in branches]
    }
    
    # 将数据写入 JSON 文件
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"JSON file '{output_file}' has been generated successfully.")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python script.py branch1 branch2 ...")
        sys.exit(1)
    
    # 从命令行获取分支名称列表
    branch_names = sys.argv[1:]
    
    # 生成 JSON 文件
    generate_branch_json(branch_names)
