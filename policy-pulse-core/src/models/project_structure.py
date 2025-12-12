"""
Project Structure Model

Represents the overall organization of the Policy Pulse system with backend and frontend components.
"""

from typing import List, Optional
import uuid


class ProjectStructure:
    """Model representing a project component in the Policy Pulse architecture."""

    def __init__(self, name: str, project_type: str, path: str, description: str,
                 dependencies: Optional[List[str]] = None, version: Optional[str] = None):
        """
        Initialize a ProjectStructure instance.

        Args:
            name: Name of the project component
            project_type: Type of project ('backend', 'frontend', 'shared')
            path: Relative path to the component
            description: Description of the component's purpose
            dependencies: List of dependencies for the component
            version: Current version of the component
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = project_type
        self.path = path
        self.description = description
        self.dependencies = dependencies or []
        self.version = version

    def to_dict(self) -> dict:
        """Convert the ProjectStructure to a dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'path': self.path,
            'description': self.description,
            'dependencies': self.dependencies,
            'version': self.version
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'ProjectStructure':
        """Create a ProjectStructure instance from a dictionary."""
        return cls(
            name=data['name'],
            project_type=data['type'],
            path=data['path'],
            description=data['description'],
            dependencies=data.get('dependencies', []),
            version=data.get('version')
        )


class Component:
    """Model representing an individual component within a project."""

    def __init__(self, name: str, component_type: str, path: str, project_id: str,
                 description: str, size_lines: int, last_modified: str):
        """
        Initialize a Component instance.

        Args:
            name: Name of the component
            component_type: Type of component ('module', 'service', 'library', 'script', 'configuration')
            path: Relative path to the component
            project_id: Reference to the parent project
            description: Description of the component's purpose
            size_lines: Number of lines of code
            last_modified: When the component was last modified
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = component_type
        self.path = path
        self.project_id = project_id
        self.description = description
        self.size_lines = size_lines
        self.last_modified = last_modified

    def to_dict(self) -> dict:
        """Convert the Component to a dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'path': self.path,
            'project_id': self.project_id,
            'description': self.description,
            'size_lines': self.size_lines,
            'last_modified': self.last_modified
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Component':
        """Create a Component instance from a dictionary."""
        return cls(
            name=data['name'],
            component_type=data['type'],
            path=data['path'],
            project_id=data['project_id'],
            description=data['description'],
            size_lines=data['size_lines'],
            last_modified=data['last_modified']
        )