Work in Progress

- saved every x amount of keypresses & when keyboard interrupt is hit
- backs up loaded .json file
- when keyboard interrupt exits, a `_TOTAL_LOG` attribute is added onto the object with the combined keypresses of all loaded data + data recorded this session

# Key FreqWINcy

A simple key frequency logger that counts the number of times each key is pressed, along with what program was active at the time, and saves the data in a JSON file.

## Security Concerns
- **Does not** track the time or order the keys are pressed, just the count.
- Default settings logs keypresses in a closed scope, and saves the data every 30 minutes (1,800,000 ms).

## Issues
- Could be just my specific keyboard:
  - Not properly recording keys correctly when `ctrl` is held down. 
  - Keyboard Interrupt not properly stopping (Current workaround - f17 global hotkey)

## Requirements
- python3
- pynput

## How To Run

## Settings
```

```

## Inspirations
benign-key-logger
