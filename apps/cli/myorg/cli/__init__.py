from myorg.core import hello as hello_core
from myorg.utils import hello as hello_utils


def main() -> None:
    print(hello_core())
    print(hello_utils())
    print("Hello from myorg-cli!")
