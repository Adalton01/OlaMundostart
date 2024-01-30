function calc ()
{
    var ini = document.getElementById( "ini" )
    var fim = document.getElementById( "fim" )
    var passo = document.getElementById( "passo" )
    var res = document.getElementById( "res" )

    if ( ini.value.length == 0 || fim.value.length == 0 || passo.value.length == 0 )
    {
        res.innerHTML = "Impossivel contar"
        // window.alert( "[Erro] Verifique os dados ..." )



    } else
    {
        res.innerHTML = "Contando : "
        var i = Number( ini.value )
        var f = Number( fim.value )
        var p = Number( passo.value )

        if ( p <= 0 )
        {
            window.alert( "Passo invalido" )
            p = 1

        }


        if ( i < f )
        {
            for ( var c = i; c <= f; c += p )//contagem crescente
            {
                res.innerHTML += `\u{1F449} ${ c } `

            }
        }
        else
        {
            for ( var c = i; c >= f; c -= p )
            {//contagem decrescente
                res.innerHTML += `\u{1F449} ${ c } `//adicionando emoji


            }
        }

        res.innerHTML += `\u{1F449} ${ c } `//adicionando 
    }
}
