function start ()
{
  var ini = document.getElementById( "ini" )
  var fim = document.getElementById( "fim" )
  var pas = document.getElementById( "pas" )
  var res = document.getElementById( "res" )


  if ( ini.value.length <= 0 || fim.value.length <= 0 || pas.value.length <= 0 )
  {
    window.alert( "ERRO..... Digite os numeros" )

  }
  else
  {
    ini1 = Number( ini.value )
    fim1 = Number( fim.value )
    pas1 = Number( pas.value )

    if ( ini1 <= fim1 )//contagem crescente 
    {
      for ( var c = ini1; c <= fim1; c += pas1 )
      {
        res.innerHTML += `  \u{1F604}${ c }`

      }
    } else // contagem regressiva
    {
      for ( var c = ini1; c >= fim1; c -= pas1 )
      {
        res.innerHTML += `\u{1F643} ${ c }`


      }
    }



  }
}





