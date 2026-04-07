# Inverted Pendulum - ROS 2
A complete ROS 2 implementation of an inverted pendulum control system.
## Nodes
- pendulum_sim_node: Publishes simulated angle on /pendulum_angle
- controller_node: PID controller, publishes PWM on /control_output
- motor_node: Reads PWM command, drives motor
## Pipeline
pendulum_sim_node → /pendulum_angle → controller_node → /control_output →
motor_node
## Tech Stack
ROS 2 Humble, Python, Ubuntu 22.04
## Status
Simulation complete. Hardware integration in progress.
