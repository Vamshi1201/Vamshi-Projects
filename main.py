class VivoMobile:
    def __init__(self):
        self.model = 'model'
        self.ram = 'ram'
        self.rom = 'rom'

    def info(self):
        print('Vivo', self.model, 'info :')
        print('model -',self.model)
        print('ram -',self.ram)
        print('rom-',self.rom)
        print('')


mobile1 = VivoMobile()
mobile1.model = 'v20'
mobile1.ram = '8gb'
mobile1.rom = '64gb'
mobile1.info()
mobile2 = VivoMobile()
mobile2.model = 'x50'
mobile2.ram = '16gb'
mobile2.rom = '128gb'
mobile2.info()