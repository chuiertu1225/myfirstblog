from django.db import models
import shortuuid
# Create your models here.
from django.utils.timezone import now


class BaseModel(models.Model):
    uuid = models.CharField(
        'ID',
        max_length=22,
        primary_key=True,
        default=shortuuid.uuid(),
        editable=False
    )
    created_time = models.DateTimeField('创建时间',auto_now_add=now)
    last_mod_time = models.DateTimeField('修改时间',auto_now=now)

    DEL_STATE = ((0,'已删除'),(1,'默认'))
    del_state = models.PositiveIntegerField('删除状态',choices=DEL_STATE, default=1, db_index=True)
    class Meta:
        abstract = True