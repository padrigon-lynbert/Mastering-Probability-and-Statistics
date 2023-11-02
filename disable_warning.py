import warnings

def disable_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
