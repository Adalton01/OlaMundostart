<?php
// Loop externo para iterar de 1 a 10 (para cada número da tabuada)
for ($i = 1; $i <= 10; $i++) { ?>
    <div>
        <!-- Exibe o título da tabuada atual -->
        <h2>Tabuada <?php echo $i; ?></h2>

        <?php 
        // Loop interno para multiplicar o número atual ($i) por 1 até 10
        for ($j = 1; $j <= 10; $j++) { ?>
            <!-- Exibe a operação e o resultado da multiplicação -->
            <?php echo $i; ?> x <?php echo $j; ?> = <?php echo $i * $j; ?> <br>
        <?php } ?>
    </div>
<?php } ?>
