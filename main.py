def DongCo(out1: number, out2: number, out3: number, out4: number):
    pins.analog_write_pin(AnalogPin.P12, out2)
    pins.analog_write_pin(AnalogPin.P13, out1)
    pins.analog_write_pin(AnalogPin.P14, out4)
    pins.analog_write_pin(AnalogPin.P16, out3)

def on_bluetooth_connected():
    global ketnoi
    basic.show_icon(IconNames.YES)
    ketnoi = 1
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global ketnoi
    basic.show_icon(IconNames.NO)
    ketnoi = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

ketnoi = 0
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)
ketnoi = 0
dulieuGui = ""
dulieuNhan = ""

def on_forever():
    global dulieuNhan
    if ketnoi == 1:
        dulieuNhan = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        if dulieuNhan == "up#":
            basic.show_arrow(ArrowNames.NORTH)
            DongCo(1023, 0, 1023, 0)
        elif dulieuNhan == "down#":
            basic.show_arrow(ArrowNames.SOUTH)
            DongCo(0, 700, 0, 700)
        elif dulieuNhan == "right#":
            basic.show_arrow(ArrowNames.WEST)
            DongCo(1000, 0, 0, 1000)
            basic.pause(200)
            DongCo(0, 0, 0, 0)
        elif dulieuNhan == "left#":
            basic.show_arrow(ArrowNames.EAST)
            DongCo(0, 1000, 1000, 0)
            basic.pause(200)
            DongCo(0, 0, 0, 0)
        elif dulieuNhan == "pause#":
            basic.show_leds("""
                . # . # .
                                . # . # .
                                . # . # .
                                . # . # .
                                . # . # .
            """)
            DongCo(0, 0, 0, 0)
        elif dulieuNhan == "play#":
            basic.show_leds("""
                . . . # .
                                . . # # .
                                . # # # .
                                . . # # .
                                . . . # .
            """)
            DongCo(700, 0, 700, 0)
        elif dulieuNhan == "heart#":
            basic.show_icon(IconNames.HEART)
            DongCo(0, 1000, 1000, 0)
basic.forever(on_forever)
