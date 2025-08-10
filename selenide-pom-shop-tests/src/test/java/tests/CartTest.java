package tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import pages.CartPage;
import pages.HomePage;
import pages.SearchResultsPage;

public class CartTest extends BaseTest {

    @Test
    @Tag("regression")
    @DisplayName("Add product to cart and verify cart")
    void addProductToCartAndVerify() {
        HomePage home = new HomePage().openHome();
        SearchResultsPage results = home.searchFor("Mac");
        results.shouldShowResults()
               .addFirstResultToCart();
        CartPage cart = home.goToCart();
        cart.shouldContainItems();
    }
}
