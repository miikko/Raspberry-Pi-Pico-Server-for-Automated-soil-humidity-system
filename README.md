# Setup

## 1. Download MicroPython

Download [link](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2)

## 2. Add MicroPython to Pico

Push and hold the BOOTSEL button and plug your Pico into the USB port of your computer. Release the BOOTSEL button after your Pico is connected. Pico should appear on your computer as a Mass Storage Device called RPI-RP2.

Drag and drop the downloaded MicroPython file to the RPI-RP2 volume. The Pico should then reboot automatically after which MicroPython is installed in the Pico.

## 3. Programming directly on Pico with MicroPython REPL via USB

### 3.1 Windows

Download Coolterm serial port terminal software from [here](https://coolterm.en.lo4d.com/windows).

Extract downloaded `CoolTermWin.zip` and install Coolterm by running `Coolterm.exe`. During installation select the 'Use Defaults' option.

The program should start once the installation is complete. In the program GUI, select 'Options'. On the opened window in the 'Port' dropdown menu, select the COM version that is compatible with your computer.

You can check which version is compatible by opening the 'Device Manager' program and expanding the 'Ports (COM & LPT)' item. See the COM version behind 'USB Serial Device'.

Now open the 'Terminal' view in Coolterm popup window. Set the 'Terminal Mode' select the 'Line Mode' option. You can now close the popup window.

Now you can connect to the Raspberry Pi Pico by pressing the 'Connect' button on the Coolterm GUI. You can now run MicroPython commands by typing on the command line at the bottom. Test this by typing `print("Hello Pico")`.
