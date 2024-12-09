# Utilities folder - `utilities`

**Purpose:**  
Contains generic utility scripts and constants that support the main codebase. These utilities make the code cleaner, DRY (Don’t Repeat Yourself), and easier to maintain.

**Key Files:**

- `constants.py`:  
  Stores global constants (e.g., directory paths, default model names, common prompt templates) to avoid hardcoding them throughout the code.

- `helper.py`:  
  Provides utility functions such as file I/O helpers, data parsing routines, or formatting helpers.

- `classify.py`:  
  May contain a standalone script or function that integrates classification logic, possibly a CLI entry point to run classification tasks outside the notebooks.

- `__init__.py`:  
  Makes `utilities` a Python package, facilitating imports.

**How to Use:**


**Notes:**
- Keep utility scripts focused and generic.
- Regularly review and update constants to reflect the current project structure.