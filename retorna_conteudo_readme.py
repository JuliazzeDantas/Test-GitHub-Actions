import base64
import sys

def main(name, owner, project, area):
    content = f"#Repositório {name}\n##Owner: {owner}\n##Project: {project}\n##Área: {area}"
    return base64.b64encode(str(content).encode()).decode()



if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[3]))