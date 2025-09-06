
'''
pip is preferred for pure Python packages and projects that primarily rely on the Python ecosystem. Conda, on the other hand, is advantageous when dealing with multi-language projects or packages with complex dependencies that extend beyond Python.


Important Conda commands

conda create: Creates a new Conda environment.
conda activate: Activates a specific Conda environment.
conda deactivate: Deactivates the currently active environment.
conda install: Installs packages into the active environment.
conda list: Lists all packages installed in the active environment.
conda search: Searches for available packages in the Conda repositories.
conda search <keyword>: Searches the Conda repositories for packages related to the given keyword.
conda update: Updates a package to its latest version.
conda remove: Uninstalls a package from the active environment.
conda env list: Lists all Conda environments on your system.

Managing packages with Conda

conda install <package-name>: Installs the specified package into your active Conda environment.
conda list <package-name>: Displays information about the specified package, including its version.
conda update <package-name>: Upgrades the specified package to its latest available version.
conda install <package-name>=<version>: Installs a specific version of the specified package.
conda remove <package-name>: Uninstalls the specified package from your active environment


Essential pip commands

pip list: Quickly view all installed packages and their versions.
pip show <package>: Get detailed information about a specific package, including its dependencies and location.
pip freeze: Generate a list of your installed packages suitable for a requirements.txt file, perfect for sharing your project's dependencies.
pip check: Verify your environment for any dependency conflicts, helping prevent unexpected errors.
'''
