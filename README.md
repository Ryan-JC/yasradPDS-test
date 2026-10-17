# yasradPDS

**SRAD Parachute Design System**: a simulation-based design tool for the
McMaster Rocketry team's parachute recovery systems. Size a canopy,
get the gore pattern to cut, and see the loads, descent and landing
dispersion that go with it.

## Setup

Requires Python 3

```shell
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell
pip install -r requirements.txt
```

## Usage

```shell
yasradpds run my_chute.ypd
yasradpds dispersion my_chute.ypd --trials 500 --seed 42
yasradpds --version
```

## Project layout

Code lives under `src/yasradPDS/`. Each folder only depends on the ones
before it, and the core has no file or screen code in it.

| Folder | What it holds |
| --- | --- |
| `0-design` | Design data classes, default values, unit conversion to SI |
| `1-physics` | Pure math: atmosphere, aerodynamics, opening shock, constants |
| `2-geometry` | Canopy shape interface and each shape's gore pattern |
| `3-engine` | Single-design analysis, RocketPy dispersion, environment, structures |
| `4-system` | Drogue + main dual-deploy staging |
| `5-visualize` | Plots, gore preview, 3D render |
| `6-import_export` | CSV, DXF, PDF template, text report, load/save design files |
| `7-gui` | Graphic user interface for editing design arguments |
| `8-cli` | Command-line frontend |

`main.py` is the entry point that starts a frontend.

## Design file

A design is a JSON file (`.ypd`). Keys are stable field names, not GUI
labels, and the unit is part of the name. Values are stored in the units
people measure in and converted to SI in one place (`0-design/units.py`).

```json
{
  "schema_version": 1,
  "main": {
    "diameter_ft": 6.0,
    "gore_count": 8
  }
}
```
