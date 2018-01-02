from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    '''
    Record all account information.
    '''
    accountId = models.AutoField(primary_key=True, unique=True)
    phoneNumber = models.CharField(max_length=45, unique=True)
    accountCreateDate = models.DateTimeField(null=True, auto_now_add=True)
    # accountStatus = models.CharField(max_length=45)
    # email = models.EmailField(max_length=45, unique=True, null=True)
    # accountPhoneNumber = models.CharField(max_length=45, unique=True, null=True)
    # accountCreateDate = models.DateTimeField(auto_now_add=True, null=True)
    # accountUpdateDate = models.DateTimeField(auto_now=True, null=True)
    # accountLevel = models.CharField(max_length=45, null=True)
    # password = models.CharField(max_length=45)
    # USERNAME_FIELD = 'accountName'
    # EMAIL_FIELD = 'email'
    # REQUIRED_FIELDS = ''
    class Meta:
        db_table = 'account'

class TaskCategory(models.Model):
    '''
    Record task types.
    '''
    taskCategoryId = models.AutoField(primary_key=True, unique=True)
    taskCategoryName = models.CharField(max_length=45)
    taskCategoryCreateDate = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'task_category'

class OriginalFile(models.Model):
    '''
    Record information of files to label.
    '''
    originalFileId = models.AutoField(primary_key=True, unique=True)
    originalFileName = models.CharField(max_length=45, unique=True)
    originalFileOwner = models.CharField(max_length=45)
    originalFileCreateDate = models.DateTimeField(auto_now_add=True)
    originalFileStatus = models.CharField(max_length=45)
    originalFileText = models.TextField()
    class Meta:
        db_table = 'original_file'

class EntityPool(models.Model):
    '''
    Record definition of all entity type.
    '''
    entityId = models.AutoField(primary_key=True, unique=True)
    entityName = models.CharField(unique=True, max_length=45)
    entityColor = models.CharField(max_length=45)
    entityShortcur = models.CharField(max_length=45)
    TaskCategory_taskcategoryId = models.IntegerField()
    class Meta:
        db_table = 'entity_pool'

class Task(models.Model):
    '''
    Record all tasks.
    '''
    taskId = models.AutoField(primary_key=True, unique=True)
    taskName = models.CharField(max_length=255, unique=True)
    taskCreateDate = models.DateTimeField(auto_now_add=True)
    taskStatus = models.CharField(max_length=45)
    taskCategory_TaskCategoryID = models.ForeignKey(TaskCategory, on_delete=None)
    class Meta:
        db_table = 'task'

class LabelResultFile(models.Model):
    '''
    Record labeled result information.
    '''
    labelResultFileId = models.AutoField(primary_key=True, unique=True)
    labelResultFileName = models.CharField(max_length=255, unique=True)
    labelResultFileCreateDate = models.DateTimeField(auto_now_add=True)
    labelResultFileEditor = models.CharField(max_length=45)
    labelResultFileStatus= models.CharField(max_length=45)
    labelResultFileText = models.TextField()
    class Meta:
        db_table = 'label_result_file'

class RelationPool(models.Model):
    '''
    Record relation definition
    '''
    relationId = models.AutoField(primary_key=True, unique=True)
    relationName = models.CharField(max_length=45, unique=True)
    relationColor = models.CharField(max_length=45)
    relationShortcut = models.CharField(max_length=45)
    taskCategory_taskCategoryId = models.ForeignKey(TaskCategory, on_delete=None)
    class Meta:
        db_table = 'relation_pool'

class AccountTaskAssociate(models.Model):
    '''
    join table for Account, Task, OriginalFile, LabelResultFile
    '''
    accountTaskAssociateId = models.AutoField(primary_key=True, unique=True)
    account_accountId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=None)
    task_taskId = models.ForeignKey(Task, on_delete=None)
    originalFile_originalFileId = \
        models.ForeignKey(OriginalFile, on_delete=None, null=True)
    labelResultFile_originalLabelResultFileId = \
        models.ForeignKey(LabelResultFile, on_delete=None, null=True, related_name='originalResult')
    labelResultFile_updatedLabelResultFileId = \
        models.ForeignKey(LabelResultFile, on_delete=None, null=True, unique=True, related_name='updatedResult')
    class Meta:
        db_table = 'account_task_associate'
