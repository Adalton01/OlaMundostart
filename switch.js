var valor1 =new Date()
var diaSem =valor1.getDay()

switch (diaSem ) {
    case 0:
        console.log("Errou")    
        break;

    case 5:
        console.log("Parabens ")
          break;

    default:
        console.log("Quase Acertou")
        break;
}