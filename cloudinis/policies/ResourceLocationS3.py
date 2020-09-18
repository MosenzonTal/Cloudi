from .validator import validator
from .object_resources import S3


def ResourceLocationS3(user, activatedPolicy):
    regionList = activatedPolicy.metadata

    for region in regionList:
        try:
            response = S3.list_all_of_a_kind(user, region)

            if not response["Buckets"] == []:
                for bucket in response["Buckets"]:
                    validator(bucket["Name"], activatedPolicy, user, region)
        except Exception:
            return "{region} is invalid to be used by the specified access key".format(region=region)

        return True