package com.mycompany.votaswing;

/**
 * TelaVoto - Programa simples que calcula a idade a partir do ano de nascimento
 * e informa se a pessoa é maior ou menor de idade para votar.
 * 
 * Autor: Adalton
 */
public class TelaVoto extends javax.swing.JFrame {

    /**
     * Construtor da classe que inicializa os componentes da interface.
     */
    public TelaVoto() {
        initComponents();
    }

    /**
     * Método gerado pelo editor para inicializar componentes da interface gráfica.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">                          
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jScrollPane2 = new javax.swing.JScrollPane();
        txtdata = new javax.swing.JTextPane();
        btncal = new javax.swing.JButton();
        lblida = new javax.swing.JLabel();
        lblmen = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(255, 255, 255));

        // Label para o campo do ano de nascimento
        jLabel1.setText("Ano de Nascimento");

        jScrollPane2.setViewportView(txtdata);

        // Botão para calcular a idade e verificar condição de voto
        btncal.setText("Calcular");
        btncal.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btncalActionPerformed(evt);
            }
        });

        // Label para mostrar a idade calculada
        lblida.setText("Idade");

        // Layout dos componentes na janela
        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(59, 59, 59)
                        .addComponent(btncal))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(155, 155, 155)
                        .addComponent(lblida, javax.swing.GroupLayout.PREFERRED_SIZE, 64, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(24, 24, 24)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblmen, javax.swing.GroupLayout.PREFERRED_SIZE, 258, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(jLabel1)
                                .addGap(110, 110, 110)
                                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)))))
                .addContainerGap(41, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(27, 27, 27)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel1))
                .addGap(48, 48, 48)
                .addComponent(btncal)
                .addGap(48, 48, 48)
                .addComponent(lblida)
                .addGap(42, 42, 42)
                .addComponent(lblmen, javax.swing.GroupLayout.PREFERRED_SIZE, 26, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(43, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>                        

    /**
     * Evento chamado ao clicar no botão "Calcular"
     * Calcula a idade com base no ano informado e verifica se é maior ou menor de idade.
     */
    private void btncalActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // Obtém o ano digitado pelo usuário
        int anoNascimento = Integer.parseInt(txtdata.getText());
        int anoAtual = 2023;
        
        // Calcula a idade
        int idade = anoAtual - anoNascimento;
        
        // Exibe a idade no label
        lblida.setText(Integer.toString(idade));
        
