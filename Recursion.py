import os
from typing import List

def list_directory(path: str) -> List[str]:
    """
    Recursively lists all files and directories in the given directory.

    Args:
        path: The path of the directory to explore.

    Returns:
        A list of paths to files and directories within the given directory.
    """
    def explore(path: str) -> List[str]:
        # Base case: if path is a file, return it as a single-element list
        if os.path.isfile(path):
            return [path]
        
        # Recursive case: if path is a directory, get its contents and explore each
        try:
            entries = os.listdir(path)
        except PermissionError:
            return [f"PermissionError: {path}"]

        results = []
        for entry in entries:
            full_path = os.path.join(path, entry)
            results.extend(explore(full_path))
        
        return results
    
    # Start the recursive exploration
    return explore(path)

# Example usage
if __name__ == "__main__":
    directory_path = "."  # Change to the directory you want to explore
    files_and_directories = list_directory(directory_path)
    
    print(f"Files and directories in '{directory_path}':")
    for item in files_and_directories:
        print(item)
