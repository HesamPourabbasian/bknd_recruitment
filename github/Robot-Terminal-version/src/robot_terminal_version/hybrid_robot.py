from energy_efficient import EnergyEfficient
from flying_robot import Flying_Robot
from wheeled_robot import Wheeled_Robot


class Hybrid_Robot(EnergyEfficient, Flying_Robot, Wheeled_Robot):
    """Robot that can switch between flying and rolling modes with energy-efficient power-on."""

    def __init__(self, name: str, energy_level: float = 50.00):
        """
        Initialize a hybrid robot with a name, energy level, and default mode.

        Args:
            name (str): The robot's unique identifier.
            energy_level (float, optional): Initial energy level. Defaults to 50.00.
        """
        super().__init__(name, energy_level)
        self.mode = "flying"

    def switch_mode(self, mode: str) -> None:
        """
        Switch the robot's movement mode between flying and rolling.

        Args:
            mode (str): The mode to switch to ('flying' or 'rolling').
        """
        if mode in ["flying", "rolling"]:
            self.mode = mode
            print(f"{self.name} switched to {mode} mode.")
        else:
            print(f"{self.name}: Invalid mode {mode}.")

    def move(self) -> None:
        """
        Move the robot based on its current mode (flying or rolling).

        Calls the appropriate parent class's move method.
        """
        if self.mode == "flying":
            Flying_Robot.move(self)
        else:
            Wheeled_Robot.move(self)
