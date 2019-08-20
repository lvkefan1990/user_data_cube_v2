# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CellBasicInfo(models.Model):
    cellid = models.BigAutoField(db_column='CELLID', primary_key=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    local_area = models.CharField(db_column='LOCAL_AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cell_name = models.CharField(db_column='CELL_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cell_grid = models.CharField(db_column='CELL_GRID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    azimuth = models.FloatField(db_column='AZIMUTH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cell_basic_info'


class CellParaTable(models.Model):
    cellid = models.BigIntegerField(db_column='CELLID', primary_key=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cell_name = models.CharField(db_column='CELL_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enodeb_id = models.IntegerField(db_column='ENODEB_ID', blank=True, null=True)  # Field name made lowercase.
    cell_id = models.IntegerField(db_column='CELL_ID', blank=True, null=True)  # Field name made lowercase.
    factory = models.CharField(db_column='FACTORY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cover_type = models.CharField(db_column='COVER_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cover_fomat = models.CharField(db_column='COVER_FOMAT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    earfcn = models.CharField(db_column='EARFCN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pci = models.CharField(db_column='PCI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tac = models.CharField(db_column='TAC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mod3 = models.CharField(db_column='MOD3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mod3_group = models.CharField(db_column='MOD3_GROUP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cell_para_table'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FieldSumma(models.Model):
    fieldid = models.AutoField(db_column='FIELDID', primary_key=True)  # Field name made lowercase.
    field_name = models.CharField(db_column='FIELD_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_table_name = models.CharField(db_column='FIELD_TABLE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fielddesc = models.CharField(db_column='FIELDDESC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'field_summa'


class RoundsLog(models.Model):
    rounds = models.CharField(max_length=10, blank=True, null=True)
    sdate = models.DateField(blank=True, null=True)
    count_num = models.BigIntegerField(blank=True, null=True)
    start_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rounds_log'


class RoundsMsisdnRelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', max_length=15)  # Field name made lowercase.
    if_tac_imei_relation = models.IntegerField()
    if_usr_app_pecpt = models.IntegerField()
    if_usr_app_rank = models.IntegerField()
    if_usr_basic_info = models.IntegerField()
    if_usr_call_pecpt = models.IntegerField()
    if_usr_complt_record = models.IntegerField()
    if_usr_core_pecpt = models.IntegerField()
    if_usr_cover_pecpt = models.IntegerField()
    if_usr_ete_pecpt = models.IntegerField()
    if_usr_expenses = models.IntegerField()
    if_usr_score_return = models.IntegerField()
    if_usr_speed_pecpt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rounds_msisdn_relation'


class SelectSumma(models.Model):
    selectid = models.AutoField(db_column='SELECTID', primary_key=True)  # Field name made lowercase.
    s_table = models.CharField(db_column='S_TABLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    s_field = models.CharField(db_column='S_FIELD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    s_where = models.CharField(db_column='S_WHERE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    s_statement = models.CharField(db_column='S_STATEMENT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'select_summa'


class TableSumma(models.Model):
    tableid = models.AutoField(db_column='TABLEID', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TABLENAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tabledesc = models.CharField(db_column='TABLEDESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.IntegerField(db_column='FIELDNUMBER', blank=True, null=True)  # Field name made lowercase.
    relev_field_name = models.CharField(db_column='RELEV_FIELD_NAME', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table_summa'


class TacImeiRelation(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tac_imei_relation'
        unique_together = (('msisdn', 'rounds'),)


class TestappUserinfo(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    last_time = models.DateTimeField()
    datastatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'testapp_userinfo'


class UsrAppPecpt(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    top1_app_name = models.CharField(db_column='TOP1_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top1_sp_delay = models.FloatField(db_column='TOP1_SP_DELAY', blank=True, null=True)  # Field name made lowercase.
    top1_b1_speed = models.FloatField(db_column='TOP1_B1_SPEED', blank=True, null=True)  # Field name made lowercase.
    top1_b2_speed = models.FloatField(db_column='TOP1_B2_SPEED', blank=True, null=True)  # Field name made lowercase.
    top1_b3_speed = models.FloatField(db_column='TOP1_B3_SPEED', blank=True, null=True)  # Field name made lowercase.
    top2_app_name = models.CharField(db_column='TOP2_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top2_sp_delay = models.FloatField(db_column='TOP2_SP_DELAY', blank=True, null=True)  # Field name made lowercase.
    top2_b1_speed = models.FloatField(db_column='TOP2_B1_SPEED', blank=True, null=True)  # Field name made lowercase.
    top2_b2_speed = models.FloatField(db_column='TOP2_B2_SPEED', blank=True, null=True)  # Field name made lowercase.
    top2_b3_speed = models.FloatField(db_column='TOP2_B3_SPEED', blank=True, null=True)  # Field name made lowercase.
    top3_app_name = models.CharField(db_column='TOP3_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top3_sp_delay = models.FloatField(db_column='TOP3_SP_DELAY', blank=True, null=True)  # Field name made lowercase.
    top3_b1_speed = models.FloatField(db_column='TOP3_B1_SPEED', blank=True, null=True)  # Field name made lowercase.
    top3_b2_speed = models.FloatField(db_column='TOP3_B2_SPEED', blank=True, null=True)  # Field name made lowercase.
    top3_b3_speed = models.FloatField(db_column='TOP3_B3_SPEED', blank=True, null=True)  # Field name made lowercase.
    top4_app_name = models.CharField(db_column='TOP4_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top4_sp_delay = models.FloatField(db_column='TOP4_SP_DELAY', blank=True, null=True)  # Field name made lowercase.
    top4_b1_speed = models.FloatField(db_column='TOP4_B1_SPEED', blank=True, null=True)  # Field name made lowercase.
    top4_b2_speed = models.FloatField(db_column='TOP4_B2_SPEED', blank=True, null=True)  # Field name made lowercase.
    top4_b3_speed = models.FloatField(db_column='TOP4_B3_SPEED', blank=True, null=True)  # Field name made lowercase.
    top5_app_name = models.CharField(db_column='TOP5_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top5_sp_delay = models.FloatField(db_column='TOP5_SP_DELAY', blank=True, null=True)  # Field name made lowercase.
    top5_b1_speed = models.FloatField(db_column='TOP5_B1_SPEED', blank=True, null=True)  # Field name made lowercase.
    top5_b2_speed = models.FloatField(db_column='TOP5_B2_SPEED', blank=True, null=True)  # Field name made lowercase.
    top5_b3_speed = models.FloatField(db_column='TOP5_B3_SPEED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_app_pecpt'
        unique_together = (('msisdn', 'rounds'),)


class UsrAppRank(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    top1_app_name = models.CharField(db_column='TOP1_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top1_session = models.BigIntegerField(db_column='TOP1_SESSION', blank=True, null=True)  # Field name made lowercase.
    top1_data = models.BigIntegerField(db_column='TOP1_DATA', blank=True, null=True)  # Field name made lowercase.
    top2_app_name = models.CharField(db_column='TOP2_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top2_session = models.BigIntegerField(db_column='TOP2_SESSION', blank=True, null=True)  # Field name made lowercase.
    top2_data = models.BigIntegerField(db_column='TOP2_DATA', blank=True, null=True)  # Field name made lowercase.
    top3_app_name = models.CharField(db_column='TOP3_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top3_session = models.BigIntegerField(db_column='TOP3_SESSION', blank=True, null=True)  # Field name made lowercase.
    top3_data = models.BigIntegerField(db_column='TOP3_DATA', blank=True, null=True)  # Field name made lowercase.
    top4_app_name = models.CharField(db_column='TOP4_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top4_session = models.BigIntegerField(db_column='TOP4_SESSION', blank=True, null=True)  # Field name made lowercase.
    top4_data = models.BigIntegerField(db_column='TOP4_DATA', blank=True, null=True)  # Field name made lowercase.
    top5_app_name = models.CharField(db_column='TOP5_APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    top5_session = models.BigIntegerField(db_column='TOP5_SESSION', blank=True, null=True)  # Field name made lowercase.
    top5_data = models.BigIntegerField(db_column='TOP5_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_app_rank'
        unique_together = (('msisdn', 'rounds'),)


class UsrBasicInfo(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    area1 = models.CharField(db_column='AREA1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    overlay_area = models.CharField(db_column='OVERLAY_AREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    star_type = models.CharField(db_column='STAR_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(db_column='START_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    online_time = models.IntegerField(db_column='ONLINE_TIME', blank=True, null=True)  # Field name made lowercase.
    attrib_addr = models.CharField(db_column='ATTRIB_ADDR', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_basic_info'
        unique_together = (('msisdn', 'rounds'),)


class UsrCallPecpt(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    paging_rate = models.FloatField(db_column='PAGING_RATE', blank=True, null=True)  # Field name made lowercase.
    dc_rate = models.FloatField(db_column='DC_RATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_call_pecpt'
        unique_together = (('msisdn', 'rounds'),)


class UsrCompltRecord(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    if_risk_user = models.IntegerField(db_column='IF_RISK_USER', blank=True, null=True)  # Field name made lowercase.
    policy_product = models.CharField(db_column='POLICY_PRODUCT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    if_complaint_user = models.IntegerField(db_column='IF_COMPLAINT_USER', blank=True, null=True)  # Field name made lowercase.
    reason1 = models.CharField(db_column='REASON1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    reason2 = models.CharField(db_column='REASON2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    business = models.CharField(db_column='BUSINESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    if_discontent_user = models.IntegerField(db_column='IF_DISCONTENT_USER', blank=True, null=True)  # Field name made lowercase.
    rfd = models.CharField(db_column='RFD', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dfw = models.CharField(db_column='DFW', max_length=500, blank=True, null=True)  # Field name made lowercase.
    college_usr = models.CharField(db_column='COLLEGE_USR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    over_packges_user = models.CharField(db_column='OVER_PACKGES_USER', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_complt_record'
        unique_together = (('msisdn', 'rounds'),)


class UsrCorePecpt(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    bad_rip_rate = models.FloatField(db_column='BAD_RIP_RATE', blank=True, null=True)  # Field name made lowercase.
    ho_rate = models.FloatField(db_column='HO_RATE', blank=True, null=True)  # Field name made lowercase.
    sr_rate = models.FloatField(db_column='SR_RATE', blank=True, null=True)  # Field name made lowercase.
    attach_rate = models.FloatField(db_column='ATTACH_RATE', blank=True, null=True)  # Field name made lowercase.
    pdn_rate = models.FloatField(db_column='PDN_RATE', blank=True, null=True)  # Field name made lowercase.
    initial_rate = models.FloatField(db_column='INITIAL_RATE', blank=True, null=True)  # Field name made lowercase.
    tau_rate = models.FloatField(db_column='TAU_RATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_core_pecpt'
        unique_together = (('msisdn', 'rounds'),)


class UsrCoverPecpt(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    sum_point = models.IntegerField(db_column='SUM_POINT', blank=True, null=True)  # Field name made lowercase.
    poor_point = models.IntegerField(db_column='POOR_POINT', blank=True, null=True)  # Field name made lowercase.
    weak_point = models.IntegerField(db_column='WEAK_POINT', blank=True, null=True)  # Field name made lowercase.
    avg_rsrp = models.FloatField(db_column='AVG_RSRP', blank=True, null=True)  # Field name made lowercase.
    mr_rate_100 = models.FloatField(db_column='MR_RATE_100', blank=True, null=True)  # Field name made lowercase.
    mr_rate = models.FloatField(db_column='MR_RATE', blank=True, null=True)  # Field name made lowercase.
    off_rate = models.FloatField(db_column='OFF_RATE', blank=True, null=True)  # Field name made lowercase.
    bad_phr_rate = models.FloatField(db_column='BAD_PHR_RATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_cover_pecpt'
        unique_together = (('msisdn', 'rounds'),)


class UsrEtePecpt(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    http_res_rate = models.FloatField(db_column='HTTP_RES_RATE', blank=True, null=True)  # Field name made lowercase.
    http_att = models.FloatField(db_column='HTTP_ATT', blank=True, null=True)  # Field name made lowercase.
    http_res_delay = models.FloatField(db_column='HTTP_RES_DELAY', blank=True, null=True)  # Field name made lowercase.
    tcp_core_rate = models.FloatField(db_column='TCP_CORE_RATE', blank=True, null=True)  # Field name made lowercase.
    tcp_core_delay = models.FloatField(db_column='TCP_CORE_DELAY', blank=True, null=True)  # Field name made lowercase.
    tcp_radio_rate = models.FloatField(db_column='TCP_RADIO_RATE', blank=True, null=True)  # Field name made lowercase.
    tcp_radio_delay = models.FloatField(db_column='TCP_RADIO_DELAY', blank=True, null=True)  # Field name made lowercase.
    tcp_dl_re_rate = models.FloatField(db_column='TCP_DL_RE_RATE', blank=True, null=True)  # Field name made lowercase.
    tcp_ul_re_rate = models.FloatField(db_column='TCP_UL_RE_RATE', blank=True, null=True)  # Field name made lowercase.
    tcp_re_rate = models.FloatField(db_column='TCP_RE_RATE', blank=True, null=True)  # Field name made lowercase.
    page_res_delay = models.FloatField(db_column='PAGE_RES_DELAY', blank=True, null=True)  # Field name made lowercase.
    page_res_session = models.FloatField(db_column='PAGE_RES_SESSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_ete_pecpt'
        unique_together = (('msisdn', 'rounds'),)


class UsrExpenses(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    packages_name = models.CharField(db_column='PACKAGES_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    up_500m_user = models.CharField(db_column='UP_500M_USER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flows = models.CharField(db_column='FLOWS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    college_user = models.CharField(db_column='COLLEGE_USER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    over_packges_user = models.CharField(db_column='OVER_PACKGES_USER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last3m_avg_arpu = models.FloatField(db_column='LAST3M_AVG_ARPU', blank=True, null=True)  # Field name made lowercase.
    arpu_rank = models.BigIntegerField(db_column='ARPU_RANK', blank=True, null=True)  # Field name made lowercase.
    if_30_arpu = models.IntegerField(db_column='IF_30_ARPU', blank=True, null=True)  # Field name made lowercase.
    last3m_avg_dou = models.FloatField(db_column='LAST3M_AVG_DOU', blank=True, null=True)  # Field name made lowercase.
    dou_rank = models.BigIntegerField(db_column='DOU_RANK', blank=True, null=True)  # Field name made lowercase.
    if_30_dou = models.IntegerField(db_column='IF_30_DOU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_expenses'
        unique_together = (('msisdn', 'rounds'),)


class UsrLocation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', max_length=255)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    cell = models.IntegerField(db_column='CELL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_location'


class UsrLogin(models.Model):
    user_name = models.CharField(primary_key=True, max_length=40)
    password = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usr_login'


class UsrResidentCell(models.Model):
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    enodeb_id = models.IntegerField(db_column='ENODEB_ID', blank=True, null=True)  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_resident_cell'


class UsrScoreReturn(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    score_usr_worth = models.FloatField(db_column='SCORE_USR_WORTH', blank=True, null=True)  # Field name made lowercase.
    score_usr_cover_pecpt = models.FloatField(db_column='SCORE_USR_COVER_PECPT', blank=True, null=True)  # Field name made lowercase.
    score_usr_speed_pecpt = models.FloatField(db_column='SCORE_USR_SPEED_PECPT', blank=True, null=True)  # Field name made lowercase.
    score_usr_ete_pecpt = models.FloatField(db_column='SCORE_USR_ETE_PECPT', blank=True, null=True)  # Field name made lowercase.
    score_usr_sensitivity = models.FloatField(db_column='SCORE_USR_SENSITIVITY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_score_return'
        unique_together = (('msisdn', 'rounds'),)


class UsrSpeedPecpt(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    rounds = models.CharField(db_column='ROUNDS', max_length=4)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', primary_key=True, max_length=20)  # Field name made lowercase.
    dl_speed = models.FloatField(db_column='DL_SPEED', blank=True, null=True)  # Field name made lowercase.
    bp_dl_speed = models.FloatField(db_column='BP_DL_SPEED', blank=True, null=True)  # Field name made lowercase.
    bp_dl_data = models.FloatField(db_column='BP_DL_DATA', blank=True, null=True)  # Field name made lowercase.
    bp_dl_dura = models.FloatField(db_column='BP_DL_DURA', blank=True, null=True)  # Field name made lowercase.
    ul_speed = models.FloatField(db_column='UL_SPEED', blank=True, null=True)  # Field name made lowercase.
    bp_ul_speed = models.FloatField(db_column='BP_UL_SPEED', blank=True, null=True)  # Field name made lowercase.
    sp_dl_delay = models.FloatField(db_column='SP_DL_DELAY', blank=True, null=True)  # Field name made lowercase.
    sp_ul_delay = models.FloatField(db_column='SP_UL_DELAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usr_speed_pecpt'
        unique_together = (('msisdn', 'rounds'),)
