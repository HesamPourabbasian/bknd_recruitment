from robot import Robot


class Flying_Robot(Robot):
    """Robot that moves by flying, consuming energy per flight."""

    def move(self) -> None:
        """
        Move the robot by flying, consuming 5 units of energy.

        Checks if the robot is powered on and has sufficient energy.
        """
        if self.is_powered_on and self.energy_level >= 5.0:
            print(f"{self.name} is flying in the sky")
            self.energy_level -= 5.0
        else:
            print(f"{self.name} can't fly. Insufficient energy fuel or robot is turned off.")
