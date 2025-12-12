#!/usr/bin/env python3
"""
Policy Pulse Core - Environment Setup Script

This script automates the setup of the Python environment for Policy Pulse Core.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def setup_virtual_environment():
    """Set up Python virtual environment."""
    print("Setting up Python virtual environment...")

    try:
        # Create virtual environment
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✓ Virtual environment created successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to create virtual environment: {e}")
        return False


def install_dependencies():
    """Install project dependencies."""
    print("Installing dependencies...")

    try:
        # Activate virtual environment and install dependencies
        if os.name == 'nt':  # Windows
            pip_path = os.path.join("venv", "Scripts", "pip")
        else:  # Unix-like systems
            pip_path = os.path.join("venv", "bin", "pip")

        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install dependencies: {e}")
        return False


def verify_setup():
    """Verify that the setup was successful."""
    print("Verifying setup...")

    try:
        # Try importing core modules
        import policy_pulse_core
        print("✓ Core modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import core modules: {e}")
        return False


def main():
    """Main setup function."""
    parser = argparse.ArgumentParser(description="Setup Policy Pulse Core environment")
    parser.add_argument("--skip-venv", action="store_true", help="Skip virtual environment creation")
    parser.add_argument("--skip-deps", action="store_true", help="Skip dependency installation")

    args = parser.parse_args()

    print("Policy Pulse Core Environment Setup")
    print("=" * 40)

    # Setup steps
    success = True

    if not args.skip_venv:
        if not setup_virtual_environment():
            success = False

    if not args.skip_deps and success:
        if not install_dependencies():
            success = False

    if success:
        print("\n✓ Setup completed successfully!")
        print("\nTo activate the environment:")
        if os.name == 'nt':  # Windows
            print("  venv\\Scripts\\activate")
        else:  # Unix-like systems
            print("  source venv/bin/activate")
        print("\nTo verify installation:")
        print("  python -c \"import policy_pulse_core; print('Success!')\"")
    else:
        print("\n✗ Setup failed. Please check the error messages above.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())