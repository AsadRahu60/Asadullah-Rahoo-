package pages;

import com.codeborne.selenide.Condition;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;
import static com.codeborne.selenide.Selenide.page;

public class SearchResultsPage {
    private final String productTile = "div.product-layout";
    private final String firstAddToCart = "(//button[@data-original-title='Add to Cart'])[1]";
    private final String successAlert = "div.alert-success";

    public SearchResultsPage shouldShowResults() {
        $$(productTile).first().shouldBe(Condition.visible);
        return this;
    }

    public SearchResultsPage addFirstResultToCart() {
        $(firstAddToCart).click();
        $(successAlert).shouldBe(Condition.visible);
        return this;
    }

    public CartPage goToCartFromAlert() {
        // Optional: click on link inside success alert; fallback navigate via header
        return page(CartPage.class);
    }
}
