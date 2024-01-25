import os

# -----------------------------------
# Set the root folder
# -----------------------------------
def set_root_dir():
    # Determines the root directory based on environment variables and creates necessary folders.
    try:
        if "C8_ENV" in os.environ and os.environ["C8_ENV"] == "Laptop":
            print("Laptop environment detected")
            return f"C:\\Programming\\Github\\correl8"  # laptop path
        else:
            print("Desktop environment detected")
            return f"D:\\Programming\\github\\correl8"  # desktop path
    except KeyError:
        raise ValueError("ENV environment variable not set")

# -----------------------------------
# -----------------------------------


# -----------------------------------
# Returns the path of the folder specified by folder_name
# -----------------------------------
def get_folder(folder_name):
    root_dir = ""
    root_dir = set_root_dir()  # Ensure root_dir is set

    # Returns the path of the folder specified by folder_name
    return os.path.join(root_dir, folder_name)

# -----------------------------------
# -----------------------------------

