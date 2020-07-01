var lista = [5,4,7,9,6,2,1]
var nota = 0
var total = 0
var media = 0
var soma = 0
var abaixo_media = []
/*
while (nota != 11) {
    nota = console.writeline('Digite seu nome: ')
    if (nota != 11){
        notas.push(nota)
    }
}*/

total = lista.length
console.log(`Foram adicionadas ${total}`)


for (c=0;c<total;c++){
    soma += lista[c]
}
console.log(`A soma dos valores é igual a ${soma}`)


media = soma/total
console.log(`A média é igual a ${media.toFixed(2)}`)

for (c = 0; c < total; c++){
    if (lista[c] > media){
        abaixo_media.push(lista[c])
    }
}

console.log(`Foram ${abaixo_media.length} abaixo da média`)


for (c = 0; c < total; c++){
    console.log(lista[c])
    }

for (c = total; c > 0; c--){
    console.log(lista[c])
    }