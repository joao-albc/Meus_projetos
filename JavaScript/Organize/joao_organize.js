var notas = []
var total = 0
var nota = 0
var soma = 0
var media = 0
var acima_media = []
var abaixo_7 = []


while (nota != -1){
    nota = window.prompt("Digite uma nota (-1 para encerrar)")
    if (nota != -1){
        notas.push(nota);
    }
}

total = notas.length;
console.log(`O total de notas foi ${total}`)

//Um ao lado do outro
console.log(notas.join(','))

for (c=total-1; c>-1;c--){
    console.log(notas[c])
}

for (c=0; c<total;c++){
    soma += notas[c]
}
console.log(`A soma das notas foi ${soma}`)

media = soma/total
console.log(`A  média dos ${total} valores é igual a ${media.toFixed(2)}`)

for (c=0;c<total;c++){
    if (notas[c] > media){
        acima_media.push(notas[c])
    }
}
console.log(`Valores acima da média: ${acima_media.length}`)

for (c=0;c<total;c++){
    if (notas[c] < 7){
        abaixo_7.push(notas[c])
    }
}
console.log(`Valores abaixo da nota (7): ${abaixo_7.length}`)

console.log("Notas inseridas")