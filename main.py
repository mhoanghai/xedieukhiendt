def on_bluetooth_connected():
    global ketnoi
    basic.show_icon(IconNames.HEART)
    ketnoi = 1
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global ketnoi
    basic.show_icon(IconNames.SMALL_DIAMOND)
    ketnoi = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

ketnoi = 0
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)
ketnoi = 0
a = 0

def on_forever():
    global a
    if bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH)) == "quay#":
        a = 1
        basic.show_icon(IconNames.STICK_FIGURE)
    elif bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH)) == "dung#":
        a = 0
        basic.show_icon(IconNames.YES)
    else:
        a = -1
        basic.show_icon(IconNames.LEFT_TRIANGLE)
    while ketnoi == 1 and a == 1:
        pins.servo_write_pin(AnalogPin.P1, 20)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P1, 160)
        basic.pause(1000)
basic.forever(on_forever)
