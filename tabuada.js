function tab ()
{

    var valor = document.getElementById( "valor" )
    var res = document.getElementById( "res" )


    var val = Number( valor.value )

    if ( valor.value.length == 0 )
    {

        window.alert( "Digite Valor" )
        return;


    } else
    {
        res.innerHTML = ""

        for ( var c = 1; c <= 10; c += 1 )
        {

            res.innerHTML += `<br> ${ val } X ${ c } = ${ val * c }`




        }
        res.style.overflowY = "scroll";// Aplica estilos uma única vez fora do loop
        res.style.height = "180px"; 

    }









}