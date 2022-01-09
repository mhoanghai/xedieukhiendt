function DongCo (out1: number, out2: number, out3: number, out4: number) {
    pins.analogWritePin(AnalogPin.P12, out2)
    pins.analogWritePin(AnalogPin.P13, out1)
    pins.analogWritePin(AnalogPin.P14, out4)
    pins.analogWritePin(AnalogPin.P16, out3)
}
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
    ketnoi = 1
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
    ketnoi = 0
})
let dulieuNhan = ""
let ketnoi = 0
let dulieuGui = ""
bluetooth.startUartService()
basic.showIcon(IconNames.Square)
ketnoi = 0
basic.forever(function () {
    if (ketnoi == 1) {
        dulieuNhan = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
        if (dulieuNhan == "up#") {
            basic.showArrow(ArrowNames.North)
            DongCo(1023, 0, 1023, 0)
        } else if (dulieuNhan == "down#") {
            basic.showArrow(ArrowNames.South)
            DongCo(0, 700, 0, 700)
        } else if (dulieuNhan == "right#") {
            basic.showArrow(ArrowNames.West)
            DongCo(1000, 0, 0, 1000)
            basic.pause(200)
            DongCo(0, 0, 0, 0)
        } else if (dulieuNhan == "left#") {
            basic.showArrow(ArrowNames.East)
            DongCo(0, 1000, 1000, 0)
            basic.pause(200)
            DongCo(0, 0, 0, 0)
        } else if (dulieuNhan == "pause#") {
            basic.showLeds(`
                . # . # .
                . # . # .
                . # . # .
                . # . # .
                . # . # .
                `)
            DongCo(0, 0, 0, 0)
        } else if (dulieuNhan == "play#") {
            basic.showLeds(`
                . . . # .
                . . # # .
                . # # # .
                . . # # .
                . . . # .
                `)
            DongCo(700, 0, 700, 0)
        } else if (dulieuNhan == "heart#") {
            basic.showIcon(IconNames.Heart)
            DongCo(0, 1000, 1000, 0)
        }
    }
})
