import json
import sys

def generate_branch_json(branches, output_file='branches.json'):
    # create json file.
    data = {
        "branches": [{"name": branch, "url": f"/dgl_docs/en/{branch}/"} for branch in branches]
    }
    data["branches"].append({"name": "latest", "url": "/dgl_docs/"})
    # write data to json file.
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"JSON file '{output_file}' has been generated successfully.")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python script.py branch1 branch2 ...")
        sys.exit(1)
    
    # get branch names.
    branch_names = sys.argv[1:]
    
    # generate json file.
    generate_branch_json(branch_names)
