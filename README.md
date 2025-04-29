# Minimum Platform Needed

This repository contains a Python implementation for solving the classic scheduling problem: **finding the minimum number of railway platforms required** at a station so that no train has to wait.

## 🧩 Problem Statement

Given the arrival and departure times of `n` trains at a railway station, determine the **minimum number of platforms** required so that no train is kept waiting.

Each train occupies a platform from its arrival time to its departure time. Two trains cannot use the same platform at the same time.

### Input
- Two lists of equal length `n`:
  - `arrivals`: List of train arrival times (in 24-hour format)
  - `departures`: List of train departure times (in 24-hour format)

### Output
- A single integer `k` indicating the **minimum number of platforms** required.

## 💡 Algorithm Overview

The approach uses:
- Sorting both arrival and departure lists
- Two pointers (`i` and `j`) to iterate over both lists
- A counter for current platforms in use (`platforms_needed`)
- A tracker for the maximum platforms needed at any point (`max_platforms`)

### Time Complexity

- **O(n log n)** due to sorting
- Much more efficient than brute-force solutions (which may be O(2ⁿ))

## ✅ Example

```python
arrivals =  [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
```

- Output: `3`  
- Explanation: At time 1100–1120, 3 trains are at the station.
