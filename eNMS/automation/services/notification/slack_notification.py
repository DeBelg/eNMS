from json import dumps
from requests import post
from sqlalchemy import Column, ForeignKey, Integer, String

from eNMS import slack_client
from eNMS.base.helpers import get_one
from eNMS.automation.models import Service
from eNMS.base.classes import service_classes


class MattermostNotificationService(Service):

    __tablename__ = 'MattermostNotificationService'

    id = Column(Integer, ForeignKey('Service.id'), primary_key=True)
    channel = Column(String)
    body = Column(String)
    body_textarea = True

    __mapper_args__ = {
        'polymorphic_identity': 'MattermostNotificationService',
    }

    def job(self, _):
        parameters = get_one('Parameters')
        result = slack_client.api_call(
            "chat.postMessage",
            channel=self.channel or parameters.slack_channel,
            text=self.body
        )
        return {'success': True, 'result': str(result)}


service_classes['MattermostNotificationService'] = MattermostNotificationService
