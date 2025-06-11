/seu-projeto
│
├── index.html
├── tela.css
├── script.js
└── Imagens/
      ├── Manha.png
      ├── tarde.png
      └── noite.png
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Hora do Dia</title>
    <link rel="stylesheet" href="tela.css" />
</head>

<body onload="carregar()"> <!-- Chama a função carregar ao carregar a página -->

    <h1>Hora do Dia</h1>

    <section id="cor">
        <div id="msg">Aqui a Hora Certa</div>
        <div id="foto">
            <img id="img" src="Imagens/tarde.png" alt="Manhã" />
        </div>
    </section>

    <footer>
        <p>&copy; Dev Dalton</p>
    </footer>

    <script src="script.js"></script>
</body>

</html>


/* Define o estilo geral da página */
body {
    background: blue;
    color: azure;
    font: normal 15pt Arial, sans-serif;
}

/* Cabeçalho */
h1 {
    text-align: center;
}

/* Seção principal com fundo branco e bordas arredondadas */
section {
    background: white;
    border-radius: 10px;
    padding: 15px;
    width: 500px;
    margin: auto; /* Centraliza horizontalmente */
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.577); /* Sombra ao redor da seção */
    color: black;
}

/* Rodapé com texto branco e itálico */
footer {
    color: white;
    text-align: center;
    font-style: italic;
}

/* Centraliza o texto dentro das divs e adiciona espaçamento */
div {
    text-align: center;
    padding: 8px;
}


function carregar() {
    // Seleciona os elementos do DOM que serão manipulados
    var msg = document.getElementById("msg");
    var img = document.getElementById("img");
    var cor = document.getElementById("cor");

    var data = new Date();
    // Pega a hora atual (descomente a linha abaixo para pegar a hora real)
    // var hora = data.getHours();

    // Para testes, a hora está fixada em 22 (10 da noite)
    var hora = 22;

    // Exibe a hora atual na mensagem
    msg.innerHTML = `Agora são ${hora} horas.`;

    // Altera a imagem e a cor de fundo conforme o horário
    if (hora >= 0 && hora < 12) {
        img.src = "Imagens/Manha.png";
        cor.style.background = "#f49e12"; // Cor laranja para manhã
    } else if (hora >= 12 && hora < 18) {
        img.src = "Imagens/tarde.png";
        cor.style.background = "#838383"; // Cinza para tarde
    } else {
        img.src = "Imagens/noite.png";
        cor.style.background = "black"; // Preto para noite
    }
}


