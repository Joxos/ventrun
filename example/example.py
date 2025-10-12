from moduvent import subscribe
from ventrun import Main


@subscribe(Main)
def main(e):
    print("Hello, world!")
