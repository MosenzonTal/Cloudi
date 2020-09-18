from .validator import validator
from .object_resources import EC2

def ResourceLocationEC2(user, activatedPolicy):
    regionList = activatedPolicy.metadata

    for region in regionList:
        try:
            response = EC2.list_all_of_a_kind(user, region)

            if not response == []:
                for reservation in response['Reservations']:
                    for instance in reservation['Instances']:
                        if not instance['State']['Name'] == 'terminated':
                            validator(instance["InstanceId"], activatedPolicy, user, region)
        except Exception:
            return "{region} is invalid to be used by the specified access key".format(region=region)

    return True