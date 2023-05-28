# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17meshtastic/config.proto\"\x8e\x1b\n\x06\x43onfig\x12&\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x14.Config.DeviceConfigH\x00\x12*\n\x08position\x18\x02 \x01(\x0b\x32\x16.Config.PositionConfigH\x00\x12$\n\x05power\x18\x03 \x01(\x0b\x32\x13.Config.PowerConfigH\x00\x12(\n\x07network\x18\x04 \x01(\x0b\x32\x15.Config.NetworkConfigH\x00\x12(\n\x07\x64isplay\x18\x05 \x01(\x0b\x32\x15.Config.DisplayConfigH\x00\x12\"\n\x04lora\x18\x06 \x01(\x0b\x32\x12.Config.LoRaConfigH\x00\x12,\n\tbluetooth\x18\x07 \x01(\x0b\x32\x17.Config.BluetoothConfigH\x00\x1a\xdc\x03\n\x0c\x44\x65viceConfig\x12\'\n\x04role\x18\x01 \x01(\x0e\x32\x19.Config.DeviceConfig.Role\x12\x16\n\x0eserial_enabled\x18\x02 \x01(\x08\x12\x19\n\x11\x64\x65\x62ug_log_enabled\x18\x03 \x01(\x08\x12\x13\n\x0b\x62utton_gpio\x18\x04 \x01(\r\x12\x13\n\x0b\x62uzzer_gpio\x18\x05 \x01(\r\x12>\n\x10rebroadcast_mode\x18\x06 \x01(\x0e\x32$.Config.DeviceConfig.RebroadcastMode\x12 \n\x18node_info_broadcast_secs\x18\x07 \x01(\r\x12\"\n\x1a\x64ouble_tap_as_button_press\x18\x08 \x01(\x08\x12\x12\n\nis_managed\x18\t \x01(\x08\"i\n\x04Role\x12\n\n\x06\x43LIENT\x10\x00\x12\x0f\n\x0b\x43LIENT_MUTE\x10\x01\x12\n\n\x06ROUTER\x10\x02\x12\x11\n\rROUTER_CLIENT\x10\x03\x12\x0c\n\x08REPEATER\x10\x04\x12\x0b\n\x07TRACKER\x10\x05\x12\n\n\x06SENSOR\x10\x06\"A\n\x0fRebroadcastMode\x12\x07\n\x03\x41LL\x10\x00\x12\x15\n\x11\x41LL_SKIP_DECODING\x10\x01\x12\x0e\n\nLOCAL_ONLY\x10\x02\x1a\x80\x04\n\x0ePositionConfig\x12\x1f\n\x17position_broadcast_secs\x18\x01 \x01(\r\x12(\n position_broadcast_smart_enabled\x18\x02 \x01(\x08\x12\x16\n\x0e\x66ixed_position\x18\x03 \x01(\x08\x12\x13\n\x0bgps_enabled\x18\x04 \x01(\x08\x12\x1b\n\x13gps_update_interval\x18\x05 \x01(\r\x12\x18\n\x10gps_attempt_time\x18\x06 \x01(\r\x12\x16\n\x0eposition_flags\x18\x07 \x01(\r\x12\x0f\n\x07rx_gpio\x18\x08 \x01(\r\x12\x0f\n\x07tx_gpio\x18\t \x01(\r\x12(\n broadcast_smart_minimum_distance\x18\n \x01(\r\x12-\n%broadcast_smart_minimum_interval_secs\x18\x0b \x01(\r\"\xab\x01\n\rPositionFlags\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x41LTITUDE\x10\x01\x12\x10\n\x0c\x41LTITUDE_MSL\x10\x02\x12\x16\n\x12GEOIDAL_SEPARATION\x10\x04\x12\x07\n\x03\x44OP\x10\x08\x12\t\n\x05HVDOP\x10\x10\x12\r\n\tSATINVIEW\x10 \x12\n\n\x06SEQ_NO\x10@\x12\x0e\n\tTIMESTAMP\x10\x80\x01\x12\x0c\n\x07HEADING\x10\x80\x02\x12\n\n\x05SPEED\x10\x80\x04\x1a\xe5\x01\n\x0bPowerConfig\x12\x17\n\x0fis_power_saving\x18\x01 \x01(\x08\x12&\n\x1eon_battery_shutdown_after_secs\x18\x02 \x01(\r\x12\x1f\n\x17\x61\x64\x63_multiplier_override\x18\x03 \x01(\x02\x12\x1b\n\x13wait_bluetooth_secs\x18\x04 \x01(\r\x12\x1d\n\x15mesh_sds_timeout_secs\x18\x05 \x01(\r\x12\x10\n\x08sds_secs\x18\x06 \x01(\r\x12\x0f\n\x07ls_secs\x18\x07 \x01(\r\x12\x15\n\rmin_wake_secs\x18\x08 \x01(\r\x1a\xe8\x02\n\rNetworkConfig\x12\x14\n\x0cwifi_enabled\x18\x01 \x01(\x08\x12\x11\n\twifi_ssid\x18\x03 \x01(\t\x12\x10\n\x08wifi_psk\x18\x04 \x01(\t\x12\x12\n\nntp_server\x18\x05 \x01(\t\x12\x13\n\x0b\x65th_enabled\x18\x06 \x01(\x08\x12\x37\n\x0c\x61\x64\x64ress_mode\x18\x07 \x01(\x0e\x32!.Config.NetworkConfig.AddressMode\x12\x35\n\x0bipv4_config\x18\x08 \x01(\x0b\x32 .Config.NetworkConfig.IpV4Config\x12\x16\n\x0ersyslog_server\x18\t \x01(\t\x1a\x46\n\nIpV4Config\x12\n\n\x02ip\x18\x01 \x01(\x07\x12\x0f\n\x07gateway\x18\x02 \x01(\x07\x12\x0e\n\x06subnet\x18\x03 \x01(\x07\x12\x0b\n\x03\x64ns\x18\x04 \x01(\x07\"#\n\x0b\x41\x64\x64ressMode\x12\x08\n\x04\x44HCP\x10\x00\x12\n\n\x06STATIC\x10\x01\x1a\x92\x05\n\rDisplayConfig\x12\x16\n\x0escreen_on_secs\x18\x01 \x01(\r\x12=\n\ngps_format\x18\x02 \x01(\x0e\x32).Config.DisplayConfig.GpsCoordinateFormat\x12!\n\x19\x61uto_screen_carousel_secs\x18\x03 \x01(\r\x12\x19\n\x11\x63ompass_north_top\x18\x04 \x01(\x08\x12\x13\n\x0b\x66lip_screen\x18\x05 \x01(\x08\x12\x31\n\x05units\x18\x06 \x01(\x0e\x32\".Config.DisplayConfig.DisplayUnits\x12,\n\x04oled\x18\x07 \x01(\x0e\x32\x1e.Config.DisplayConfig.OledType\x12\x36\n\x0b\x64isplaymode\x18\x08 \x01(\x0e\x32!.Config.DisplayConfig.DisplayMode\x12\x14\n\x0cheading_bold\x18\t \x01(\x08\x12\x1d\n\x15wake_on_tap_or_motion\x18\n \x01(\x08\"M\n\x13GpsCoordinateFormat\x12\x07\n\x03\x44\x45\x43\x10\x00\x12\x07\n\x03\x44MS\x10\x01\x12\x07\n\x03UTM\x10\x02\x12\x08\n\x04MGRS\x10\x03\x12\x07\n\x03OLC\x10\x04\x12\x08\n\x04OSGR\x10\x05\"(\n\x0c\x44isplayUnits\x12\n\n\x06METRIC\x10\x00\x12\x0c\n\x08IMPERIAL\x10\x01\"M\n\x08OledType\x12\r\n\tOLED_AUTO\x10\x00\x12\x10\n\x0cOLED_SSD1306\x10\x01\x12\x0f\n\x0bOLED_SH1106\x10\x02\x12\x0f\n\x0bOLED_SH1107\x10\x03\"A\n\x0b\x44isplayMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08TWOCOLOR\x10\x01\x12\x0c\n\x08INVERTED\x10\x02\x12\t\n\x05\x43OLOR\x10\x03\x1a\xe1\x05\n\nLoRaConfig\x12\x12\n\nuse_preset\x18\x01 \x01(\x08\x12\x34\n\x0cmodem_preset\x18\x02 \x01(\x0e\x32\x1e.Config.LoRaConfig.ModemPreset\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x15\n\rspread_factor\x18\x04 \x01(\r\x12\x13\n\x0b\x63oding_rate\x18\x05 \x01(\r\x12\x18\n\x10\x66requency_offset\x18\x06 \x01(\x02\x12-\n\x06region\x18\x07 \x01(\x0e\x32\x1d.Config.LoRaConfig.RegionCode\x12\x11\n\thop_limit\x18\x08 \x01(\r\x12\x12\n\ntx_enabled\x18\t \x01(\x08\x12\x10\n\x08tx_power\x18\n \x01(\x05\x12\x13\n\x0b\x63hannel_num\x18\x0b \x01(\r\x12\x1b\n\x13override_duty_cycle\x18\x0c \x01(\x08\x12\x1e\n\x16sx126x_rx_boosted_gain\x18\r \x01(\x08\x12\x1a\n\x12override_frequency\x18\x0e \x01(\x02\x12\x17\n\x0fignore_incoming\x18g \x03(\r\"\xa9\x01\n\nRegionCode\x12\t\n\x05UNSET\x10\x00\x12\x06\n\x02US\x10\x01\x12\n\n\x06\x45U_433\x10\x02\x12\n\n\x06\x45U_868\x10\x03\x12\x06\n\x02\x43N\x10\x04\x12\x06\n\x02JP\x10\x05\x12\x07\n\x03\x41NZ\x10\x06\x12\x06\n\x02KR\x10\x07\x12\x06\n\x02TW\x10\x08\x12\x06\n\x02RU\x10\t\x12\x06\n\x02IN\x10\n\x12\n\n\x06NZ_865\x10\x0b\x12\x06\n\x02TH\x10\x0c\x12\x0b\n\x07LORA_24\x10\r\x12\n\n\x06UA_433\x10\x0e\x12\n\n\x06UA_868\x10\x0f\"\x94\x01\n\x0bModemPreset\x12\r\n\tLONG_FAST\x10\x00\x12\r\n\tLONG_SLOW\x10\x01\x12\x12\n\x0eVERY_LONG_SLOW\x10\x02\x12\x0f\n\x0bMEDIUM_SLOW\x10\x03\x12\x0f\n\x0bMEDIUM_FAST\x10\x04\x12\x0e\n\nSHORT_SLOW\x10\x05\x12\x0e\n\nSHORT_FAST\x10\x06\x12\x11\n\rLONG_MODERATE\x10\x07\x1a\xa2\x01\n\x0f\x42luetoothConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x31\n\x04mode\x18\x02 \x01(\x0e\x32#.Config.BluetoothConfig.PairingMode\x12\x11\n\tfixed_pin\x18\x03 \x01(\r\"8\n\x0bPairingMode\x12\x0e\n\nRANDOM_PIN\x10\x00\x12\r\n\tFIXED_PIN\x10\x01\x12\n\n\x06NO_PIN\x10\x02\x42\x11\n\x0fpayload_variantBa\n\x13\x63om.geeksville.meshB\x0c\x43onfigProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CONFIG_DEVICECONFIG = _CONFIG.nested_types_by_name['DeviceConfig']
_CONFIG_POSITIONCONFIG = _CONFIG.nested_types_by_name['PositionConfig']
_CONFIG_POWERCONFIG = _CONFIG.nested_types_by_name['PowerConfig']
_CONFIG_NETWORKCONFIG = _CONFIG.nested_types_by_name['NetworkConfig']
_CONFIG_NETWORKCONFIG_IPV4CONFIG = _CONFIG_NETWORKCONFIG.nested_types_by_name['IpV4Config']
_CONFIG_DISPLAYCONFIG = _CONFIG.nested_types_by_name['DisplayConfig']
_CONFIG_LORACONFIG = _CONFIG.nested_types_by_name['LoRaConfig']
_CONFIG_BLUETOOTHCONFIG = _CONFIG.nested_types_by_name['BluetoothConfig']
_CONFIG_DEVICECONFIG_ROLE = _CONFIG_DEVICECONFIG.enum_types_by_name['Role']
_CONFIG_DEVICECONFIG_REBROADCASTMODE = _CONFIG_DEVICECONFIG.enum_types_by_name['RebroadcastMode']
_CONFIG_POSITIONCONFIG_POSITIONFLAGS = _CONFIG_POSITIONCONFIG.enum_types_by_name['PositionFlags']
_CONFIG_NETWORKCONFIG_ADDRESSMODE = _CONFIG_NETWORKCONFIG.enum_types_by_name['AddressMode']
_CONFIG_DISPLAYCONFIG_GPSCOORDINATEFORMAT = _CONFIG_DISPLAYCONFIG.enum_types_by_name['GpsCoordinateFormat']
_CONFIG_DISPLAYCONFIG_DISPLAYUNITS = _CONFIG_DISPLAYCONFIG.enum_types_by_name['DisplayUnits']
_CONFIG_DISPLAYCONFIG_OLEDTYPE = _CONFIG_DISPLAYCONFIG.enum_types_by_name['OledType']
_CONFIG_DISPLAYCONFIG_DISPLAYMODE = _CONFIG_DISPLAYCONFIG.enum_types_by_name['DisplayMode']
_CONFIG_LORACONFIG_REGIONCODE = _CONFIG_LORACONFIG.enum_types_by_name['RegionCode']
_CONFIG_LORACONFIG_MODEMPRESET = _CONFIG_LORACONFIG.enum_types_by_name['ModemPreset']
_CONFIG_BLUETOOTHCONFIG_PAIRINGMODE = _CONFIG_BLUETOOTHCONFIG.enum_types_by_name['PairingMode']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

  'DeviceConfig' : _reflection.GeneratedProtocolMessageType('DeviceConfig', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_DEVICECONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.DeviceConfig)
    })
  ,

  'PositionConfig' : _reflection.GeneratedProtocolMessageType('PositionConfig', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_POSITIONCONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.PositionConfig)
    })
  ,

  'PowerConfig' : _reflection.GeneratedProtocolMessageType('PowerConfig', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_POWERCONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.PowerConfig)
    })
  ,

  'NetworkConfig' : _reflection.GeneratedProtocolMessageType('NetworkConfig', (_message.Message,), {

    'IpV4Config' : _reflection.GeneratedProtocolMessageType('IpV4Config', (_message.Message,), {
      'DESCRIPTOR' : _CONFIG_NETWORKCONFIG_IPV4CONFIG,
      '__module__' : 'meshtastic.config_pb2'
      # @@protoc_insertion_point(class_scope:Config.NetworkConfig.IpV4Config)
      })
    ,
    'DESCRIPTOR' : _CONFIG_NETWORKCONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.NetworkConfig)
    })
  ,

  'DisplayConfig' : _reflection.GeneratedProtocolMessageType('DisplayConfig', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_DISPLAYCONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.DisplayConfig)
    })
  ,

  'LoRaConfig' : _reflection.GeneratedProtocolMessageType('LoRaConfig', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_LORACONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.LoRaConfig)
    })
  ,

  'BluetoothConfig' : _reflection.GeneratedProtocolMessageType('BluetoothConfig', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_BLUETOOTHCONFIG,
    '__module__' : 'meshtastic.config_pb2'
    # @@protoc_insertion_point(class_scope:Config.BluetoothConfig)
    })
  ,
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'meshtastic.config_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  })
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.DeviceConfig)
_sym_db.RegisterMessage(Config.PositionConfig)
_sym_db.RegisterMessage(Config.PowerConfig)
_sym_db.RegisterMessage(Config.NetworkConfig)
_sym_db.RegisterMessage(Config.NetworkConfig.IpV4Config)
_sym_db.RegisterMessage(Config.DisplayConfig)
_sym_db.RegisterMessage(Config.LoRaConfig)
_sym_db.RegisterMessage(Config.BluetoothConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\014ConfigProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _CONFIG._serialized_start=28
  _CONFIG._serialized_end=3498
  _CONFIG_DEVICECONFIG._serialized_start=327
  _CONFIG_DEVICECONFIG._serialized_end=803
  _CONFIG_DEVICECONFIG_ROLE._serialized_start=631
  _CONFIG_DEVICECONFIG_ROLE._serialized_end=736
  _CONFIG_DEVICECONFIG_REBROADCASTMODE._serialized_start=738
  _CONFIG_DEVICECONFIG_REBROADCASTMODE._serialized_end=803
  _CONFIG_POSITIONCONFIG._serialized_start=806
  _CONFIG_POSITIONCONFIG._serialized_end=1318
  _CONFIG_POSITIONCONFIG_POSITIONFLAGS._serialized_start=1147
  _CONFIG_POSITIONCONFIG_POSITIONFLAGS._serialized_end=1318
  _CONFIG_POWERCONFIG._serialized_start=1321
  _CONFIG_POWERCONFIG._serialized_end=1550
  _CONFIG_NETWORKCONFIG._serialized_start=1553
  _CONFIG_NETWORKCONFIG._serialized_end=1913
  _CONFIG_NETWORKCONFIG_IPV4CONFIG._serialized_start=1806
  _CONFIG_NETWORKCONFIG_IPV4CONFIG._serialized_end=1876
  _CONFIG_NETWORKCONFIG_ADDRESSMODE._serialized_start=1878
  _CONFIG_NETWORKCONFIG_ADDRESSMODE._serialized_end=1913
  _CONFIG_DISPLAYCONFIG._serialized_start=1916
  _CONFIG_DISPLAYCONFIG._serialized_end=2574
  _CONFIG_DISPLAYCONFIG_GPSCOORDINATEFORMAT._serialized_start=2309
  _CONFIG_DISPLAYCONFIG_GPSCOORDINATEFORMAT._serialized_end=2386
  _CONFIG_DISPLAYCONFIG_DISPLAYUNITS._serialized_start=2388
  _CONFIG_DISPLAYCONFIG_DISPLAYUNITS._serialized_end=2428
  _CONFIG_DISPLAYCONFIG_OLEDTYPE._serialized_start=2430
  _CONFIG_DISPLAYCONFIG_OLEDTYPE._serialized_end=2507
  _CONFIG_DISPLAYCONFIG_DISPLAYMODE._serialized_start=2509
  _CONFIG_DISPLAYCONFIG_DISPLAYMODE._serialized_end=2574
  _CONFIG_LORACONFIG._serialized_start=2577
  _CONFIG_LORACONFIG._serialized_end=3314
  _CONFIG_LORACONFIG_REGIONCODE._serialized_start=2994
  _CONFIG_LORACONFIG_REGIONCODE._serialized_end=3163
  _CONFIG_LORACONFIG_MODEMPRESET._serialized_start=3166
  _CONFIG_LORACONFIG_MODEMPRESET._serialized_end=3314
  _CONFIG_BLUETOOTHCONFIG._serialized_start=3317
  _CONFIG_BLUETOOTHCONFIG._serialized_end=3479
  _CONFIG_BLUETOOTHCONFIG_PAIRINGMODE._serialized_start=3423
  _CONFIG_BLUETOOTHCONFIG_PAIRINGMODE._serialized_end=3479
# @@protoc_insertion_point(module_scope)
