from robot import Robot


class Wheeled_Robot(Robot):
    """Robot that moves by rolling on wheels, consuming energy per roll."""

    def move(self) -> None:
        """
        Move the robot by rolling, consuming 3 units of energy.

        Checks if the robot is powered on and has sufficient energy.
        """
        if self.is_powered_on and self.energy_level >= 3.0:
            print(f"{self.name} is rolling on wheels.")
            self.energy_level -= 3.0
        else:
            print(f"{self.name} cannot roll: insufficient energy fuel or powered off.")
