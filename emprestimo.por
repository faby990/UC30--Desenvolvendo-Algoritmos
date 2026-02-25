programa {
    funcao inicio() {
        real valor, salario
        inteiro anosPagamento

        escreva("Digite o valor da casa:")
        leia(valor)

        escreva("Digite seu salário:")
        leia(salario)

        escreva("Digite em quantos anos você vai pegar:")
        leia(anosPagamento)

        meses = anosPagamento * 12
        prestacaoMensal = valor / meses
        limite = salario * 0.30

        se(prestacaoMensal<=limite){
            escreva("Empréstimo aprovado!")
        }
        senao{
            escreva("Empréstimo negado!")
        }
        }
    }