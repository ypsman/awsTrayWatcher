import boto
from boto.ec2.cloudwatch import MetricAlarm
from CREDENTIALS import *

class Alarmgetter():
    def __init__(self):
        self.cw = boto.ec2.cloudwatch.connect_to_region(REGION,
        aws_access_key_id=KEYID,
        aws_secret_access_key=KEYSECRET)

    def get_OK(self ,alarmtype):
        self.get_OKS = self.cw.describe_alarms(state_value='OK')
        if alarmtype == "amount":
            amount_OKS = len(self.get_OKS)
            return amount_OKS
        elif alarmtype == "alarms":
            return self.get_OKS

    def get_ALARM(self, alarmtype):
        self.get_ALARMS = self.cw.describe_alarms(state_value='ALARM')
        if alarmtype == "amount":
            amount_ALARMS = len(self.get_ALARMS)
            return  amount_ALARMS #, self.get_ALARMS
        elif alarmtype == "alarms":
            return  self.get_ALARMS

    def get_INSU(self, alarmtype):
        self.get_INSUS = self.cw.describe_alarms(state_value='INSUFFICIENT_DATA')
        if alarmtype == "amount":
            amount_INSUS = len(self.get_INSUS)
            return  amount_INSUS #, self.get_ALARMS
        elif alarmtype == "alarms":
            return  self.get_INSUS
