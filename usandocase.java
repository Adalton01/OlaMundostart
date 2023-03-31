/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package jogojava;

import java.util.Scanner;

/**
 *
 * @author Adalton
 */
public class Jogojava {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner tec = new Scanner(System.in);
        System.out.println("Digite numero de Pernas");
        int perna = tec.nextInt();
        String tipo;
        System.out.println("Seu animal e um");
        switch (perna) {
            case 2:
                tipo = "Pato";
                break;
            case 4:
                tipo = "Cavalo";
                break;
            case 7:
                tipo = "Aranha";
                break;
            default:
                tipo = "Obrigado Por Participar";
                break;


            
        

    }
        System.out.println(tipo);


    }

}
