package modulos.produto;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

import java.net.MalformedURLException;
import java.net.URL;

@DisplayName("Testes Modulo de Produtos")
public class ProdutoTest {
    @DisplayName("Validaçao do Produto")
    @Test
    public  void testValidacaoDoProduto() throws MalformedURLException {
        DesiredCapabilities capacidades = new DesiredCapabilities();
        capacidades.setCapability("deviceName","Google Pixel 3_1");
        capacidades.setCapability("platform","Android");
        capacidades.setCapability("udid","127.0.0.1:6555");
        capacidades.setCapability("appPackage","com.lojinha");
        capacidades.setCapability("appActivity","com.lojinha.ui.MainActivity");
        capacidades.setCapability("app","\"C:\\Users\\adalt\\OneDrive\\Área de Trabalho\\Nova pasta (3)\\lojinha-nativa.apk\"");

        new RemoteWebDriver(new URL("http://127.0.0.1:4723/wd/hub"),capacidades);

    }
}
