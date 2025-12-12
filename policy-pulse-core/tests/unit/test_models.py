"""
Unit tests for Policy Pulse Core models.
"""

import unittest
from policy_pulse_core.src.models.project_structure import ProjectStructure, Component


class TestProjectStructure(unittest.TestCase):
    """Test cases for ProjectStructure model."""

    def test_project_structure_creation(self):
        """Test creating a ProjectStructure instance."""
        project = ProjectStructure(
            name="test-project",
            project_type="backend",
            path="./test",
            description="A test project",
            dependencies=["pytest"],
            version="1.0.0"
        )

        self.assertEqual(project.name, "test-project")
        self.assertEqual(project.type, "backend")
        self.assertEqual(project.path, "./test")
        self.assertEqual(project.description, "A test project")
        self.assertEqual(project.dependencies, ["pytest"])
        self.assertEqual(project.version, "1.0.0")
        self.assertIsNotNone(project.id)

    def test_project_structure_to_dict(self):
        """Test converting ProjectStructure to dictionary."""
        project = ProjectStructure(
            name="test-project",
            project_type="backend",
            path="./test",
            description="A test project"
        )

        data = project.to_dict()
        self.assertEqual(data['name'], "test-project")
        self.assertEqual(data['type'], "backend")
        self.assertEqual(data['path'], "./test")
        self.assertEqual(data['description'], "A test project")


class TestComponent(unittest.TestCase):
    """Test cases for Component model."""

    def test_component_creation(self):
        """Test creating a Component instance."""
        component = Component(
            name="test-component",
            component_type="service",
            path="./test/component.py",
            project_id="test-project-id",
            description="A test component",
            size_lines=42,
            last_modified="2023-01-01T00:00:00Z"
        )

        self.assertEqual(component.name, "test-component")
        self.assertEqual(component.type, "service")
        self.assertEqual(component.path, "./test/component.py")
        self.assertEqual(component.project_id, "test-project-id")
        self.assertEqual(component.description, "A test component")
        self.assertEqual(component.size_lines, 42)
        self.assertEqual(component.last_modified, "2023-01-01T00:00:00Z")
        self.assertIsNotNone(component.id)

    def test_component_to_dict(self):
        """Test converting Component to dictionary."""
        component = Component(
            name="test-component",
            component_type="service",
            path="./test/component.py",
            project_id="test-project-id",
            description="A test component",
            size_lines=42,
            last_modified="2023-01-01T00:00:00Z"
        )

        data = component.to_dict()
        self.assertEqual(data['name'], "test-component")
        self.assertEqual(data['type'], "service")
        self.assertEqual(data['path'], "./test/component.py")
        self.assertEqual(data['project_id'], "test-project-id")
        self.assertEqual(data['description'], "A test component")
        self.assertEqual(data['size_lines'], 42)
        self.assertEqual(data['last_modified'], "2023-01-01T00:00:00Z")


if __name__ == '__main__':
    unittest.main()