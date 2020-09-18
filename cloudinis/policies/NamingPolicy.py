import re
from .validator import validator
from .object_resources import EC2


def NamingPolicy(user, activatedPolicy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]

    if len(activatedPolicy.metadata) > 1 or (' ' in activatedPolicy.metadata[0]):
        return "An error occurred for the given Regex pattern"

    for region in regionList:
        response = EC2.list_all_of_a_kind(user, region)

        if not response == []:
            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    if not instance['State']['Name'] == 'terminated':
                        tags = EC2.list_tags(instance, user, region)
                        if tags is False:
                            return "Name tag does not exist on {instance}".format(instance=instance["InstanceId"])

                        if not 'Name' in tags:
                            return "Name tag does not exist on {instance}".format(instance=instance["InstanceId"])
                        else:
                            if not re.search(activatedPolicy.metadata[0], tags['Name']):
                                validator(instance["InstanceId"], activatedPolicy, user, region)
    return True