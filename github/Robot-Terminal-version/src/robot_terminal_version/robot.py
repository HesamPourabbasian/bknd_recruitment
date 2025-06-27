from abc import ABC, abstractmethod


class Robot(ABC):
    """Base class for all robot types, providing power and energy management."""

    def __init__(self, name: str, energy_level: float = 50.00):
        """
        Initialize a robot with a name and energy level.

        Args:
            name (str): The robot's unique identifier.
            energy_level (float, optional): Initial energy level. Defaults to 100.00.
        """
        self.name = name
        self.energy_level = energy_level
        self.is_powered_on = False

    def power_on(self) -> None:
        """
        Power on the robot, consuming 10% of initial energy.

        Prints status and updates energy level if not already powered on.
        """
        if not self.is_powered_on:
            print(
                f"Powering on {self.name}. Initial energy level: {self.energy_level:.2f}. Every start uses 10 percent of energy fuel"
            )
            self.is_powered_on = True
            self.energy_level -= 10.0
        else:
            print(f"{self.name} is already powered on")

    @abstractmethod
    def move(self) -> None:
        """Abstract method to define robot movement. Must be implemented by subclasses."""
        pass

    def get_energy_level(self) -> float:
        """
        Get the current energy level of the robot.

        Returns:
            float: The current energy level.
        """
        return self.energy_level
