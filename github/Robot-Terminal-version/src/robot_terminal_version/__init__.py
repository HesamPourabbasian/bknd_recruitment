import random
from typing import List
from tabulate import tabulate
from robot import Robot
from flying_robot import Flying_Robot
from wheeled_robot import Wheeled_Robot
from hybrid_robot import Hybrid_Robot


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
