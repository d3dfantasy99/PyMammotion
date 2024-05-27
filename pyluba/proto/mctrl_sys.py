# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: pyluba/proto/mctrl_sys.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class Operation(betterproto.Enum):
    WRITE = 0
    READ = 1
    ERASE = 2


class OffPartId(betterproto.Enum):
    OFF_PART_DL_IMG = 0
    OFF_PART_UPDINFO_BACK = 1
    OFF_PART_UPDINFO = 2
    OFF_PART_NAKEDB = 3
    OFF_PART_FLASHDB = 4
    OFF_PART_UPD_APP_IMG = 5
    OFF_PART_UPD_BMS_IMG = 6
    OFF_PART_UPD_TMP_IMG = 7
    OFF_PART_DEV_INFO = 8
    OFF_PART_NAKEDB_BACK = 9
    OFF_PART_MAX = 10


class QCAppTestId(betterproto.Enum):
    QC_APP_ITEM_ON_CHARGESATSTION = 0
    QC_APP_TEST_X3_SPEAKER = 1
    QC_APP_TEST_STATIC_OBSTACLE_DETECTION = 2
    QC_APP_TEST_CHARGESTATION_TEMP = 3
    QC_APP_ITEM_KEY = 4
    QC_APP_TEST_BUMPER_FRONTLEFT = 5
    QC_APP_TEST_BUMPER_FRONTRIGHT = 6
    QC_APP_TEST_STOP = 7
    QC_APP_TEST_UNLOCK = 8
    QC_APP_TEST_BUZZ = 9
    QC_APP_TEST_LIFT = 10
    QC_APP_ITEM_SENEOR = 11
    QC_APP_TEST_ROLL_LEFT = 12
    QC_APP_TEST_ROLL_RIGHT = 13
    QC_APP_TEST_ULTRA_UNCOVER = 14
    QC_APP_TEST_ULTRA0_COVER = 15
    QC_APP_TEST_ULTRA1_COVER = 16
    QC_APP_TEST_ULTRA2_COVER = 17
    QC_APP_TEST_RAIN = 18
    QC_APP_ITEM_SQ = 19
    QC_APP_TEST_BLE_RSSI = 20
    QC_APP_TEST_SATELLITES_ROVER = 21
    QC_APP_TEST_SATELLITES_REF_STATION_L1 = 22
    QC_APP_TEST_SATELLITES_REF_STATION_L2 = 23
    QC_APP_TEST_SATELLITES_COMMON_VIEW = 24
    QC_APP_TEST_CNO_ROVER = 25
    QC_APP_TEST_CNO_REF_STATION = 26
    QC_APP_TEST_REF_STATION_LINK_STATUS = 27
    QC_APP_TEST_LOCATION_STATE = 28
    QC_APP_TEST_MAX = 29


class NetUsedType(betterproto.Enum):
    NET_USED_TYPE_NONE = 0
    NET_USED_TYPE_WIFI = 1
    NET_USED_TYPE_MNET = 2


class RptInfoType(betterproto.Enum):
    RIT_CONNECT = 0
    RIT_DEV_STA = 1
    RIT_RTK = 2
    RIT_DEV_LOCAL = 3
    RIT_WORK = 4
    RIT_FW_INFO = 5
    RIT_MAINTAIN = 6
    RIT_VISION_POINT = 7
    RIT_VIO = 8
    RIT_VISION_STATISTIC = 9


class RptAct(betterproto.Enum):
    RPT_START = 0
    RPT_STOP = 1
    RPT_KEEP = 2


@dataclass
class SysBatUp(betterproto.Message):
    bat_val: int = betterproto.int32_field(1)


@dataclass
class SysWorkState(betterproto.Message):
    device_state: int = betterproto.int32_field(1)
    charge_state: int = betterproto.int32_field(2)
    cm_hash: int = betterproto.int64_field(3)
    path_hash: int = betterproto.int64_field(4)


@dataclass
class SysSetTimeZone(betterproto.Message):
    time_stamp: int = betterproto.int32_field(1)
    time_area: int = betterproto.int32_field(2)


@dataclass
class SysSetDateTime(betterproto.Message):
    year: int = betterproto.int32_field(1)
    month: int = betterproto.int32_field(2)
    date: int = betterproto.int32_field(3)
    week: int = betterproto.int32_field(4)
    hours: int = betterproto.int32_field(5)
    minutes: int = betterproto.int32_field(6)
    seconds: int = betterproto.int32_field(7)
    time_zone: int = betterproto.int32_field(8)
    daylight: int = betterproto.int32_field(9)


