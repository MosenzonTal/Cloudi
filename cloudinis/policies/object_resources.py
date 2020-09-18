import boto3


class Resource:
    @staticmethod
    def list_all_of_a_kind(user, region):
        raise NotImplementedError

    @staticmethod
    def destroy_resource(resource_id, user, region):
        raise NotImplementedError

    @staticmethod
    def list_tags(resource, user, region):
        raise NotImplementedError

    @staticmethod
    def list_tags_by_id(resource_id, user, region):
        raise NotImplementedError


class EC2(Resource):
    @staticmethod
    def list_all_of_a_kind(user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        return client.describe_instances()

    @staticmethod
    def destroy_resource(resource_id, user, region):
        client = boto3.resource('ec2', aws_access_key_id=user.access_key,
                                        aws_secret_access_key=user.secret_key,
                                        aws_session_token=user.session_token, region_name=region)
        client.instances.filter(InstanceIds=[resource_id]).terminate()

    @staticmethod
    def list_tags(resource, user, region):
        tags = {}
        try:
            for tag in resource["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        except:
            return False

        return tags

    @staticmethod
    def list_tags_by_id(resource_id, user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        resource = client.describe_instances(Filters=[{'Name': 'instance-id', 'Values': [resource_id]}])

        tags = {}
        try:
            for tag in resource["Reservations"][0]["Instances"][0]["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        except:
            return False

        return tags


class Volume(Resource):
    @staticmethod
    def list_all_of_a_kind(user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        return client.describe_volumes()

    @staticmethod
    def destroy_resource(resource_id, user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key,
                                        aws_secret_access_key=user.secret_key,
                                        aws_session_token=user.session_token, region_name=region)
        client.delete_volume(VolumeId=resource_id)

    @staticmethod
    def list_tags(resource, user, region):
        tags = {}
        try:
            for tag in resource["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        except:
            return False

        return tags

    @staticmethod
    def list_tags_by_id(resource_id, user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        resource = client.describe_volumes(Filters=[{'Name': 'volume-id', 'Values': [resource_id]}])

        tags = {}
        try:
            for tag in resource["Volumes"][0]["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        except:
            return False

        return tags


class S3(Resource):
    @staticmethod
    def list_all_of_a_kind(user, region):
        client = boto3.client('s3', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        return client.list_buckets()

    @staticmethod
    def destroy_resource(resource_id, user, region):
        client = boto3.resource('s3', aws_access_key_id=user.access_key,
                                        aws_secret_access_key=user.secret_key,
                                        aws_session_token=user.session_token, region_name=region)

        bucket = client.Bucket(resource_id)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()

    @staticmethod
    def list_tags(resource, user, region):
        tags = {}
        try:
            client = boto3.client('s3', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                                  aws_session_token=user.session_token, region_name=region)
            response = client.get_bucket_tagging(Bucket=resource["Name"])

            try:
                for tag in response["TagSet"]:
                    tags[tag["Key"]] = tag["Value"]
            except:
                return False
        except:
            return False

        return tags

    @staticmethod
    def list_tags_by_id(resource_id, user, region):
        tags = {}
        try:
            client = boto3.client('s3', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                                  aws_session_token=user.session_token, region_name=region)
            response = client.get_bucket_tagging(Bucket=resource_id)

            try:
                for tag in response["TagSet"]:
                    tags[tag["Key"]] = tag["Value"]
            except:
                return False
        except:
            return False

        return tags


class EIP(Resource):
    @staticmethod
    def list_all_of_a_kind(user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        return client.describe_addresses()

    @staticmethod
    def destroy_resource(resource_id, user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        client.release_address(AllocationId=resource_id)

    @staticmethod
    def list_tags(resource, user, region):
        tags = {}
        try:
            for tag in resource["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        except:
            return False

        return tags

    @staticmethod
    def list_tags_by_id(resource_id, user, region):
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        resource = client.describe_addresses(Filters=[{'Name': 'allocation-id', 'Values': [resource_id]}])

        tags = {}
        try:
            for tag in resource["Addresses"][0]["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        except:
            return False

        return tags