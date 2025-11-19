# This line makes 'func_from_module1' directly accessible when importing 'my_package'
from .module1 import func_from_module1

# This line makes 'func_from_module2' directly accessible when importing 'my_package'
from .module2 import func_from_module2

# You can also define package-level variables or functions here
PACKAGE_VERSION = "1.0.0"


def package_info():
    """Prints information about the package."""
    print(f"My Package Version: {PACKAGE_VERSION}")
    print("This is a sample Python package.")


# The __all__ variable defines what gets imported when using 'from my_package import *'
__all__ = ["func_from_module1", "func_from_module2",
           "package_info", "PACKAGE_VERSION"]