@dataclass
class SysJobPlan(betterproto.Message):
    job_id: int = betterproto.int64_field(1)
    job_mode: int = betterproto.int32_field(2)
    rain_tactics: int = betterproto.int32_field(3)
    knife_height: int = betterproto.int32_field(4)


@dataclass
class SysDevErrCode(betterproto.Message):
    error_code: int = betterproto.int32_field(1)


@dataclass
class SysBoardType(betterproto.Message):
    board_type: int = betterproto.int32_field(1)


@dataclass
class SysSwVersion(betterproto.Message):
    board_type: int = betterproto.int32_field(1)
    version_len: int = betterproto.int32_field(2)


@dataclass
class SysDelJobPlan(betterproto.Message):
    device_id: str = betterproto.string_field(1)
    plan_id: str = betterproto.string_field(2)


@dataclass
class SysJobPlanTime(betterproto.Message):
    plan_id: int = betterproto.int64_field(1)
    start_job_time: int = betterproto.int32_field(2)
    end_job_time: int = betterproto.int32_field(3)
    time_in_day: int = betterproto.int32_field(4)
    job_plan_mode: int = betterproto.int32_field(5)
    job_plan_enable: int = betterproto.int32_field(6)
    week_day: List[int] = betterproto.int32_field(7)
    time_in_week_day: List[int] = betterproto.int32_field(8)
    every_day: int = betterproto.int32_field(9)
    job_plan: "SysJobPlan" = betterproto.message_field(10)


@dataclass
class SysMowInfo(betterproto.Message):
    device_state: int = betterproto.int32_field(1)
    bat_val: int = betterproto.int32_field(2)
    knife_height: int = betterproto.int32_field(3)
    r_t_kstatus: int = betterproto.int32_field(4)
    r_t_kstars: int = betterproto.int32_field(5)


@dataclass
class SysOptiLineAck(betterproto.Message):
    respones_cmd: int = betterproto.int32_field(1)
    current_frame: int = betterproto.int32_field(2)


@dataclass
class SysCommCmd(betterproto.Message):
    rw: int = betterproto.int32_field(1)
    id: int = betterproto.int32_field(2)
    context: int = betterproto.int32_field(3)


@dataclass
class SysUploadFileProgress(betterproto.Message):
    biz_id: str = betterproto.string_field(1)
    result: int = betterproto.int32_field(2)
    progress: int = betterproto.int32_field(3)


@dataclass
class SysErrorCode(betterproto.Message):
    code_no: int = betterproto.int32_field(1)


@dataclass
class SysBorder(betterproto.Message):
    borderval: int = betterproto.int32_field(1)


@dataclass
class SysPlanJobStatus(betterproto.Message):
    planjob_status: int = betterproto.int32_field(1)


@dataclass
class SysKnifeControl(betterproto.Message):
    knife_status: int = betterproto.int32_field(1)
    knife_height: int = betterproto.int32_field(2)


@dataclass
class SysResetSystemStatus(betterproto.Message):
    reset_staus: int = betterproto.int32_field(1)


@dataclass
class TimeCtrlLight(betterproto.Message):
    operate: int = betterproto.int32_field(1)
    enable: int = betterproto.int32_field(2)
    start_hour: int = betterproto.int32_field(3)
    start_min: int = betterproto.int32_field(4)
    end_hour: int = betterproto.int32_field(5)
    end_min: int = betterproto.int32_field(6)
    action: int = betterproto.int32_field(7)


