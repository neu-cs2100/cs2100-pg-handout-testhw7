"""Defines the Status options for living entities."""

from enum import Enum


class Status(Enum):
    """
    The status of a living entity based on its health."""

    HEALTHY = "Healthy"
    INJURED = "Injured"
    DEAD = "Dead"
