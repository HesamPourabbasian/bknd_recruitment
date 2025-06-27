class EnergyEfficient:
    """Mixin to provide energy-efficient power-on functionality, consuming less energy."""
    def power_on(self) -> None:
        """
        Power on the robot in energy-saving mode, consuming 5 units of energy.

        Overrides the default power_on behavior for efficiency.
        """
        if not self.is_powered_on:
            print(
                f"{self.name} is powered on in saving mode to reduce energy usage. Energy level: {self.energy_level:.2f}"
            )
            self.is_powered_on = True
            self.energy_level -= 5.0
        else:
            print(f"{self.name} is already powered on")