package pages;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.page;

public class HomePage extends BasePage {
    private final String searchInput = "input[name='search']";
    private final String searchButton = "button.btn.btn-default.btn-lg";
    private final String cartLink = "#top-links a[title='Shopping Cart']";

    public HomePage openHome() {
        open("https://demo.opencart.com/");
        return this;
    }

    public SearchResultsPage searchFor(String term) {
        $(searchInput).setValue(term);
        $(searchButton).click();
        return page(SearchResultsPage.class);
    }

    public CartPage goToCart() {
        $(cartLink).click();
        return page(CartPage.class);
    }
}
