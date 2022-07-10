#!/bin/bash
cd /home/pi/rpi-rgb-led-matrix/bindings/python/samples/

now="$(date +'%H')"

while :
do
    if [ $now -gt 20 ] || [ $now -lt 6 ]
    then
        #echo "nacht"
        sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/graphics.py --led-rows=64 --led-cols=64 --led-slowdown-gpio=2 --led-chain=2 --led-brightness=50
    else
        #echo "tag"
        sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/graphics.py --led-rows=64 --led-cols=64 --led-slowdown-gpio=2 --led-chain=2 --led-brightness=100
    fi
done

exit 0