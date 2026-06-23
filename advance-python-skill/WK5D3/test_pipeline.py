from unittest.mock import MagicMock
from pipeline import LogFetcher, clean_and_extract

def test_successful_log_ingestion_pipeline():
    """
    Test that our pipeline can fetch, clean, and extract user IDs 
    without hitting a real S3 bucket.
    """
    # -------------------------------------------------------------
    # 1. ARRANGE: Set up our fake infrastructure (The Mock)
    # -------------------------------------------------------------
    mock_client = MagicMock()
    mock_body = MagicMock()
    
    # Fake the binary data that would normally come from S3
    fake_s3_bytes = b"  [ERROR] USER_ID:102938 - Timeout \n  [INFO] USER_ID:555444 - OK "
    
    # Tell the mock body what to return when .read() is called
    mock_body.read.return_value = fake_s3_bytes
    
    # Tell the mock client what to return when .get_object() is called
    # It must return a dictionary with our mock_body inside it
    mock_client.get_object.return_value = {"Body": mock_body}

    # -------------------------------------------------------------
    # 2. ACT: Run the actual production code using the mock
    # -------------------------------------------------------------
    fetcher = LogFetcher(client=mock_client)
    raw_logs = fetcher.fetch_raw_logs(bucket_name="my-production-bucket")
    parsed_user_ids = clean_and_extract(raw_logs)

    # -------------------------------------------------------------
    # 3. ASSERT: Verify the results are perfectly accurate
    # -------------------------------------------------------------
    # Check that the logic extracted the correct IDs
    assert parsed_user_ids == ["102938", "555444"]
    
    # Crucial Data Eng Check: Verify our code actually called the cloud client 
    # with the correct parameters!
    mock_client.get_object.assert_called_once_with(Bucket="my-production-bucket")