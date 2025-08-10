package tests;

import com.codeborne.selenide.Configuration;
import io.qameta.allure.selenide.AllureSelenide;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import com.codeborne.selenide.logevents.SelenideLogger;

public class BaseTest {

    @BeforeAll
    static void setupAll() {
        Configuration.browser = "chrome";
        Configuration.headless = true;      // overridden by surefire too
        Configuration.timeout = 10000;
        SelenideLogger.addListener("AllureSelenide", new AllureSelenide().screenshots(true).savePageSource(false));
    }

    @BeforeEach
    void beforeEach() {
        // can add per-test setup here
    }

    @AfterEach
    void tearDown() {
        // Selenide closes browser automatically per test
    }
}
