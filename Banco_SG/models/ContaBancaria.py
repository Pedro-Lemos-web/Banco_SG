class ContaBancaria:
    def _init_(self, titular: str, 
                       saldo: float,
                       limite: float):
        
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = []

    def depositar(self, valor):
        """metodo depositar

        Args:
            valor : numero float para depositar
        Returns:
            booleano: true/false para ok/
        """
        if valor > 0: 
            self.__saldo += valor
            self._historico.append([valor, self._saldo, "deposito"])
            return True
        return False
        
    def sacar(self, valor):
        """metodo sacar

        Args:
            valor (type): description

        Returns:
            type: description
        """
        
        if valor > 0: 
            if self.__saldo - valor >= 0 :
                self.__saldo -= valor
                self._historico.append([valor, self._saldo, "saque"])
        else:
            permitir = input(" deseja utilizar o limite S/N? ").upper()
            if permitir == "S":
                if self._saldo + self._limite > valor:
                    self.__saldo -= valor
                    self._historico.append([valor, self._saldo, "saque"])
                    return True
                else:
                    print("limite insuficiente!")
            else:
                print("optou por nao usar o limite !")
        return False

    def transferir (self, valor, destino):
        """metodo transferir
        Args:
        valor : numero float para sacar
        destino : obj da conta de destino
        Returns:
        booleano: true/false para ok/
        """
        if destino!= None:
            if self.sacar(valor):
                if destino.depositar(valor):
                    self._historico.append([valor, self._saldo, "transferencia"])
                    return True
        else:
            self.depositar(valor)
        return False

    def exibir_historico(self):
        print(""*10 + "historico bancario " + ""*10)        
        for operacao in self.__historico:
            print(f"{operacao[2]} de R$ {operacao[0]}. saldo final de {operacao[1]}")
        
   
    def exibir_saldo(self):
        infos = f"O saldo da conta do {self.__titular}" +\
            f" é de R${self.__saldo}"
        print(infos)