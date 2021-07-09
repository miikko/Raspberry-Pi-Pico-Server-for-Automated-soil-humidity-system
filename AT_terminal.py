from machine import UART
import _thread
import utime

uart = UART(1, 115200)

def print_cmd_help():
    print("Check that you typed a valid AT-command.")
    print("List of valid ESP8266 AT-commands can be found from the address below.")
    print("https://www.electronicshub.org/esp8266-at-commands/")

def uart_receiver():
    while True:
        # Is none, if there are no bytes to read.
        res_bytes = uart.read()
        if res_bytes:
            # Sometimes "res_bytes" cannot be read to a string.
            # Having this try-except block is a safety measure...
            # so that the thread running this function does not crash.
            try:
                res = res_bytes.decode()
                print(res, end="")
                if "ERROR" in res:
                    print_cmd_help()
            except:
                print("Failed to decode received bytes.")
                print("Received bytes: {}".format(res_bytes))
        utime.sleep(1)

_thread.start_new_thread(uart_receiver, ())

while True:
    send = input()
    uart.write(send+'\r\n')
