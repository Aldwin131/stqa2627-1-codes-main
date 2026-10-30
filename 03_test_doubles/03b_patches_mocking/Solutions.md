### Solution to step 1

```py
@patch('test_imdb.IMDb.search_titles')
def test_search_by_title(self, imdb_mock):
    """Test searching by title"""
    imdb_mock.return_value = IMDB_DATA["GOOD_SEARCH"]
    imdb = IMDb("fake_valid_api_key")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertIsNone(results["errorMessage"])
    self.assertIsNotNone(results["results"])
    self.assertEqual(results["results"][0]["id"], "tt1375666")
```

### Solution to step 2

```py
@patch('models.imdb.requests.get')
def test_search_by_title(self, imdb_mock):
    """Test searching by title"""
    imdb_mock.return_value = Mock(
        spec=Response,
        status_code=200,
        json=Mock(return_value=IMDB_DATA["GOOD_SEARCH"])
    )
    imdb = IMDb("fake_valid_api_key")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertIsNone(results["errorMessage"])
    self.assertIsNotNone(results["results"])
    self.assertEqual(results["results"][0]["id"], "tt1375666")
```

### Solution to Step 3

```py
@patch('models.imdb.requests.get')
def test_search_with_no_results(self, imdb_mock):
    """Test searching with no results"""
    imdb_mock.return_value = Mock(status_code=404)
    imdb = IMDb("fake_valid_api_key")
    results = imdb.search_titles("Bambi")
    self.assertEqual(results, {})
```

### Solution to Step 4

```py
@patch('models.imdb.requests.get')
def test_search_by_title_failed(self, imdb_mock):
    """Test searching by title failed"""
    imdb_mock.return_value = Mock(
        spec=Response,
        status_code=200, 
        json=Mock(return_value=IMDB_DATA["INVALID_API"])
    )
    imdb = IMDb("fake_valid_api_key")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertEqual(results["errorMessage"], "Invalid API Key")
```

### Solution to Step 5

```py
@patch('models.imdb.requests.get')
def test_movie_ratings(self, imdb_mock):
    """Test movie Ratings"""
    imdb_mock.return_value = Mock(
        spec=Response,
        status_code=200, 
        json=Mock(return_value=IMDB_DATA["GOOD_RATING"])
    )
    imdb = IMDb("fake_valid_api_key")
    results = imdb.movie_ratings("tt1375666")
    self.assertIsNotNone(results)
    self.assertEqual(results["title"], "Bambi")
    self.assertEqual(results["filmAffinity"], 3)
    self.assertEqual(results["rottenTomatoes"], 5)
```
