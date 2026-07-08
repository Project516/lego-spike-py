# lego-spike-py

A small collection of LEGO® Education SPIKE™ Prime micropython programs for line-following and color-sensing robots.

The scripts included here were written for the SPIKE Prime hub and use the official SPIKE MicroPython (spike) runtime.

## Requirements

- A **LEGO® Education SPIKE™ Prime** hub (the "brain").
- Two medium motors driving the wheels, connected to **ports C and D**.
- One **color sensor** mounted on the robot, connected to **port B**, facing the surface the robot drives on.
- The SPIKE app to transfer the `.py` files onto the hub.

> The scripts import `hub`, `motor_pair`, `color_sensor`, `color`, and `runloop` which are all a part of the SPIKE MicroPython runtime. They will **not** run on a standard desktop CPython install.

## Hardware Setup

| Component | Hub Port |
| --- | --- |
| Color sensor | **B** (the surface-facing sensor) |
| Left drive motor | **C** |
| Right drive motor | **D** |

The scripts pair motors C and D as `motor_pair.PAIR_1` and drive the pair based on the color the port B sensor sees.

## Included Programs

### Color detection

- [`getcolor.py`](getcolor.py) — A debugging helper. Continuously reads the color sensor on port B and prints the detected color (as a name) once per second. Useful to verify your sensor is wired up and to test what the sensor reports on different surfaces.

### Line-following ("box") variants

All of the box programs follow a line by moving straight ahead when the color sensor detects a blue family color (Blue, Azure, or Turquoise) and steering back when it does not. They differ in speed/aggressiveness and in the extra code left in for tuning.

- [`box.py`](box.py) — Base line-follower. Drives the motor pair forward (steering `0`) when the sensor sees a blue family color, otherwise steers (`-100`) back toward the line.
- [`box2.py`](box2.py) — Same logic as `box.py`, with explicitly tuned `velocity` and `acceleration` (forward `750`, steer-back `250`).
- [`box-fast.py`](box-fast.py) — Higher-speed variant (`velocity=1000`, `acceleration=1000` for both moves).
- [`box-autocorrect.py`](box-autocorrect.py) — Adds commented-out scaffolding for a timed recovery sequence (a `stopClock` idea), which can be enabled while you are tuning the robot's behavior.

## Color Key

The `getColor` helper used across the scripts maps the SPIKE `color_sensor.color()` integer codes to names:

| Code | Color name |
| --- | --- |
| -1 | Unknown |
| 0 | Black |
| 1 | Magenta |
| 2 | Purple |
| 3 | Blue |
| 4 | Azure |
| 5 | Turquoise |
| 6 | Green |
| 7 | Yellow |
| 8 | Orange |
| 9 | Red |
| 10 | White |

Note: the SPIKE color codes above are what the runtime reports for the detected color; the names are returned from the sensor on port B.

## How to Run

1. Open one of the `.py` files in the SPIKE app or your preferred SPIKE MicroPython editor.
2. Connect your SPIKE Prime hub over USB or Bluetooth.
3. Transfer / run the program on the hub.

Each program's `main()` coroutine is started with `runloop.run(main())`, which is the standard SPIKE MicroPython entry point.

## Contributing

This is a small hobby project, but improvements are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full guide — in short, please:

- Keep changes small and focused.
- Test your robot code on real SPIKE hardware before submitting (these programs cannot be run unit-tested on a regular PC).
- Open a pull request describing what your change does and which hub/motor/sensor setup you tested it with.

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0).

---

LEGO® and SPIKE™ are trademarks of the LEGO Group, which does not sponsor, authorize, or endorse this repository.
