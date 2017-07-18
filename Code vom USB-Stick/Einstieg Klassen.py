class Konto:

    def __init__(self, kontoinhaber, kontonummer, kontostand = 0.0):
        kontoinhaber = str(kontoinhaber)
        if isinstance(kontoinhaber, str) and isinstance(kontonummer, int) and isinstance(kontostand, float):
            self.__kontoinhaber = kontoinhaber
            self.__kontonummer = kontonummer
            self.__kontostand = kontostand



    def einzahlen(self, geldmenge):
        if float(geldmenge) >= 0.01:
            self.__kontostand = self.__kontostand + geldmenge
            print(self.__kontostand)
            return print("Das Geld wurde eingezahlt.")
        else:
            return print("Das Geld konnte nicht eingezahlt werden. Bitte geben Sie einen größeren Betrag ein.")



    def auszahlen(self, geldmenge):
        if float(geldmenge) >= 0.01 and geldmenge < self.__kontostand:
            self.__kontostand = self.__kontostand - geldmenge
            print(self.__kontostand)
            print("Das Geld wurde ausgezahlt.")
            return True
            
        else:
            print("Sie haben nicht genug Geld auf Ihrem Konto.")
            return False
            


    def kontostand(self):
        print(self.__kontostand)
        return kontostand



    def überweisen(self, geldmenge, zielkonto):
        if float(geldmenge) >= 0.01 and geldmenge < self.__kontostand:
            self.__kontostand = self.__kontostand - geldmenge
            zielkonto.einzahlen(geldmenge)
            print(self.__kontostand)
            zielkonto.kontostand
            return True


            
    def __add__(self, other):
        neuer_kontostand = self.kontostand + other.kontostand
        str(self, " + ", other) = Konto(self.kontonummer, neuer_kontostand)












        
#Konto erstellen

JEK = Konto("Jonas", 3158)
JEK.einzahlen(1000)
JEK.auszahlen(50)
JEK.kontostand()






