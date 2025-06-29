import unittest
from unittest.mock import patch, Mock
from producteca.config.config import ConfigProducteca
from producteca.sales_orders.search_sale_orders import SearchSalesOrder, SearchSalesOrderParams


class TestSearchSalesOrder(unittest.TestCase):
    def setUp(self):
        self.config = ConfigProducteca(
            token="test_client_id",
            api_key="test_client_secret",
        )
        self.params = SearchSalesOrderParams(
            top=10,
            skip=0,
            filter="status eq 'confirmed'"
        )

    @patch('requests.get')
    def test_search_saleorder_success(self, mock_get):
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {
            "count": 1,
            "results": [{
                "id": "123",
                "status": "confirmed",
                "lines": [],
                "payments": [],
                "shipments": [],
                "integrations": [],
                "codes": [],
                "integration_ids": [],
                "product_names": [],
                "skus": [],
                "tags": [],
                "brands": []
            }]
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response, status_code = SearchSalesOrder.search_saleorder(self.config, self.params)
        
        # Validate response
        self.assertEqual(status_code, 200)
        self.assertEqual(response["count"], 1)
        self.assertEqual(len(response["results"]), 1)
        self.assertEqual(response["results"][0]["id"], "123")

        # Verify the request was made with correct parameters
        expected_url = f"{self.config.get_endpoint(SearchSalesOrder.endpoint)}?$filter={self.params.filter}&top={self.params.top}&skip={self.params.skip}"
        mock_get.assert_called_once_with(
            expected_url,
            headers=self.config.headers
        )

    @patch('requests.get')
    def test_search_saleorder_error(self, mock_get):
        # Mock error response
        mock_response = Mock()
        mock_response.json.return_value = {"error": "Invalid request"}
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        response, status_code = SearchSalesOrder.search_saleorder(self.config, self.params)
        
        # Validate error response
        self.assertEqual(status_code, 400)
        self.assertEqual(response["error"], "Invalid request")


if __name__ == '__main__':
    unittest.main()
