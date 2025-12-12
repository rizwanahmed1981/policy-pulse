#!/usr/bin/env python3
"""
Policy Pulse Core - Main CLI Entry Point

This module provides the command-line interface for the Policy Pulse system.
"""

import argparse
import sys
from policy_pulse_core.src.services.project_service import ProjectService


def main():
    """Main entry point for the Policy Pulse CLI."""
    parser = argparse.ArgumentParser(
        description="Policy Pulse - Policy Management System",
        prog="policy-pulse"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # Project management commands
    project_parser = subparsers.add_parser(
        "project",
        help="Project management commands"
    )

    project_subparsers = project_parser.add_subparsers(
        dest="project_command",
        help="Project commands"
    )

    # Create project command
    create_project_parser = project_subparsers.add_parser(
        "create",
        help="Create a new project"
    )

    create_project_parser.add_argument(
        "name",
        help="Name of the project"
    )

    create_project_parser.add_argument(
        "--type",
        choices=["backend", "frontend", "shared"],
        default="shared",
        help="Type of project"
    )

    create_project_parser.add_argument(
        "--path",
        help="Path to the project"
    )

    create_project_parser.add_argument(
        "--description",
        help="Description of the project"
    )

    # List projects command
    project_subparsers.add_parser(
        "list",
        help="List all projects"
    )

    # Parse arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "project":
        if args.project_command == "create":
            # Create project logic would go here
            print(f"Creating project '{args.name}' of type '{args.type}'")
            return 0
        elif args.project_command == "list":
            # List projects logic would go here
            print("Listing projects...")
            return 0
        else:
            parser.print_help()
            return 1
    elif args.command is None:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())