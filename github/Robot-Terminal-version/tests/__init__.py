import random
from abc import ABC, abstractmethod
from typing import List
from tabulate import tabulate


# Abstract base class for robot models, defining core attributes and methods
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


# Mixin for energy-efficient power-on behavior
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


# Robot subclass for flying robots
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


# Robot subclass for wheeled robots
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


# Hybrid robot combining flying and wheeled capabilities with energy efficiency
class Hybrid_Robot(EnergyEfficient, Flying_Robot, Wheeled_Robot):
    """Robot that can switch between flying and rolling modes with energy-efficient power-on."""
    def __init__(self, name: str, energy_level: float = 50.00):
        """
        Initialize a hybrid robot with a name, energy level, and default mode.

        Args:
            name (str): The robot's unique identifier.
            energy_level (float, optional): Initial energy level. Defaults to 100.00.
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


# Simulate a group of robots with random actions
def simulate_robots(num_robots: int = 50, num_actions: int = 3) -> None:
    """
    Simulate a group of robots performing actions and track energy consumption.

    Displays results in a formatted table using tabulate.

    Args:
        num_robots (int, optional): Number of robots to simulate. Defaults to 50.
        num_actions (int, optional): Number of actions per robot. Defaults to 5.
    """
    # Initialize list to store robots
    robots: List[Robot] = []
    for i in range(num_robots):
        name = f"Robot-{i + 1}"
        robot_type = random.choice(["flying", "wheeled", "hybrid"])
        if robot_type == "flying":
            robots.append(Flying_Robot(name))
        elif robot_type == "wheeled":
            robots.append(Wheeled_Robot(name))
        else:
            robots.append(Hybrid_Robot(name))

    # List to store table data for each robot
    table_data = []
    total_energy_consumed = 0.0
    for robot in robots:
        print(f"\nSimulating {robot.name} ({type(robot).__name__})")
        initial_energy = robot.get_energy_level()
        robot.power_on()
        for _ in range(num_actions):
            if isinstance(robot, Hybrid_Robot):
                if random.random() < 0.3:  # 30% chance to switch
                    robot.switch_mode(random.choice(["flying", "rolling"]))
            robot.move()
        final_energy = robot.get_energy_level()
        energy_consumed = initial_energy - final_energy
        total_energy_consumed += energy_consumed
        # Add robot data to table
        table_data.append([
            robot.name,
            type(robot).__name__,
            f"{initial_energy:.2f}",
            f"{final_energy:.2f}",
            f"{energy_consumed:.2f}"
        ])

    # Calculate average energy consumption
    avg_energy_per_robot = total_energy_consumed / num_robots if num_robots > 0 else 0.0

    # Print robot results in a table
    print("\nRobot Simulation Results:")
    headers = ["Robot Name", "Robot Type", "Initial Energy", "Final Energy", "Energy Consumed"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Print simulation summary
    print("\nSimulation Summary:")
    print(f"Total robots: {num_robots}")
    print(f"Total energy consumed: {total_energy_consumed:.2f}")
    print(f"Average energy consumed per robot: {avg_energy_per_robot:.2f}")


# Entry point for the simulation
if __name__ == "__main__":
    """Run the robot simulation with a fixed random seed for reproducibility."""
    random.seed(42)  # For reproducibility
    simulate_robots()