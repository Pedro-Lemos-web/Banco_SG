from models.ContaBancaria import ContaBancaria

Pedro = ContaBancaria(titular="Pedro", 
                      saldo=100.00, 
                      limite=100)

Tiago = ContaBancaria(titular="Tiago", 
                      saldo=1000.00, 
                      limite=100)

Pedro.exibir_saldo()
Tiago.exibir_saldo()

Pedro.depositar(50)
Tiago.sacar(50)

Pedro.transferir(50, Tiago)

Pedro.exibir_historico()
Tiago.exibir_historico()