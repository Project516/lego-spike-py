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

## Why the "blue family" colors?

The box programs treat the **blue family** — color codes **3 (Blue)**, **4 (Azure)**, and **5 (Turquoise)** — as "on the line" and everything else as "off the line". Several colors are grouped this way because the SPIKE color sensor can report any of the three for the same physical surface depending on lighting, ambient color, and sensor distance, so checking all three makes line detection more robust.

The line you follow does **not** have to be blue. If your line is a different color, change the three color checks in the `while` loop (or the set of names you compare against in your own improved helper) to the family that matches your line. For example:

- A **black line** on a light surface: treat `0` (Black) as on the line.
- A **red line**: treat `9` (Red) as on the line.
- A **green line**: treat `6` (Green) as on the line.

When you adapt the script, also flip the off-line steering behavior if needed. The included scripts steer `-100` (turn one way) when off the line; if your robot turns *away* from the line instead of back toward it, change `-100` to `100` to steer the other way, or swap which motor is on port C vs port D.

## Tuning Robot Speed

All four box programs call [`motor_pair.move(pair, steering, velocity=..., acceleration=...)`](https://spike-lego.education.lego.com/en-us/python-docs/spike_prime/motor_pair/index.html#motor_pair.move). Two parameters control how the robot behaves:

- **`velocity`** — the target speed of the paired motors, in degrees per second. Higher is faster. On the hub, a medium motor's maximum is roughly **1000** deg/s, so values near `1000` are near top speed.
- **`acceleration`** — how quickly the motors ramp up to the target velocity. A small `acceleration` makes starts smooth (less wheel slip); a value close to `velocity` makes the robot start almost immediately.

The included scripts differ in how these are set:

| Script | Forward (`velocity` / `acceleration`) | Steer-back (`velocity` / `acceleration`) |
| --- | --- | --- |
| `box.py` | defaults / defaults | defaults / defaults |
| `box2.py` | `750` / `750` | `250` / `250` |
| `box-fast.py` | `1000` / `1000` | `1000` / `1000` |

A good starting point is `box2.py`'s profile: a brisk forward speed (`750`) with a much slower, more controllable steer-back (`250`). If the robot overshoots at high speed and loses the line, drop the forward `velocity`. If the steer-back is too sluggish to recover, raise the steer-back `acceleration`.

The `box-autocorrect.py` script contains commented-out scaffolding for a timed recovery sequence. The idea is to count how long the robot has been off the line, and if it stays off the line for a fixed duration, briefly steer the *other* way (or stop) to re-acquire it. This is left as a advanced tuning exercise — uncomment and adapt it to your course.

## Troubleshooting

If the robot does not behave as expected, check these in order. They are the most common hardware issues with this exact wiring (sensor on B, motors on C and D):

**The robot spins in circles and never follows the line**
- The most likely cause is the off-line steering direction. The scripts steer `-100` when the sensor is off the line. If your robot always turns *away* from the line, swap the left and right drive motors: put the motor currently on port **C** on port **D**, and vice versa. Alternatively, change the `-100` to `100` in the script.
- Confirm the color sensor sees one of the line colors when it is directly on the line. Use `getcolor.py` first to verify.

**`getcolor.py` always prints `Unknown`**
- `Unknown` (color code `-1`) means the sensor cannot decide on a color. Make sure the sensor is mounted close to the surface — LEGO recommends roughly one "stud" of clearance for reliable color detection.
- Strong direct sunlight or colored room lighting can confuse the sensor. Try a more even, neutral light.
- Verify the color sensor is actually on port **B**. If it shares a port or is on a different port, `color_sensor.color(port.B)` will return `-1`.

**The robot drives forward but does not steer back onto the line**
- Check that the line color matches what the script is looking for. The box programs only treat the blue family (Blue / Azure / Turquoise, codes 3/4/5) as "on the line". If your physical line is a different color, the robot never drives forward — it just steers (`-100`) constantly, which looks like a steering problem but is really a color mismatch. See [Why the "blue family" colors?](#why-the-blue-family-colors) for how to adapt the check.
- On very shiny or wet surfaces the sensor may misread. A matte line on a matte background works best.

**The robot stops or shows an error at `motor_pair.pair(...)`**
- The SPIKE runtime only has a few motor pairs available. If you have previously paired motors in another program without unpairing, the call may fail. Reset the hub (or run a fresh program) and try again.
- Both motors must be **medium motors** on the correct ports. A large motor or motor on the wrong port won't pair as `PAIR_1`.

**The robot is too fast / twitchy and keeps overshooting the line**
- Start from `box2.py` rather than `box.py` and lower the forward `velocity` (try `600` or `500`). See [Tuning Robot Speed](#tuning-robot-speed).
- Increase the steer-back `acceleration` so the robot reacts sooner once it leaves the line.

**The robot is sluggish or barely moves**
- The default `velocity` used by `box.py` is the motor's default, which is a moderate speed. If it feels slow, switch to `box2.py` (forward velocity `750`) or `box-fast.py` (`1000`).
- Check the battery level of the hub; motors slow down noticeably as the battery drains.

## Contributing

This is a small hobby project, but improvements are welcome. Please:

- Keep changes small and focused.
- Test your robot code on real SPIKE hardware before submitting (these programs cannot be run unit-tested on a regular PC).
- Open a pull request describing what your change does and which hub/motor/sensor setup you tested it with.

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0).

---

LEGO® and SPIKE™ are trademarks of the LEGO Group, which does not sponsor, authorize, or endorse this repository.
