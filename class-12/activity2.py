class Computer:
    def __init__(self):
        self.__maximum = 270000


    def sell(self):
        print("===========Computer Specifications===========")
        print("Processor Platform: AMD")
        print("Processor: Ryzen 9 9950x")
        print("Motherboard: MSI MAG X870E Tomahawk WIFI")
        print("RAM: 64GB (32x2) G.Skill Trident Z5 RGB 6000MHz DDR5 CL30")
        print("SSD: ACER Predator 2TB Gen4 NVMe M.2")
        print("Case: NZXT H5 Flow (Non-RGB)")
        print("Fan: Jonsbo HF12 High-Pressure Low Noise Performance Fan (Non-RGB) x 7  (3 for front , 1for rear, 3 for AIO-TOP)")
        print("GPU: Zotac Gaming GeForce RTX 5070 TI Solid Core")
        print("CPU Cooler: ThermalTake TH360 V2 Ultra AIO Black Edition with LCD")
        print("Power Supply: ThermalTake ToughPower GF A3 850W 80+ Gold Fully Modular")
        print("Cable Management: Custom Sleeved Cables")
        print("Thermal Paste: Thermal Grizzly Kryonaut")
        print("Monitor: MSI G274QPF E2 27 Inch Gaming Monitor")
        print("============Computer Specifications===========")
        print(f"Selling computer for ₹{self.__maximum}.")

    def setMaximum(self, maximum):
        self.__maximum = maximum

ComputerCallable = Computer()
ComputerCallable.sell() 

ComputerCallable.__maximum = 280000
ComputerCallable.sell()

ComputerCallable.setMaximum(280000)
ComputerCallable.sell()