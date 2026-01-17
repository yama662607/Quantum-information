import subprocess
import shutil
import sys


def check_command(cmd, name):
    path = shutil.which(cmd)
    if path:
        try:
            version = (
                subprocess.check_output([cmd, "--version"], stderr=subprocess.STDOUT)
                .decode()
                .strip()
            )
            print(f"✅ {name:10} Found: {path}")
            print(f"   Version: {version.splitlines()[0]}")
            return True
        except Exception:
            print(f"⚠️ {name:10} Found at {path}, but failed to get version.")
            return True
    else:
        print(f"❌ {name:10} NOT FOUND. Please install it.")
        return False


def main():
    print("🔍 Checking development environment...\n")

    results = [
        check_command("uv", "uv"),
        check_command("just", "just"),
        check_command("quarto", "Quarto"),
        check_command("npm", "Node/npm"),
    ]

    print("\n--- Python Environment ---")
    print(f"Interpretor: {sys.executable}")

    if all(results):
        print("\n✨ All systems go! You are ready to develop.")
        sys.exit(0)
    else:
        print(
            "\n❗ Some dependencies are missing. Please refer to README.md for installation instructions."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
