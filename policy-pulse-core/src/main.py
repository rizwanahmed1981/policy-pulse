#!/usr/bin/env python3
"""
Policy Pulse Core - Main Application Entry Point

This module provides the main Flask application for the Policy Pulse backend.
"""

import os
from flask import Flask, jsonify
from policy_pulse_core.src.services.project_service import ProjectService
from policy_pulse_core.src.lib.utils import setup_logging

# Set up logging
setup_logging(os.getenv('LOG_LEVEL', 'INFO'))

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Configure the application
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

    # Initialize services
    project_service = ProjectService()

    # Register routes
    @app.route('/')
    def home():
        """Home endpoint."""
        return jsonify({
            'message': 'Policy Pulse Core API',
            'version': '0.1.0',
            'status': 'healthy'
        })

    @app.route('/health')
    def health():
        """Health check endpoint."""
        return jsonify({
            'status': 'healthy',
            'service': 'policy-pulse-core'
        })

    # Project endpoints
    @app.route('/api/projects', methods=['GET'])
    def list_projects():
        """List all projects."""
        projects = project_service.list_projects()
        return jsonify({
            'projects': [project.to_dict() for project in projects]
        })

    @app.route('/api/projects/<project_id>', methods=['GET'])
    def get_project(project_id):
        """Get a specific project."""
        project = project_service.get_project(project_id)
        if project:
            return jsonify(project.to_dict())
        return jsonify({'error': 'Project not found'}), 404

    @app.route('/api/components', methods=['GET'])
    def list_components():
        """List all components."""
        components = project_service.list_components()
        return jsonify({
            'components': [component.to_dict() for component in components]
        })

    @app.route('/api/components/<component_id>', methods=['GET'])
    def get_component(component_id):
        """Get a specific component."""
        component = project_service.get_component(component_id)
        if component:
            return jsonify(component.to_dict())
        return jsonify({'error': 'Component not found'}), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=os.getenv('HOST', '127.0.0.1'),
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('DEBUG', 'False').lower() == 'true'
    )