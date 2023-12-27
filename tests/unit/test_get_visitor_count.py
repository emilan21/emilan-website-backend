import unittest
from unittest import mock


class TestSampleLambda(unittest.TestCase):
    # Setting the default AWS region environment variable required by the Python SDK boto3
    with mock.patch.dict('os.environ', {'AWS_REGION': 'us-east-1'}):
        from visit_count.get_visit_count import lambda_handler

        # Mock call to S3 to read file
        def mocked_get_visit_count(self, bKey):
            return
