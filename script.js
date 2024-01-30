
function carregar ()
{


    var msg = window.document.getElementById( "msg" )
    var img = window.document.getElementById( "img" )
    var cor = window.document.getElementById( "cor" )
    var data = new Date()
    var hora = data.getHours()
   

    msg.innerHTML = `Agora são ${ hora } horas`

    if ( hora >= 0 && hora <= 12 )
    {
        img.src = "Imagens/tarde.png"
        cor.style.background = "orange"

    } else if ( hora > 12 && hora <= 18 )
    {
        img.src = "Imagens/tarde.png"
        cor.style.background = "brown"
    }
    else
    {
        img.src = "Imagens/noite.png"
        cor.style.background = "black"
    }



}