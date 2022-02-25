from pathlib import Path
import shutil

def main():
    build_system = "{{ cookiecutter.type }}".lower()
    trigger = "{{ cookiecutter.trigger }}".lower()
    shutil.copytree("sub-templates/common/", "./", dirs_exist_ok=True)
    shutil.copytree(f"sub-templates/{trigger}/{build_system}/", "./", dirs_exist_ok=True)
    shutil.copytree(f"sub-templates/{trigger}/code/", "./", dirs_exist_ok=True)
    shutil.rmtree(f"sub-templates")


if __name__ == "__main__":
    main()
