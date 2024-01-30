function veri() {


    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById("txtano")    
    var resul = document.getElementById("res")

    if (fano.value.length < 0 || Number(fano.value) > ano) {
       window.alert("[Erro] verifique a data ..")
    }
    else{ var idade = ano - Number(fano.value)
          var  fsex =document.getElementsByName("radsex")
          var genero =""
          var img =document.createElement("img")
          img.setAttribute("id","foto")

    }if (fsex[0].checked) {
        genero="Homen"        
    }
    if (idade >= 0 && idade <4) {
        img.src="Imagens/nene.png"
        
        
    }else if (idade <10 ) {
        img.src="Imagens/criança.png"
        
        
    }else if (idade <=18 ) {
        img.src="Imagens/adolescente.png"
        
    }else if (idade <=50) {
        img.src="Imagens/adulto.png"
        
    }else if (idade <=100) {
        img.src="Imagens/idoso.png"
        
    }else{
        resul.innerHTML="vbvbvbv"
    }
    
     if (fsex[1].checked) {
        genero="Mulher"
        
    }else if (idade >= 0 && idade <4) {
        img.src="Imagens/nene.png"
    
    }else if (idade < 10) {
        img.src="Imagens/criança.png"
        
    }else if (idade < 18) {
        img.src="Imagens/adolescente.png"
        
    }else if (idade < 50) {
        img.src="Imagens/adulto.png"
        
    }else if (idade < 100) {
        img.src="Imagens/idoso.png"
        
    }else{
        resul.innerHTML=`Veriifique as Datas`
    }    
    
    resul.innerHTML=`Obrigado sua idade é ${idade} ${genero}`
    
resul.appendChild(img)
    
}