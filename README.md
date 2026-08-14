# Weather App — Current Conditions & Historical Climate Graphs

A Python command-line weather tool with two modes: a **live weather report** for any location,
and a **historical climate grapher** that plots a full year of daily weather data for any city
as a multi-panel matplotlib chart.

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![matplotlib](https://img.shields.io/badge/matplotlib-plotting-11557c)
![Meteostat](https://img.shields.io/badge/Meteostat-weather%20data-lightgrey)

<!-- TODO: add a screenshot of the generated 6-panel graph here. This project's whole
     selling point is the graph — showing it is worth more than any paragraph.
     Example:  ![Weather graph](docs/london-2021.png)  -->

---

## What it does

Type in a city name and the tool will:

1. **Geocode it** — resolve the city name to latitude/longitude coordinates using OpenStreetMap's
   Nominatim service, so you can type "Singapore" or "Kuala Lumpur" rather than looking up
   coordinates yourself
2. **Fetch a year of daily weather history** for that exact point from the
   [Meteostat](https://meteostat.net) network of weather stations
3. **Plot five variables side by side** in a 3×2 grid of subplots:

   | Variable | Meaning |
   |---|---|
   | `tavg` | Average daily temperature |
   | `prcp` | Daily precipitation |
   | `wdir` | Wind direction |
   | `wspd` | Wind speed |
   | `pres` | Atmospheric pressure |

Separately, a **current-conditions mode** pulls a formatted live weather report for any
location straight from [wttr.in](https://wttr.in) and prints it to the terminal — including
the ASCII-art forecast panel.

## Why two modes

Current weather answers "should I bring an umbrella today". Historical data answers "what is
this place actually like in March" — which is the more interesting question, and the one that
needs a graph rather than a number. The project covers both.

## Tech stack

| Purpose | Library |
|---|---|
| Geocoding (city name → lat/long) | [geopy](https://geopy.readthedocs.io) (Nominatim) |
| Historical weather data | [meteostat](https://dev.meteostat.net/python/) (`Point`, `Daily`) |
| Plotting | [matplotlib](https://matplotlib.org) |
| Live weather | [requests](https://requests.readthedocs.io) + [wttr.in](https://wttr.in) |
| Language | Python 3 |

## Getting started

```bash
# 1. Clone the repo
git clone https://github.com/DakshAnajwala/Weather_app-history-.git
cd Weather_app-history-

# 2. (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Historical climate graphs

```bash
python Main.py
```

```
Enter your desired city for latitude and longitude  Singapore
Singapore, Central, Singapore
The latitude for Singapore is 1.357107
The longitude for Singapore is 103.8194992
Enter the year of which weather data is needed (default is 2021)  2023
```

A matplotlib window opens with the five-variable subplot grid. Press Enter at the year prompt
to default to 2021.

### Current conditions

```bash
python Current_weather.py
```

```
Enter your desired area:  Tokyo
Weather Report for: Tokyo
   \  /       Partly cloudy
 _ /"".-.     18 °C
   \_(   ).   ↖ 11 km/h
   /(___(__)  10 km
```

## Project structure

```
Weather_app-history-/
├── Main.py              # Historical climate grapher (geopy + meteostat + matplotlib)
├── Current_weather.py   # Live weather report via wttr.in
└── requirements.txt     # Dependencies
```

## Notes and limitations

- Meteostat data availability varies by location — remote areas with no nearby weather station
  may return sparse or empty data for some variables
- Nominatim has a usage policy and rate limit; it is fine for interactive use but not for
  bulk lookups
- Currently plots one calendar year at a time; multi-year comparison is the obvious next step

## Roadmap

- [ ] Let the user pick which variables to plot instead of always plotting all five
- [ ] Support arbitrary date ranges rather than whole calendar years
- [ ] Overlay multiple years or multiple cities on the same axes for comparison
- [ ] Save the chart to a PNG instead of only showing it interactively
- [ ] Wrap both modes in a single entry point with a `--mode` flag

## Author

**Daksh Anajwala** — [@DakshAnajwala](https://github.com/DakshAnajwala)

---

<!-- HOUSEKEEPING TODO — this repo needs code fixes before the README above is accurate.
     Do these first, they are quick:

  1. RENAME `Main` → `Main.py`. The file is a valid Python script but has no extension, so
     GitHub doesn't syntax-highlight it and it doesn't look like code at a glance. This is
     the single fastest improvement to this repo.

  2. FIX `Current_weather.py` — it currently does not run. It has a stub function:

         def graph(city,start_date,end_date):
             data =

     That bare `data =` is a syntax error, so the whole file fails to import. Either delete
     the unused `graph()` stub (the working graph code already lives in `Main`), or finish
     it. Also remove the now-unused matplotlib/meteostat/datetime imports from that file if
     you delete the stub. Leaving code that doesn't even parse in a repo you're pointing a
     reviewer at is worse than not having the repo.

  3. There is a duplicate of the wttr.in script in your Progressio repo (weathermain.py).
     Pick one home for it.

  4. ADD requirements.txt — the README above tells people to pip install from it:
         geopy
         meteostat
         matplotlib
         requests
         pandas

  5. RENAME THE REPO to `weather-app`. "Weather_app-history-" with the trailing hyphens
     reads like an accident.

  6. Set the repo's About description and topics: python, weather, matplotlib, data-
     visualization, meteostat.

  7. Add a LICENSE (MIT is fine).
-->
