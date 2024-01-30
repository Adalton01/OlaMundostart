var Agora=new Date()
var hora = Agora.getHours()
if (hora <= 12) {
    console.log(`Bom dia Agora são ${hora}`)    
}
else if (hora <= 18){
    console.log(`Boa Tarde ${hora}`)
}
else{
    console.log(`Boa noite ${hora}`)
}