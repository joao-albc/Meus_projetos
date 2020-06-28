function parImpar(num){
    if (num%2==1){
        return 'Ímpar'
    }else if (num == 0) {
        return 'Zero'
    }else{
        return 'Par'
    }
}

console.log(parImpar(-2))