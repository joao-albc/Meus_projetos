var agora = new Date()
var horario = agora.getHours()


console.log(`Sao exatamente ${hora}hrs`)

if (hora >= 18 && hora <= 24){
    console.log('Boa noite')
}
else if(hora < 12 && hora >= 6){
    console.log('Bom dia')
}
else if(hora >= 12){
    console.log('Boa tarde')
}
else if (hora > 24 || hora < 0 ){
    console.log('O horário precisa estar entre 0 e 24')
}else{
    console.log('É madrugada')
}