function carregar ()
{

    var msg = window.document.getElementById( "msg" )
    var img = window.document.getElementById( "img" )
    var data = new Date()
    //var hora =data.getHours()
    hora = 22
    var cor = document.getElementById( "cor" )

    msg.innerHTML = `Agora são ${ hora } horas.`

    if ( hora >= 0 && hora <= 12 )
    {
        img.src = "Imagens/Manha.png"
        cor.style.background = "#f49e12"
    } else if ( hora >= 12 && hora <= 18 )
    {
        img.src = "Imagens/tarde.png"
        cor.style.background = "#838383"

    } else
    {
        img.src = "Imagens/noite.png"
        cor.style.background = "Black"
    }

}
