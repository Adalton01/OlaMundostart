// Array para armazenar os valores adicionados
var valores = [];

// Função chamada ao clicar no botão "Adicionar"
function name01 ()
{
    // Obtém os elementos do DOM
    var n = document.getElementById( "text01" );
    var lis = document.getElementById( "list01" );
    // Converte o valor de entrada para um número
    var valor = Number( n.value );

    // Verifica se o valor está entre 1 e 100
    if ( valor >= 1 && valor <= 100 )
    {
        // Verificação se o valor já está na lista
        if ( valores.includes( valor ) )
        {
            window.alert( "Valor já está na lista" );
        } else
        {
            // Adiciona o valor ao array se não estiver presente
            valores.push( valor );
            // Atualiza a lista exibida
            atualizarLista();
        }
        // Limpa o campo de entrada e foca nele
        n.value = "";
        n.focus();
    } else
    {
        // Exibe um alerta se o valor estiver fora do intervalo permitido
        window.alert( "Corrija o valor" );
        // Limpa o campo de entrada e foca nele
        n.value = "";
        n.focus();
    }
}

// Função para atualizar a lista exibida
function atualizarLista ()
{
    // Obtém o elemento da lista do DOM
    var lis = document.getElementById( "list01" );
    // Limpa a lista atual
    lis.innerHTML = "";
    // Itera sobre os valores no array e cria novos elementos de opção
    for ( var i = 0; i < valores.length; i++ )
    {
        var item = document.createElement( "option" );
        // Define o texto do elemento de opção
        item.innerHTML = `Valor ${ valores[ i ] } adicionado`;
        // Adiciona o novo elemento de opção à lista
        lis.appendChild( item );
    }
}

// Função para finalizar a entrada de dados e calcular resultados
function finalizar ()
{
    // Verifica se há valores no array
    if ( valores.length === 0 )
    {
        window.alert( "Nenhum valor foi adicionado." );
        return;
    }

    // Encontra o maior e o menor valor no array
    var maior = Math.max( ...valores );
    var menor = Math.min( ...valores );

    // Calcula a soma de todos os valores
    var soma = valores.reduce( ( total, num ) => total + num, 0 );
    // Calcula a média dos valores
    var media = soma / valores.length;


    // Exibe o maior, menor e a média na div de resultados com até 2 decimais
    var res1 = document.getElementById( "res" );
    res1.innerHTML = `Maior valor ${ maior } <br> Menor valor: ${ menor } <br> Média: ${ media.toFixed( 2 ) }`;

    // Exibe o total de itens adicionados
    res1.innerHTML += ` <br> Quantidade de numeros              pbbbbbZC              digitados ${ valores.length }  <br>  Soma total: ${ soma.toFixed( 2 ) } <br>`;
}