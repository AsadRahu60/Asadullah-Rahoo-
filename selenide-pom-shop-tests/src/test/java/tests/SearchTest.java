package tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import pages.HomePage;
import pages.SearchResultsPage;

public class SearchTest extends BaseTest {

    @Test
    @Tag("smoke")
    @DisplayName("Search shows results")
    void searchShowsResults() {
        HomePage home = new HomePage().openHome();
        SearchResultsPage results = home.searchFor("Mac");
        results.shouldShowResults();
    }
}
