# Contributing to lego-spike-py

Thanks for your interest in improving this project! This is a small, hobby-oriented
collection of LEGO® Education SPIKE™ Prime MicroPython programs, and the goal is to
keep it approachable for students and first-time contributors.

The most common (and most welcome) contributions are **documentation improvements** —
clarifying the README, fixing inaccuracies, adding troubleshooting notes, and
improving code comments. Code changes are welcome too, but see the note on hardware
testing below.

## Before you start

- These scripts run on the **SPIKE Prime hub** using the official SPIKE MicroPython
  runtime (`hub`, `motor_pair`, `color_sensor`, `color`, `runloop`). They do **not**
  run on a standard desktop CPython installation, so you cannot run or unit-test
  them on a regular PC.
- The assumed hardware wiring is fixed across the project:
  - Color sensor → **port B** (surface-facing)
  - Left drive motor → **port C**
  - Right drive motor → **port D**
  - Motors C and D are paired as `motor_pair.PAIR_1`

  Any change that alters this wiring must be reflected in **every** affected script and
  documented in the **Hardware Setup** section of the README.

## What makes a good change

- **Small and focused.** One improvement per pull request. A typo fix, a new
  README section, or a single script cleanup is ideal — please don't combine
  unrelated changes.
- **Grounded in the source.** If you add or correct documentation, double-check
  the claim against the actual `.py` files. For example, the `getColor()` function
  maps integer codes from `color_sensor.color()` to names (see `box.py`), and the
  "blue family" check tests codes 3, 4, and 5 (Blue, Azure, Turquoise).
- **Documentation-only is fine.** Because the robot programs require real SPIKE
  hardware to verify, pure documentation and comment improvements are a
  high-impact, low-risk way to help out — no one expects you to own a SPIKE Prime
  set to fix a README.

## Making changes

1. **Fork** the repository and create a branch from `master`:
   ```bash
   git checkout -b docs/my-improvement master
   ```
2. Make your change. Keep formatting consistent with the existing files
   (4-space indentation, simple `if`-style matching `getColor`).
3. If you change a `.py` file, **test it on real SPIKE Prime hardware** before
   submitting. Include in your PR description which hub/motor/sensor setup you
   tested with, and what behavior you observed.
4. Commit with a clear message, e.g.:
   ```
   docs(README): clarify blue-family color check
   ```
5. Open a pull request against `master`.

## Pull request description

A good PR description answers:

- **What changed?** (one or two sentences)
- **Why?** (what problem does this solve for someone using these programs?)
- **If code: what hardware did you test on?** (hub, sensor port, motor ports)
- **Type of change:** documentation / SPIKE `.py` source / other

You can copy this checklist into your PR body:

```
## Summary
<!-- What does this PR do? -->

## Why
<!-- What problem does this solve? -->

## Type of change
- [ ] documentation
- [ ] SPIKE `.py` source (tested on real hardware)
- [ ] other

## Hardware tested on (for code changes)
- Hub:
- Sensor port:
- Motor ports:
```

## Coding notes

- `getColor()` is duplicated verbatim across `box.py`, `box2.py`, `box-fast.py`,
  `box-autocorrect.py`, and `getcolor.py`. If you change the mapping, update it
  in **all** files to keep the README's Color Key table accurate.
- The `color` module is imported in every script but not currently used; leave it
  in place unless your change specifically needs it, so diffs stay minimal.
- `box-autocorrect.py` contains commented-out `stopClock` scaffolding kept
  deliberately for tuning — don't remove it unless that recovery behavior is the
  subject of your change.

## Reporting issues

Found a bug or a misleading part of the docs? Open an issue with:

1. Which file/section you're referring to.
2. Your hub/sensor/motor wiring (if relevant).
3. What you expected vs. what happened (or what the docs said vs. reality).

## Code of conduct

Be kind and patient. This is a beginner-friendly project; not everyone has the
same hardware, and most people are first-timers to both SPIKE MicroPython and
open source. Help make it easy for the next person to contribute too.

## License

By contributing, you agree that your contributions will be licensed under the
[GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0) that covers this
repository.

---

LEGO® and SPIKE™ are trademarks of the LEGO Group, which does not sponsor,
authorize, or endorse this repository.
