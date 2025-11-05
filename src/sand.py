"""Class representing a block of sand"""

from src.block import Block


class Sand(Block):
    """A sand block."""

    def __init__(self) -> None:
        super().__init__(type_name="sand", image_file_name="Sand.png")
