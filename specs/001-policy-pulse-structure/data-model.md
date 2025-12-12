# Data Model: Policy Pulse Architecture

## Core Entities

### Project Structure
Represents the overall organization of the Policy Pulse system with backend and frontend components

**Fields**:
- `name` (string): Name of the project component
- `type` (enum): 'backend' | 'frontend' | 'shared'
- `path` (string): Relative path to the component
- `description` (text): Description of the component's purpose
- `dependencies` (json): List of dependencies for the component
- `version` (string): Current version of the component

**Validation**:
- Name must not be empty
- Type must be one of allowed values
- Path must be valid relative path
- Description must be provided

**Relationships**:
- One-to-many with Component (each project can have multiple components)

### Component
Represents individual modules or files within a project structure

**Fields**:
- `id` (UUID): Unique identifier for the component
- `name` (string): Name of the component
- `type` (enum): 'module' | 'service' | 'library' | 'script' | 'configuration'
- `path` (string): Relative path to the component
- `project_id` (string): Reference to the parent project
- `description` (text): Description of the component's purpose
- `size_lines` (integer): Number of lines of code
- `last_modified` (datetime): When the component was last modified

**Validation**:
- Name must not be empty
- Type must be one of allowed values
- Path must be valid relative path
- Project ID must reference an existing project
- Size lines must be positive integer

**Relationships**:
- Many-to-one with Project (components belong to a project)
- Zero-to-many with ComponentDependency (components can depend on others)

### ComponentDependency
Represents dependencies between components

**Fields**:
- `id` (UUID): Unique identifier for the dependency
- `source_component_id` (string): Component that depends on another
- `target_component_id` (string): Component that is depended upon
- `type` (enum): 'runtime' | 'build' | 'test'
- `version_constraint` (string): Version requirements (e.g., ">=1.0.0")

**Validation**:
- Source component ID must reference an existing component
- Target component ID must reference an existing component
- Type must be one of allowed values
- Version constraint must be valid semver format

**Relationships**:
- Many-to-one with Component (source dependency)
- Many-to-one with Component (target dependency)

## State Transitions

### Component States
- `active`: Component is currently in use
- `deprecated`: Component is deprecated but still functional
- `removed`: Component has been removed from the system

## Database Schema

```sql
CREATE TABLE projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('backend', 'frontend', 'shared')),
    path TEXT NOT NULL,
    description TEXT NOT NULL,
    dependencies JSON,
    version TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE components (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('module', 'service', 'library', 'script', 'configuration')),
    path TEXT NOT NULL,
    project_id TEXT NOT NULL,
    description TEXT NOT NULL,
    size_lines INTEGER NOT NULL,
    last_modified DATETIME NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE component_dependencies (
    id TEXT PRIMARY KEY,
    source_component_id TEXT NOT NULL,
    target_component_id TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('runtime', 'build', 'test')),
    version_constraint TEXT,
    FOREIGN KEY (source_component_id) REFERENCES components(id),
    FOREIGN KEY (target_component_id) REFERENCES components(id)
);

CREATE INDEX idx_components_project ON components(project_id);
CREATE INDEX idx_components_last_modified ON components(last_modified);
CREATE INDEX idx_dependencies_source ON component_dependencies(source_component_id);
CREATE INDEX idx_dependencies_target ON component_dependencies(target_component_id);
```

## API Data Contracts

### Project Structure Request
```json
{
  "name": "string",
  "type": "enum: backend|frontend|shared",
  "path": "string",
  "description": "string",
  "dependencies": ["string"],
  "version": "string"
}
```

### Component Request
```json
{
  "name": "string",
  "type": "enum: module|service|library|script|configuration",
  "path": "string",
  "project_id": "string",
  "description": "string",
  "size_lines": "integer",
  "last_modified": "ISO 8601 datetime"
}
```

### Component Dependency Request
```json
{
  "source_component_id": "string",
  "target_component_id": "string",
  "type": "enum: runtime|build|test",
  "version_constraint": "string"
}
```