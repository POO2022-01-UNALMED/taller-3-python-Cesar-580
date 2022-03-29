class Control:
    def __init__(self):
        self._tv = None

    # Enlazar
    def enlazar(self,tv):
        self._tv = tv
        self._tv.setControl(self)

    # Apagado - encendido
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    # Subir canal - Bajar canal
    def canalUp(self):
        self._tv.canalUp()
    def canalDow(self):
        self._tv.canalUp()

    # Subir volumen - Bajar volumen
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDow(self):
        self._tv.volumenDown()
    
    # Set-get canal
    def setCanal(self,canal):
        self._tv.setCanal(canal)
    def getTv(self):
        return self._tv
