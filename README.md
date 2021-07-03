# Setup

## 1. Download [MicroPython](https://micropython.org/)

MicroPython binaries can be downloaded [here](https://micropython.org/download/rp2-pico/). This project was developed with MicroPython version 1.16.

## 2. Add MicroPython to Pico

Push and hold the BOOTSEL button (the white button near the Micro-USB port) and plug your Pico into the USB port of your computer. Release the BOOTSEL button after your Pico is connected. Pico should appear on your computer as a Mass Storage Device called **RPI-RP2**.

Drag and drop the downloaded file containing MicroPython to the RPI-RP2 volume. The Pico should then reboot automatically after which MicroPython is installed in the Pico.

## 3. Programming the Pico

The [**mpremote**](https://pypi.org/project/mpremote/) Python module can be used to write and execute MicroPython code directly on the Pico via REPL and to copy files from your computer to the Pico.

Install mpremote: `$ pip install mpremote`

In order to use mpremote, Pico must be connected to your computer.

### 3.1 Writing and executing MicroPython code via REPL

To start the REPL: `$ mpremote`

To exit REPL, press Control + Å (On Skandinavian keyboards)

### 3.2 Copying MicroPython scripts to Pico

To copy a MicroPython script `myfile.py` to Pico as `main.py`: `$ mpremote cp myfile.py :main.py`

If a MicroPython script is copied to the Pico with the name `main.py`, Pico will run it on any following startups. If the script is not meant to be executed during startup, it should be copied to the Pico with a different name.

To remove copied files from Pico: `$ mpremote rm :<filename>`