@dataclass
class VisionPointMsg(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    z: float = betterproto.float_field(3)


@dataclass
class VisionPointInfoMsg(betterproto.Message):
    lable: int = betterproto.int32_field(1)
    num: int = betterproto.int32_field(2)
    vision_point: List["VisionPointMsg"] = betterproto.message_field(3)


@dataclass
class VioToAppInfoMsg(betterproto.Message):
    x: float = betterproto.double_field(1)
    y: float = betterproto.double_field(2)
    heading: float = betterproto.double_field(3)
    vio_state: int = betterproto.int32_field(4)
    brightness: int = betterproto.int32_field(5)
    detect_feature_num: int = betterproto.int32_field(6)
    track_feature_num: int = betterproto.int32_field(7)


@dataclass
class VisionStatisticMsg(betterproto.Message):
    mean: float = betterproto.float_field(1)
    var: float = betterproto.float_field(2)


@dataclass
class VisionStatisticInfoMsg(betterproto.Message):
    timestamp: float = betterproto.double_field(1)
    num: int = betterproto.int32_field(2)
    vision_statistics: List["VisionStatisticMsg"] = betterproto.message_field(3)


@dataclass
class SystemRapidStateTunnelMsg(betterproto.Message):
    rapid_state_data: List[int] = betterproto.int64_field(1)
    vision_point_info: List["VisionPointInfoMsg"] = betterproto.message_field(2)
    vio_to_app_info: "VioToAppInfoMsg" = betterproto.message_field(3)
    vision_statistic_info: "VisionStatisticInfoMsg" = betterproto.message_field(4)


@dataclass
class SystemTardStateTunnelMsg(betterproto.Message):
    tard_state_data: List[int] = betterproto.int64_field(1)


@dataclass
class SystemUpdateBufMsg(betterproto.Message):
    update_buf_data: List[int] = betterproto.int64_field(1)


@dataclass
class SysOffChipFlash(betterproto.Message):
    op: "Operation" = betterproto.enum_field(1)
    id: "OffPartId" = betterproto.enum_field(2)
    start_addr: int = betterproto.uint32_field(3)
    offset: int = betterproto.uint32_field(4)
    length: int = betterproto.int32_field(5)
    data: bytes = betterproto.bytes_field(6)
    code: int = betterproto.int32_field(7)
    msg: str = betterproto.string_field(8)


@dataclass
class SystemTmpCycleTxMsg(betterproto.Message):
    cycle_tx_data: List[int] = betterproto.int64_field(1)


@dataclass
class LoraCfgReq(betterproto.Message):
    op: int = betterproto.int32_field(1)
    cfg: str = betterproto.string_field(2)


@dataclass
class LoraCfgRsp(betterproto.Message):
    result: int = betterproto.int32_field(1)
    op: int = betterproto.int32_field(2)
    cfg: str = betterproto.string_field(3)
    fac_cfg: str = betterproto.string_field(4)


@dataclass
class ModFwInfo(betterproto.Message):
    type: int = betterproto.int32_field(1)
    identify: str = betterproto.string_field(2)
    version: str = betterproto.string_field(3)


@dataclass
class DeviceFwInfo(betterproto.Message):
    result: int = betterproto.int32_field(1)
    version: str = betterproto.string_field(2)
    mod: List["ModFwInfo"] = betterproto.message_field(3)


@dataclass
class MowToAppInfoT(betterproto.Message):
    type: int = betterproto.int32_field(1)
    cmd: int = betterproto.int32_field(2)
    mow_data: List[int] = betterproto.int32_field(3)


@dataclass
class DeviceProductTypeInfoT(betterproto.Message):
    result: int = betterproto.int32_field(1)
    main_product_type: str = betterproto.string_field(2)
    sub_product_type: str = betterproto.string_field(3)


@dataclass
class QCAppTestExcept(betterproto.Message):
    except_type: str = betterproto.string_field(1)
    conditions: List["QCAppTestConditions"] = betterproto.message_field(2)


@dataclass
class QCAppTestConditions(betterproto.Message):
    cond_type: str = betterproto.string_field(1)
    int_val: int = betterproto.int32_field(2)
    float_val: float = betterproto.float_field(3)
    double_val: float = betterproto.double_field(4)
    string_val: str = betterproto.string_field(5)


@dataclass
class MowToAppQctoolsInfoT(betterproto.Message):
    type: "QCAppTestId" = betterproto.enum_field(1)
    time_of_duration: int = betterproto.int32_field(2)
    result: int = betterproto.int32_field(3)
    result_details: str = betterproto.string_field(4)
    except_: List["QCAppTestExcept"] = betterproto.message_field(5)


@dataclass
class MCtrlSimulationCmdData(betterproto.Message):
    sub_cmd: int = betterproto.int32_field(1)
    param_id: int = betterproto.int32_field(2)
    param_value: List[int] = betterproto.int32_field(3)


@dataclass
class RptLora(betterproto.Message):
    pair_code_scan: int = betterproto.int32_field(1)
    pair_code_channel: int = betterproto.int32_field(2)
    pair_code_locid: int = betterproto.int32_field(3)
    pair_code_netid: int = betterproto.int32_field(4)
    lora_connection_status: int = betterproto.int32_field(5)


@dataclass
class RptRtk(betterproto.Message):
    status: int = betterproto.int32_field(1)
    pos_level: int = betterproto.int32_field(2)
    gps_stars: int = betterproto.int32_field(3)
    age: int = betterproto.int32_field(4)
    lat_std: int = betterproto.int32_field(5)
    lon_std: int = betterproto.int32_field(6)
    l2_stars: int = betterproto.int32_field(7)
    dis_status: int = betterproto.int64_field(8)
    top4_total_mean: int = betterproto.int64_field(9)
    co_view_stars: int = betterproto.int32_field(10)
    reset: int = betterproto.int32_field(11)
    lora_info: "RptLora" = betterproto.message_field(12)


@dataclass
class RptDevLocation(betterproto.Message):
    real_pos_x: int = betterproto.int32_field(1)
    real_pos_y: int = betterproto.int32_field(2)
    real_toward: int = betterproto.int32_field(3)
    pos_type: int = betterproto.int32_field(4)
    zone_hash: int = betterproto.int64_field(5)
    bol_hash: int = betterproto.int64_field(6)


@dataclass
class VioSurvivalInfoT(betterproto.Message):
    vio_survival_distance: float = betterproto.float_field(1)


@dataclass
class CollectorStatusT(betterproto.Message):
    collector_installation_status: int = betterproto.int32_field(1)


@dataclass
class LockStateT(betterproto.Message):
    lock_state: int = betterproto.uint32_field(1)


@dataclass
class RptDevStatus(betterproto.Message):
    sys_status: int = betterproto.int32_field(1)
    charge_state: int = betterproto.int32_field(2)
    battery_val: int = betterproto.int32_field(3)
    sensor_status: int = betterproto.int32_field(4)
    last_status: int = betterproto.int32_field(5)
    sys_time_stamp: int = betterproto.int64_field(6)
    vslam_status: int = betterproto.int32_field(7)
    mnet_info: "MnetInfo" = betterproto.message_field(8)
    vio_survival_info: "VioSurvivalInfoT" = betterproto.message_field(9)
    collector_status: "CollectorStatusT" = betterproto.message_field(10)
    lock_state: "LockStateT" = betterproto.message_field(11)


@dataclass
class RptConnectStatus(betterproto.Message):
    connect_type: int = betterproto.int32_field(1)
    ble_rssi: int = betterproto.int32_field(2)
    wifi_rssi: int = betterproto.int32_field(3)
    link_type: int = betterproto.int32_field(4)
    mnet_rssi: int = betterproto.int32_field(5)
    mnet_inet: int = betterproto.int32_field(6)
    used_net: "NetUsedType" = betterproto.enum_field(7)


@dataclass
class RptWork(betterproto.Message):
    plan: int = betterproto.int32_field(1)
    path_hash: int = betterproto.int64_field(2)
    progress: int = betterproto.int32_field(3)
    area: int = betterproto.int32_field(4)
    bp_info: int = betterproto.int32_field(5)
    bp_hash: int = betterproto.int64_field(6)
    bp_pos_x: int = betterproto.int32_field(7)
    bp_pos_y: int = betterproto.int32_field(8)
    real_path_num: int = betterproto.int64_field(9)
    path_pos_x: int = betterproto.int32_field(10)
    path_pos_y: int = betterproto.int32_field(11)
    ub_zone_hash: int = betterproto.int64_field(12)
    ub_path_hash: int = betterproto.int64_field(13)
    init_cfg_hash: int = betterproto.int64_field(14)
    ub_ecode_hash: int = betterproto.int64_field(15)
    nav_run_mode: int = betterproto.int32_field(16)
    test_mode_status: int = betterproto.int64_field(17)
    man_run_speed: int = betterproto.int32_field(18)
    nav_edit_status: int = betterproto.int32_field(19)
    knife_hight: int = betterproto.int32_field(20)


@dataclass
class RptMaintain(betterproto.Message):
    mileage: int = betterproto.int64_field(1)
    work_time: int = betterproto.int32_field(2)
    bat_cycles: int = betterproto.int32_field(3)


@dataclass
class ReportInfoCfg(betterproto.Message):
    act: "RptAct" = betterproto.enum_field(1)
    timeout: int = betterproto.int32_field(2)
    period: int = betterproto.int32_field(3)
    no_change_period: int = betterproto.int32_field(4)
    count: int = betterproto.int32_field(5)
    sub: List["RptInfoType"] = betterproto.enum_field(6)


@dataclass
class ReportInfoData(betterproto.Message):
    connect: "RptConnectStatus" = betterproto.message_field(1)
    dev: "RptDevStatus" = betterproto.message_field(2)
    rtk: "RptRtk" = betterproto.message_field(3)
    locations: List["RptDevLocation"] = betterproto.message_field(4)
    work: "RptWork" = betterproto.message_field(5)
    fw_info: "DeviceFwInfo" = betterproto.message_field(6)
    maintain: "RptMaintain" = betterproto.message_field(7)
    vision_point_info: List["VisionPointInfoMsg"] = betterproto.message_field(8)
    vio_to_app_info: "VioToAppInfoMsg" = betterproto.message_field(9)
    vision_statistic_info: "VisionStatisticInfoMsg" = betterproto.message_field(10)


@dataclass
class MctlSys(betterproto.Message):
    toapp_batinfo: "SysBatUp" = betterproto.message_field(1, group="SubSysMsg")
    toapp_work_state: "SysWorkState" = betterproto.message_field(2, group="SubSysMsg")
    todev_time_zone: "SysSetTimeZone" = betterproto.message_field(3, group="SubSysMsg")
    todev_data_time: "SysSetDateTime" = betterproto.message_field(4, group="SubSysMsg")
    job_plan: "SysJobPlan" = betterproto.message_field(6, group="SubSysMsg")
    toapp_err_code: "SysDevErrCode" = betterproto.message_field(7, group="SubSysMsg")
    todev_job_plan_time: "SysJobPlanTime" = betterproto.message_field(
        10, group="SubSysMsg"
    )
    toapp_mow_info: "SysMowInfo" = betterproto.message_field(11, group="SubSysMsg")
    bidire_comm_cmd: "SysCommCmd" = betterproto.message_field(12, group="SubSysMsg")
    plan_job_del: int = betterproto.int64_field(14, group="SubSysMsg")
    border: "SysBorder" = betterproto.message_field(15, group="SubSysMsg")
    toapp_plan_status: "SysPlanJobStatus" = betterproto.message_field(
        18, group="SubSysMsg"
    )
    toapp_ul_fprogress: "SysUploadFileProgress" = betterproto.message_field(
        19, group="SubSysMsg"
    )
    todev_deljobplan: "SysDelJobPlan" = betterproto.message_field(20, group="SubSysMsg")
    todev_mow_info_up: int = betterproto.int32_field(21, group="SubSysMsg")
    todev_knife_ctrl: "SysKnifeControl" = betterproto.message_field(
        22, group="SubSysMsg"
    )
    todev_reset_system: int = betterproto.int32_field(23, group="SubSysMsg")
    todev_reset_system_status: "SysResetSystemStatus" = betterproto.message_field(
        24, group="SubSysMsg"
    )
    system_rapid_state_tunnel: "SystemRapidStateTunnelMsg" = betterproto.message_field(
        25, group="SubSysMsg"
    )
    system_tard_state_tunnel: "SystemTardStateTunnelMsg" = betterproto.message_field(
        26, group="SubSysMsg"
    )
    system_update_buf: "SystemUpdateBufMsg" = betterproto.message_field(
        27, group="SubSysMsg"
    )
    todev_time_ctrl_light: "TimeCtrlLight" = betterproto.message_field(
        28, group="SubSysMsg"
    )
    system_tmp_cycle_tx: "SystemTmpCycleTxMsg" = betterproto.message_field(
        29, group="SubSysMsg"
    )
    todev_off_chip_flash: "SysOffChipFlash" = betterproto.message_field(
        30, group="SubSysMsg"
    )
    todev_get_dev_fw_info: int = betterproto.int32_field(31, group="SubSysMsg")
    toapp_dev_fw_info: "DeviceFwInfo" = betterproto.message_field(32, group="SubSysMsg")
    todev_lora_cfg_req: "LoraCfgReq" = betterproto.message_field(33, group="SubSysMsg")
    toapp_lora_cfg_rsp: "LoraCfgRsp" = betterproto.message_field(34, group="SubSysMsg")
    mow_to_app_info: "MowToAppInfoT" = betterproto.message_field(35, group="SubSysMsg")
    device_product_type_info: "DeviceProductTypeInfoT" = betterproto.message_field(
        36, group="SubSysMsg"
    )
    mow_to_app_qctools_info: "MowToAppQctoolsInfoT" = betterproto.message_field(
        37, group="SubSysMsg"
    )
    todev_report_cfg: "ReportInfoCfg" = betterproto.message_field(38, group="SubSysMsg")
    toapp_report_data: "ReportInfoData" = betterproto.message_field(
        39, group="SubSysMsg"
    )
    simulation_cmd: "MCtrlSimulationCmdData" = betterproto.message_field(
        42, group="SubSysMsg"
    )
