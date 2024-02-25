import importlib.machinery
import importlib.util
import os


# The following code helps in importing the application-client/pagelibraries/resources/config.py
# file in current context.
_here = os.path.dirname(__file__)
loader = importlib.machinery.SourceFileLoader('config', _here[:_here.index("application-client")] + 'application-client/pagelibraries/resources/config.py')
spec = importlib.util.spec_from_loader('config', loader)
importedModule = importlib.util.module_from_spec(spec)
loader.exec_module(importedModule)


def get_path_input_json(test_name, use_local_data=False):
    """
    The function is used to get the path of local/remote input files.
    Args:
        test_name: Name of the test
        use_local_data: true if want to load local data, false for remote data.

    Returns: The path of input data file.
    """
    if use_local_data:
        return get_local_input_file_path(test_name)
    file_name = ""
    if test_name == "SignInTest":
        file_name = "SignInInputData.json"
    elif test_name == "AdminAdvertiser":
        file_name = "AdminAdvertiser.json"

    return f"{importedModule.CONFIG.aws_url}{file_name}"


def get_local_input_file_path(test_name):
    """
    This function returns the local data path of given test.
    Args:
        test_name: Name of the test.
    Returns: The local data path of given test.
    """
    if test_name == "SignInTest":
        return r"application-client/testdata/datafiles/SignInInputData.json"
    elif test_name == "AdminAdvertiser":
        return r"application-client/testdata/datafiles/AdminAdvertiser.json"


def get_local_files_path():
    """
    Returns: Returns the local file path that stores the following information, needed to load the helping files and libraries
    dependent_module,
    dependent_library,
    output_file_path,
    merged_result_file_path
    """
    return r"application-client/testdata/datafiles/LocalFilesPath.json"
