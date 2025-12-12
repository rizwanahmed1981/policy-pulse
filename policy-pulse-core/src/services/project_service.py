"""
Project Service

Service layer for managing project structure and components.
"""

from typing import List, Optional
from policy_pulse_core.src.models.project_structure import ProjectStructure, Component


class ProjectService:
    """Service for managing project structure and components."""

    def __init__(self):
        """Initialize the ProjectService."""
        self.projects = {}
        self.components = {}

    def create_project(self, project: ProjectStructure) -> ProjectStructure:
        """
        Create a new project.

        Args:
            project: ProjectStructure instance to create

        Returns:
            The created ProjectStructure instance
        """
        self.projects[project.id] = project
        return project

    def get_project(self, project_id: str) -> Optional[ProjectStructure]:
        """
        Get a project by ID.

        Args:
            project_id: ID of the project to retrieve

        Returns:
            ProjectStructure instance or None if not found
        """
        return self.projects.get(project_id)

    def list_projects(self) -> List[ProjectStructure]:
        """
        List all projects.

        Returns:
            List of all ProjectStructure instances
        """
        return list(self.projects.values())

    def update_project(self, project_id: str, project: ProjectStructure) -> bool:
        """
        Update an existing project.

        Args:
            project_id: ID of the project to update
            project: Updated ProjectStructure instance

        Returns:
            True if updated successfully, False otherwise
        """
        if project_id in self.projects:
            self.projects[project_id] = project
            return True
        return False

    def delete_project(self, project_id: str) -> bool:
        """
        Delete a project.

        Args:
            project_id: ID of the project to delete

        Returns:
            True if deleted successfully, False otherwise
        """
        if project_id in self.projects:
            del self.projects[project_id]
            # Also delete associated components
            self.components = {
                cid: comp for cid, comp in self.components.items()
                if comp.project_id != project_id
            }
            return True
        return False

    def create_component(self, component: Component) -> Component:
        """
        Create a new component.

        Args:
            component: Component instance to create

        Returns:
            The created Component instance
        """
        self.components[component.id] = component
        return component

    def get_component(self, component_id: str) -> Optional[Component]:
        """
        Get a component by ID.

        Args:
            component_id: ID of the component to retrieve

        Returns:
            Component instance or None if not found
        """
        return self.components.get(component_id)

    def list_components(self) -> List[Component]:
        """
        List all components.

        Returns:
            List of all Component instances
        """
        return list(self.components.values())

    def get_components_by_project(self, project_id: str) -> List[Component]:
        """
        Get all components belonging to a specific project.

        Args:
            project_id: ID of the project

        Returns:
            List of Component instances for the project
        """
        return [comp for comp in self.components.values() if comp.project_id == project_id]

    def update_component(self, component_id: str, component: Component) -> bool:
        """
        Update an existing component.

        Args:
            component_id: ID of the component to update
            component: Updated Component instance

        Returns:
            True if updated successfully, False otherwise
        """
        if component_id in self.components:
            self.components[component_id] = component
            return True
        return False

    def delete_component(self, component_id: str) -> bool:
        """
        Delete a component.

        Args:
            component_id: ID of the component to delete

        Returns:
            True if deleted successfully, False otherwise
        """
        if component_id in self.components:
            del self.components[component_id]
            return True
        return False