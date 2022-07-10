#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import math
import os
import mqtt

class Graphics(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Graphics, self).__init__(*args, **kwargs)

    def run(self):

        # while True:
            canvas = self.matrix
        
            # read values from files
            transfer_akku = open("transfer_akku.txt", "r")
            akku = int(transfer_akku.read())

            transfer_netzBezug = open("transfer_netzBezug.txt", "r")
            netzbezug = float(transfer_netzBezug.read())


            transfer_produktion = open("transfer_produktion.txt", "r")
            produktion = float(transfer_produktion.read())

            transfer_batBezug = open("transfer_batBezug.txt", "r")
            batBezug = float(transfer_batBezug.read())

            font = graphics.Font()
            font.LoadFont("../../../fonts/7x13.bdf")

            fontAkku = graphics.Font()
            fontAkku.LoadFont("../../../fonts/5x7.bdf")

            fontTitle = graphics.Font()
            fontTitle.LoadFont("../../../fonts/5x8.bdf")

            fontNumbers = graphics.Font()
            fontNumbers.LoadFont("../../../fonts/10x20.bdf")

            
            white = graphics.Color(149, 149, 149)
            purewhite = graphics.Color(255, 255, 255)
            grey = graphics.Color(61, 61, 61)
            red = graphics.Color(247, 52, 22)
            green = graphics.Color(0, 255, 0)
            blue = graphics.Color(0, 0, 255)
            lightblue = graphics.Color(5, 205, 250)

            EKZStartX = 2
            EKZStartY = 58
            EKZWertStartX = EKZStartX+20
            NetzbezugPfeilStartX = 2
            NetzbezugPfeilStartY = 63

            PVStartX = 2
            PVStartY = 11
            PVWertStartX = PVStartX+20

            BatBezugStartX = 72
            BatBezugStartY = 38
            BatBezugPfeilStartX = 77
            BatBezugPfeilStartY = 46
            BatZahlStartX = 107
            BatZahlStartY = 7
            
            kWStartX = 15
            kWStartY = 34
            
            graphics.DrawText(canvas, fontNumbers, kWStartX, kWStartY+4, grey, "[kW]")
       

            # NETZBEZUG
            graphics.DrawText(canvas, fontTitle, EKZStartX, EKZStartY-3, red, "EKZ")
            if netzbezug >= 0.3:
                graphics.DrawText(canvas, fontNumbers, EKZWertStartX, EKZStartY+4, red, str(round(netzbezug, 2)))
                graphics.DrawText(canvas, fontTitle, NetzbezugPfeilStartX, NetzbezugPfeilStartY, red, "-->")
            elif (netzbezug < 0.3) and (netzbezug > -0.3):
                graphics.DrawText(canvas, fontNumbers, EKZWertStartX, EKZStartY+4, purewhite, "0.0")
            else:
                graphics.DrawText(canvas, fontNumbers, EKZWertStartX, EKZStartY+4, lightblue, str(round(netzbezug*-1, 2)))
                graphics.DrawText(canvas, fontTitle, NetzbezugPfeilStartX, NetzbezugPfeilStartY, lightblue, "<--")
            
            # PRODUKTION
            graphics.DrawText(canvas, fontTitle, PVStartX, PVStartY-3, green, "PV")
            if produktion > 0.1:
                graphics.DrawText(canvas, fontNumbers, PVWertStartX, PVStartY+4, green, str(round(produktion, 2)))
            else:
                graphics.DrawText(canvas, fontNumbers, PVWertStartX, PVStartY+4, purewhite, "0.0")

            # BATTERIE
            if batBezug >= 0.1:
                graphics.DrawText(canvas, fontNumbers, BatBezugStartX, BatBezugStartY, green, str(round(batBezug, 1)))
                graphics.DrawText(canvas, fontTitle, BatBezugPfeilStartX, BatBezugPfeilStartY, green, "<--")
            elif (batBezug < 0.1) and (batBezug > -0.1):
                graphics.DrawText(canvas, fontNumbers, BatBezugStartX, BatBezugStartY, purewhite, "0.0")
            else:
                graphics.DrawText(canvas, fontNumbers, BatBezugStartX, BatBezugStartY, lightblue, str(round(batBezug*-1, 1)))
                graphics.DrawText(canvas, fontTitle, BatBezugPfeilStartX+2, BatBezugPfeilStartY, lightblue, "-->")

            # batterie variables
            batStartX = 107
            batStartY = 9
            batBreite = 18
            batHoehe = 54-1
            batRandFarbe = white
            batVollFarbe = green
            batLeerFarbe = red
            batFarbe = green

            # AKKU %
            if akku < 10:
                graphics.DrawText(canvas, fontAkku, BatZahlStartX+6, BatZahlStartY, white, str(akku)+"%")
            elif akku == 100:
                graphics.DrawText(canvas, fontAkku, BatZahlStartX, BatZahlStartY, white, str(akku)+"%")
            else:
                graphics.DrawText(canvas, fontAkku, BatZahlStartX+3, BatZahlStartY, white, str(akku)+"%")

            graphics.DrawLine(canvas, batStartX+4, batStartY, batStartX+batBreite-4, batStartY, batRandFarbe)
            graphics.DrawLine(canvas, batStartX+2, batStartY+1, batStartX+batBreite-2, batStartY+1, batRandFarbe)
            graphics.DrawLine(canvas, batStartX+4, batStartY+batHoehe, batStartX+batBreite-4, batStartY+batHoehe, batRandFarbe)
            graphics.DrawLine(canvas, batStartX+2, batStartY+batHoehe-1, batStartX+batBreite-2, batStartY+batHoehe-1, batRandFarbe)
            
            graphics.DrawLine(canvas, batStartX, batStartY+4, batStartX, batStartY+batHoehe-4, batRandFarbe)
            graphics.DrawLine(canvas, batStartX+1, batStartY+2, batStartX+1, batStartY+batHoehe-2, batRandFarbe)

            graphics.DrawLine(canvas, batStartX+batBreite, batStartY+4, batStartX+batBreite, batStartY+batHoehe-4, batRandFarbe)
            graphics.DrawLine(canvas, batStartX+batBreite-1, batStartY+2, batStartX+batBreite-1, batStartY+batHoehe-2, batRandFarbe)
            
            if akku <= 10:
                batFarbe = batLeerFarbe

            akku = akku/2
            akkuLevel = int(math.ceil(akku))
            for x in range(akkuLevel):
                graphics.DrawLine(canvas, batStartX+2, batStartY+batHoehe-2-x, batStartX+batBreite-2, batStartY+batHoehe-2-x, batFarbe)

            time.sleep(10)


# Main function

# while True:
def main():
    if __name__ == "__main__":
        graphics = GraphicsTest()
        if (not graphics.process()):
           graphics.print_help()
main()
    