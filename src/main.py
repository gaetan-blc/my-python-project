def get_git_version():
    import subprocess
    try:
        git_version = subprocess.check_output(['git', '--version']).decode('utf-8').strip()
        return git_version
    except Exception as e:
        return f"Error getting Git version: {e}"

def get_python_version():
    import sys
    return sys.version

if __name__ == "__main__":
    print("Git Version:", get_git_version())
    print("Python Version:", get_python_version())