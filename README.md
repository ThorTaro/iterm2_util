# iTerm2 Utils
## Overview#1 ```myterm```
![Overview](./resources/overview.png)
- This is my iTerm2-Util commands, ```myterm```.
  - This command executes:
    - split panes
    - run some commands:
      - check ping command
      - show time with big figures on pane
      - get SSID of Wi-Fi now connected

- These scripts are using iTerm2 official APIs with Python.

## Overview#2 ```chbg```
- This is my iTerm-Util commands, ```chbg```.
  - This command switches current iTerm preset.

## Environments
- It works for me:
  - MacOS: Monterey(version 12.2.1)
  - iTerm2: version 3.4.15
  - Python: 3.9.5
  - zsh: 5.8.1 (x86_64-apple-darwin20.6.0

## Requirements
- Python packages
  - ``` pip3 install -r ./requirements.txt ```
- zsh commands
  - ping
  - watch
  - figlet

## Additional settings
- enable Python API on iTerm2
  - Turn on: ``` Preferences > General > Magic > Enable Python API ```

- import iTerm2 themes(If you use ```chbg```)
  - by default, we need four iTerm2 themes. Please go to [iTerm2 themes site](https://iterm2colorschemes.com/) and download these four themes:
    - Twilight
    - Violet Light
    - Solarized Dark Higher Contrast
    - Ubuntu
  - and import these themes on: ``` Preferences > Profiles > Colors > Color presets > Import...```

- change each path if you need


## Usage
### ```myterm```
- just run ```myterm```.

### ```chbg```
- run ```chbg [local|dev|stg|prd]```.
  - local(default): change theme, Twilight.
  - dev: change theme, Violet Light.
  - stg: change theme, Solarized Dark Higher Contrast.
  - prd: change theme, Ubuntu


## References
- [iTerm2 official](https://iterm2.com/)
- [iTerm2 themes site](https://iterm2colorschemes.com/)