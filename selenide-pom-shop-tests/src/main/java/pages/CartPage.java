package pages;

import com.codeborne.selenide.Condition;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;

public class CartPage {
    private final String cartRows = "div#content table tbody tr";
    private final String cartTable = "div#content table";

    public CartPage shouldContainItems() {
        $(cartTable).shouldBe(Condition.visible);
        $$(cartRows).shouldHaveSizeGreaterThan(0);
        return this;
    }
}
