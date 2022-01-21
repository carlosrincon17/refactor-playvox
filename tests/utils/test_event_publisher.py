from mock import patch
from moto import mock_sns
import pytest

from src.utils.event_publisher.event_publisher_factory import EventPublisherFactory
from src.utils.event_publisher.event_publisher_interface import IEventPublisher
from src.utils.event_publisher.third_party.sns_aws_event_publisher import SNSAWSEventPublisher
from src.utils.event_publisher.third_party.sns_helper import SNSHelper
from src.utils.exceptions import MessageBrokerNotFound

@patch.object(SNSHelper, 'get_sns_client')
def test_event_publised_factory(fake_get_sns_client):
    fake_get_sns_client.return_value = mock_sns()
    event_publisher = EventPublisherFactory.get_event_publisher("SNS")
    assert isinstance(event_publisher, IEventPublisher)
    assert isinstance(event_publisher, SNSAWSEventPublisher)


@patch.object(SNSHelper, 'get_sns_client')
def test_event_publised_factory_not_allowed(fake_get_sns_client):
    with pytest.raises(MessageBrokerNotFound):
        fake_get_sns_client.return_value = mock_sns()
        event_publisher = EventPublisherFactory.get_event_publisher("SQS")
        assert isinstance(event_publisher, IEventPublisher)
        assert isinstance(event_publisher, SNSAWSEventPublisher)