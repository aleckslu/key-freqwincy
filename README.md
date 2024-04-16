Work in Progress

- record time of keydown during taps (alphas)
- record time of keydown for holds (mods)

# Key FreqWINcy

A simple key frequency logger that counts the number of times each key is pressed, along with what program was active at the time, and saves the data in a JSON file.

## Security Concerns
- **Does not** track the time or order the keys are pressed, just the count.
- Default settings logs keypresses in a closed scope, and saves the data every 30 minutes (1,800,000 ms).

## Requirements
- python3
- pynput

## How To Run

## Settings
```

```
