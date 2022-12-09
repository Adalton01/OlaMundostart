 <?php
    for ($i = 1; $i <= 10; $i++) { ?>
        <div>

            <h2>Tabuada <?php echo $i ?></h2>
            <?php for ($j = 1; $j <= 10; $j++) { ?>
                <?php echo $i ?>x
                <?php echo $j ?>=
                <?php echo $i * $j ?> <br>




            <?php } ?>
        </div>
    <?php } ?>
