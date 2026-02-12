from tsa_cities import main, my_cities, create_cities_dataframe
import pytest

# create a list of cities
city_list = my_cities("Delhi", "Agra", "Jaipur", "Varanasi")
# create a dataframe of cities and their latitudes and longitudes
df = create_cities_dataframe(city_list)


@pytest.mark.slow
def test_my_cities():
    """Test my_cities function"""
    assert my_cities("Delhi", "Agra", "Jaipur", "Varanasi") == [
        "Delhi", "Agra", "Jaipur", "Varanasi"
    ]


@pytest.mark.slow
def test_main():
    """Test main function"""
    assert main(count=1) == None