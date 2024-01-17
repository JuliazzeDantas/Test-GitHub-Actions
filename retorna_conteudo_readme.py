import base64
import sys

def main(name, owner, project, area):
    content = f"#Repositório {name}\n##Owner: {owner}\n##Project: {project}\n##Área: {area}"
    print(base64.b64encode(content.encode()).decode())
    return base64.b64encode(content.encode()).decode()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[3])