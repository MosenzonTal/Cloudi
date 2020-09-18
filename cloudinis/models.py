from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, Group
from django.core.mail import send_mail
from django.conf import settings
from cloudinis.policies.object_resources import *


class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True)
    scan_status = models.CharField(max_length=500, default="None")
    last_scan_time = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            is_exist = CloudiniUser.objects.get(username="admin_"+self.name)
            if not is_exist:
                my_user = CloudiniUser.objects.create_user(username="admin_"+self.name, password="changeme",
                                            email="admin@{organization}.com".format(organization=self.name), isAdmin=True,
                                            access_key="changeme", secret_key="changeme", session_token="changeme")
                my_group = Group.objects.get(name='org_admins')
                my_user.groups.add(my_group)
                super().save(*args, **kwargs)
                my_user.organization = self
                my_user.save()
            else:
                super().save(*args, **kwargs)
        except:
            my_user = CloudiniUser.objects.create_user(username="admin_" + self.name, password="changeme",
                                                       email="admin@{organization}.com".format(organization=self.name),
                                                       isAdmin=True,
                                                       access_key="changeme", secret_key="changeme",
                                                       session_token="changeme")
            my_group = Group.objects.get(name='org_admins')
            my_user.groups.add(my_group)
            super().save(*args, **kwargs)
            my_user.organization = self
            my_user.save()

    def get_absolute_url(self):
        return reverse('profile')


class CloudiniUser(AbstractUser, models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None, null=True)
    isAdmin = models.BooleanField(default=False)
    access_key = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=50)
    session_token = models.CharField(max_length=400)

    class Meta:
        unique_together = ('username', 'email')

    def __str__(self):
        return self.username


class Policy(models.Model):
    name = models.CharField(max_length=40)
    affectedResources = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ActivatedPolicy(models.Model):
    CHOICES=(
        ("None", "None"),
        ("Notify", "Notify"),
        ("Delete", "Delete"),
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None, null=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    affectedResource = models.CharField(max_length=200 , verbose_name="Resource")
    metadata = ArrayField(models.CharField(max_length=200,),verbose_name="What to enforce")
    actionItem = models.CharField(max_length=200,choices=CHOICES, verbose_name="Action item")
    resourceTagToNotify = models.CharField(max_length=200, verbose_name="Tag to notify")

    def __str__(self):
        return "{}".format(self.policy)

    def get_absolute_url(self):
        return reverse('policies')

    def save(self, *args, **kwargs):
        self.affectedResource = self.policy.affectedResources
        super().save(*args, **kwargs)


class Violation(models.Model):
    connectedPolicy = models.ForeignKey(ActivatedPolicy, on_delete=models.CASCADE)
    resource_id = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) #TODO
    isChecked = models.BooleanField(default=False)
    isFixed = models.BooleanField(default=False)
    fixedDate = models.DateTimeField(default=None, null=True)

    def delete_me(self, user, region):
        kind = eval(self.connectedPolicy.affectedResource)
        kind.destroy_resource(self.resource_id, user, region)

    def notify(self, recipient):
        subject = 'Cloudini Alert'
        message = 'resource {resource_id} has been detected by {activatedPolicy} policy'.\
            format(resource_id=self.resource_id, activatedPolicy=self.connectedPolicy)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient, ]
        send_mail(subject, message, email_from, recipient_list)


    def get_recipient(self, user, region):
        admin_user = CloudiniUser.objects.get(username=str("admin_" + self.connectedPolicy.organization.name))
        kind = eval(self.connectedPolicy.affectedResource)
        tags = kind.list_tags_by_id(self.resource_id, user, region)
        if tags is False:
            return admin_user.email
        else:
            if self.connectedPolicy.resourceTagToNotify in list(tags.keys()):
                return tags[self.connectedPolicy.resourceTagToNotify]
            else:
                return admin_user.email
