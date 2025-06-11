function verificar ()
{
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById( "txtano" )
    var res = document.getElementById( "res" )
    


    if ( fano.value.lenght == 0 || Number( fano.value ) > ano )
    {
        window.alert( "[Erro] Verefique os dados " )

    } else
    {
        var fsex = window.document.getElementsByName( "radsex" )
        var idade = ano - Number( fano.value )
        var genero = ""
        var img = document.createElement( "img" )//criando elemento para add fotos
        img.setAttribute( "id", "foto" )//set elemento como id foto para alteraçoes css

        if ( fsex[ 0 ].checked )
        {
            genero = "Homen"
            if ( idade >= 0 && idade <= 4 )
            {
                img.setAttribute( "src", "Imagens/nene.png" )

            } else if ( idade > 4 && idade <= 12 )
            {
                img.setAttribute( "src", "Imagens/criança.png" )

            } else if ( idade > 12 && idade <= 18 )
            {
                img.setAttribute( "src", "Imagens/adolescente.png" )
            } if ( idade > 18 && idade <50 )
            {
                img.setAttribute( "src", "Imagens/adulto.png" )

            } else if ( idade > 50 && idade <= 120 )
            {
                img.setAttribute( "src", "Imagens/idoso.png" )

            }


        }

        else if ( fsex[ 1 ].checked )
        {
            genero = "Mulher"

        } if ( idade >= 0 && idade < 4 )
        {
            img.setAttribute( "src", "Imagens/nene.png" )

        } if ( idade >= 4 && idade <= 12 )
        {
            img.setAttribute( "src", "Imagens/criança.png" )

        } if ( idade >= 12 && idade < 18 )
        {
            img.setAttribute( "src", "Imagens/adolescente.png" )

        } if ( idade >= 18 && idade < 50 )
        {
            img.setAttribute( "src", "Imagens/adulto.png" )

        } if ( idade > 50 && idade <= 120 )
        {
            img.setAttribute( "src", "Imagens/idoso.png" )
        }




        res.innerHTML = `  ${ genero } de ${ idade } anos  nascido em ${ fano.value }.`
        res.appendChild( img )//set imagem na tela
    }

}

