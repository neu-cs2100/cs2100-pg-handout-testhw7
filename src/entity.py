"""Module defining the base Entity class for all objects in the game."""

from abc import ABC, abstractmethod
from typing import Any, Optional
import pygame

from src.position import Position


class Entity(ABC):
    """
    An animate or inanimate object in the game.

    Args:
        type_name: The type/name of the entity
        image_file_name: The filename of the image to load
    """

    def __init__(self, type_name: str, image_file_name: str) -> None:
        self.type: str = type_name
        self.image: Any = self._load_image(f"data/images/{image_file_name}")

    def _load_image(self, path: str) -> Any:
        """
        Load an image from the given path.
        """
        try:
            return pygame.image.load(path)
        except Exception as e:
            raise FileNotFoundError(f"Could not load image: {path}") from e

    @abstractmethod
    def tick(self) -> None:
        """Takes an action during its turn."""
        pass

    def exit(self) -> None:
        """
        Removes this entity from the game. It will no longer appear
        on the screen, and its tick method will no longer be called.
        """
        from src.game import Game  # Import here to avoid circular imports

        if Game.GAME:
            Game.GAME.remove(self)

    def __str__(self) -> str:
        """String representation of the entity."""
        return self.type

    def select_adjacent_empty_cell(self) -> Optional[Position]:
        """
        Returns the position of an empty cell adjacent to this entity or
        None if no adjacent empty cell exists or if this entity is not on
        the board.
        """
        from src.game import Game

        if Game.GAME is None:
            return None

        position = Game.GAME.get_position(self)
        # TODO: Implement logic to find adjacent empty cell
        return None
