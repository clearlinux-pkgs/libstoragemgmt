#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libstoragemgmt
Version  : 1.6.2
Release  : 7
URL      : https://github.com/libstorage/libstoragemgmt/releases/download/1.6.2/libstoragemgmt-1.6.2.tar.gz
Source0  : https://github.com/libstorage/libstoragemgmt/releases/download/1.6.2/libstoragemgmt-1.6.2.tar.gz
Summary  : Storage array management library
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: libstoragemgmt-bin
Requires: libstoragemgmt-python3
Requires: libstoragemgmt-config
Requires: libstoragemgmt-lib
Requires: libstoragemgmt-man
Requires: libstoragemgmt-python
BuildRequires : chrpath
BuildRequires : openssl-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libconfig)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(python2)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : ply
BuildRequires : procps-ng
BuildRequires : pyaml
BuildRequires : pyudev
BuildRequires : pywbem
BuildRequires : six
BuildRequires : valgrind
BuildRequires : yajl-dev

%description
The libStorageMgmt library will provide a vendor agnostic open source storage
application programming interface (API) that will allow management of storage
arrays.  The library includes a command line interface for interactive use and
scripting (command lsmcli).  The library also has a daemon that is used for
executing plug-ins in a separate process (lsmd).

%package bin
Summary: bin components for the libstoragemgmt package.
Group: Binaries
Requires: libstoragemgmt-config
Requires: libstoragemgmt-man

%description bin
bin components for the libstoragemgmt package.


%package config
Summary: config components for the libstoragemgmt package.
Group: Default

%description config
config components for the libstoragemgmt package.


%package dev
Summary: dev components for the libstoragemgmt package.
Group: Development
Requires: libstoragemgmt-lib
Requires: libstoragemgmt-bin
Provides: libstoragemgmt-devel

%description dev
dev components for the libstoragemgmt package.


%package lib
Summary: lib components for the libstoragemgmt package.
Group: Libraries

%description lib
lib components for the libstoragemgmt package.


%package man
Summary: man components for the libstoragemgmt package.
Group: Default

%description man
man components for the libstoragemgmt package.


%package python
Summary: python components for the libstoragemgmt package.
Group: Default
Requires: libstoragemgmt-python3

%description python
python components for the libstoragemgmt package.


%package python3
Summary: python3 components for the libstoragemgmt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libstoragemgmt package.


%prep
%setup -q -n libstoragemgmt-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526648741
%configure --disable-static --with-python3
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1526648741
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/arcconf_lsmplugin
/usr/bin/hpsa_lsmplugin
/usr/bin/local_lsmplugin
/usr/bin/lsm.d/find_unused_lun.py
/usr/bin/lsm.d/local_sanity_check.py
/usr/bin/lsmcli
/usr/bin/lsmd
/usr/bin/megaraid_lsmplugin
/usr/bin/nfs_lsmplugin
/usr/bin/nstor_lsmplugin
/usr/bin/ontap_lsmplugin
/usr/bin/sim_lsmplugin
/usr/bin/simc_lsmplugin
/usr/bin/smispy_lsmplugin
/usr/bin/targetd_lsmplugin

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/libstoragemgmt.service
/usr/lib/tmpfiles.d/libstoragemgmt.conf

%files dev
%defattr(-,root,root,-)
/usr/include/libstoragemgmt/libstoragemgmt.h
/usr/include/libstoragemgmt/libstoragemgmt_accessgroups.h
/usr/include/libstoragemgmt/libstoragemgmt_battery.h
/usr/include/libstoragemgmt/libstoragemgmt_blockrange.h
/usr/include/libstoragemgmt/libstoragemgmt_capabilities.h
/usr/include/libstoragemgmt/libstoragemgmt_common.h
/usr/include/libstoragemgmt/libstoragemgmt_disk.h
/usr/include/libstoragemgmt/libstoragemgmt_error.h
/usr/include/libstoragemgmt/libstoragemgmt_fs.h
/usr/include/libstoragemgmt/libstoragemgmt_hash.h
/usr/include/libstoragemgmt/libstoragemgmt_local_disk.h
/usr/include/libstoragemgmt/libstoragemgmt_nfsexport.h
/usr/include/libstoragemgmt/libstoragemgmt_plug_interface.h
/usr/include/libstoragemgmt/libstoragemgmt_pool.h
/usr/include/libstoragemgmt/libstoragemgmt_snapshot.h
/usr/include/libstoragemgmt/libstoragemgmt_systems.h
/usr/include/libstoragemgmt/libstoragemgmt_targetport.h
/usr/include/libstoragemgmt/libstoragemgmt_types.h
/usr/include/libstoragemgmt/libstoragemgmt_version.h
/usr/include/libstoragemgmt/libstoragemgmt_volumes.h
/usr/lib64/libstoragemgmt.so
/usr/lib64/pkgconfig/libstoragemgmt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libstoragemgmt.so.1
/usr/lib64/libstoragemgmt.so.1.6.2

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/arcconf_lsmplugin.1
/usr/share/man/man1/hpsa_lsmplugin.1
/usr/share/man/man1/local_lsmplugin.1
/usr/share/man/man1/lsmcli.1
/usr/share/man/man1/lsmd.1
/usr/share/man/man1/megaraid_lsmplugin.1
/usr/share/man/man1/nfs_lsmplugin.1
/usr/share/man/man1/nstor_lsmplugin.1
/usr/share/man/man1/ontap_lsmplugin.1
/usr/share/man/man1/sim_lsmplugin.1
/usr/share/man/man1/simc_lsmplugin.1
/usr/share/man/man1/smispy_lsmplugin.1
/usr/share/man/man1/targetd_lsmplugin.1
/usr/share/man/man3/libstoragemgmt.h.3
/usr/share/man/man3/lsm_access_group_create.3
/usr/share/man/man3/lsm_access_group_delete.3
/usr/share/man/man3/lsm_access_group_id_get.3
/usr/share/man/man3/lsm_access_group_initiator_add.3
/usr/share/man/man3/lsm_access_group_initiator_delete.3
/usr/share/man/man3/lsm_access_group_initiator_id_get.3
/usr/share/man/man3/lsm_access_group_list.3
/usr/share/man/man3/lsm_access_group_name_get.3
/usr/share/man/man3/lsm_access_group_record_array_free.3
/usr/share/man/man3/lsm_access_group_record_copy.3
/usr/share/man/man3/lsm_access_group_record_free.3
/usr/share/man/man3/lsm_access_group_system_id_get.3
/usr/share/man/man3/lsm_access_groups_granted_to_volume.3
/usr/share/man/man3/lsm_available_plugins_list.3
/usr/share/man/man3/lsm_battery_id_get.3
/usr/share/man/man3/lsm_battery_list.3
/usr/share/man/man3/lsm_battery_name_get.3
/usr/share/man/man3/lsm_battery_record_array_free.3
/usr/share/man/man3/lsm_battery_record_copy.3
/usr/share/man/man3/lsm_battery_record_free.3
/usr/share/man/man3/lsm_battery_status_get.3
/usr/share/man/man3/lsm_battery_system_id_get.3
/usr/share/man/man3/lsm_battery_type_get.3
/usr/share/man/man3/lsm_block_range_block_count_get.3
/usr/share/man/man3/lsm_block_range_dest_start_get.3
/usr/share/man/man3/lsm_block_range_record_alloc.3
/usr/share/man/man3/lsm_block_range_record_array_alloc.3
/usr/share/man/man3/lsm_block_range_record_array_free.3
/usr/share/man/man3/lsm_block_range_record_copy.3
/usr/share/man/man3/lsm_block_range_record_free.3
/usr/share/man/man3/lsm_block_range_source_start_get.3
/usr/share/man/man3/lsm_capabilities.3
/usr/share/man/man3/lsm_capability_get.3
/usr/share/man/man3/lsm_capability_record_free.3
/usr/share/man/man3/lsm_capability_supported.3
/usr/share/man/man3/lsm_connect_close.3
/usr/share/man/man3/lsm_connect_password.3
/usr/share/man/man3/lsm_connect_timeout_get.3
/usr/share/man/man3/lsm_connect_timeout_set.3
/usr/share/man/man3/lsm_disk_block_size_get.3
/usr/share/man/man3/lsm_disk_id_get.3
/usr/share/man/man3/lsm_disk_link_type_get.3
/usr/share/man/man3/lsm_disk_list.3
/usr/share/man/man3/lsm_disk_location_get.3
/usr/share/man/man3/lsm_disk_name_get.3
/usr/share/man/man3/lsm_disk_number_of_blocks_get.3
/usr/share/man/man3/lsm_disk_record_array_free.3
/usr/share/man/man3/lsm_disk_record_copy.3
/usr/share/man/man3/lsm_disk_record_free.3
/usr/share/man/man3/lsm_disk_rpm_get.3
/usr/share/man/man3/lsm_disk_status_get.3
/usr/share/man/man3/lsm_disk_system_id_get.3
/usr/share/man/man3/lsm_disk_type_get.3
/usr/share/man/man3/lsm_disk_vpd83_get.3
/usr/share/man/man3/lsm_error_debug_data_get.3
/usr/share/man/man3/lsm_error_debug_get.3
/usr/share/man/man3/lsm_error_exception_get.3
/usr/share/man/man3/lsm_error_free.3
/usr/share/man/man3/lsm_error_last_get.3
/usr/share/man/man3/lsm_error_message_get.3
/usr/share/man/man3/lsm_error_number_get.3
/usr/share/man/man3/lsm_fs_child_dependency.3
/usr/share/man/man3/lsm_fs_child_dependency_delete.3
/usr/share/man/man3/lsm_fs_clone.3
/usr/share/man/man3/lsm_fs_create.3
/usr/share/man/man3/lsm_fs_delete.3
/usr/share/man/man3/lsm_fs_file_clone.3
/usr/share/man/man3/lsm_fs_free_space_get.3
/usr/share/man/man3/lsm_fs_id_get.3
/usr/share/man/man3/lsm_fs_list.3
/usr/share/man/man3/lsm_fs_name_get.3
/usr/share/man/man3/lsm_fs_pool_id_get.3
/usr/share/man/man3/lsm_fs_record_array_free.3
/usr/share/man/man3/lsm_fs_record_copy.3
/usr/share/man/man3/lsm_fs_record_free.3
/usr/share/man/man3/lsm_fs_resize.3
/usr/share/man/man3/lsm_fs_ss_create.3
/usr/share/man/man3/lsm_fs_ss_delete.3
/usr/share/man/man3/lsm_fs_ss_id_get.3
/usr/share/man/man3/lsm_fs_ss_list.3
/usr/share/man/man3/lsm_fs_ss_name_get.3
/usr/share/man/man3/lsm_fs_ss_record_array_free.3
/usr/share/man/man3/lsm_fs_ss_record_copy.3
/usr/share/man/man3/lsm_fs_ss_record_free.3
/usr/share/man/man3/lsm_fs_ss_restore.3
/usr/share/man/man3/lsm_fs_ss_time_stamp_get.3
/usr/share/man/man3/lsm_fs_system_id_get.3
/usr/share/man/man3/lsm_fs_total_space_get.3
/usr/share/man/man3/lsm_initiator_id_verify.3
/usr/share/man/man3/lsm_iscsi_chap_auth.3
/usr/share/man/man3/lsm_job_free.3
/usr/share/man/man3/lsm_job_status_fs_get.3
/usr/share/man/man3/lsm_job_status_get.3
/usr/share/man/man3/lsm_job_status_pool_get.3
/usr/share/man/man3/lsm_job_status_ss_get.3
/usr/share/man/man3/lsm_job_status_volume_get.3
/usr/share/man/man3/lsm_local_disk_fault_led_off.3
/usr/share/man/man3/lsm_local_disk_fault_led_on.3
/usr/share/man/man3/lsm_local_disk_health_status_get.3
/usr/share/man/man3/lsm_local_disk_ident_led_off.3
/usr/share/man/man3/lsm_local_disk_ident_led_on.3
/usr/share/man/man3/lsm_local_disk_led_status_get.3
/usr/share/man/man3/lsm_local_disk_link_speed_get.3
/usr/share/man/man3/lsm_local_disk_link_type_get.3
/usr/share/man/man3/lsm_local_disk_list.3
/usr/share/man/man3/lsm_local_disk_rpm_get.3
/usr/share/man/man3/lsm_local_disk_serial_num_get.3
/usr/share/man/man3/lsm_local_disk_vpd83_get.3
/usr/share/man/man3/lsm_local_disk_vpd83_search.3
/usr/share/man/man3/lsm_nfs_auth_types.3
/usr/share/man/man3/lsm_nfs_export_anon_gid_get.3
/usr/share/man/man3/lsm_nfs_export_anon_uid_get.3
/usr/share/man/man3/lsm_nfs_export_auth_type_get.3
/usr/share/man/man3/lsm_nfs_export_delete.3
/usr/share/man/man3/lsm_nfs_export_export_path_get.3
/usr/share/man/man3/lsm_nfs_export_fs.3
/usr/share/man/man3/lsm_nfs_export_fs_id_get.3
/usr/share/man/man3/lsm_nfs_export_id_get.3
/usr/share/man/man3/lsm_nfs_export_options_get.3
/usr/share/man/man3/lsm_nfs_export_read_only_get.3
/usr/share/man/man3/lsm_nfs_export_read_write_get.3
/usr/share/man/man3/lsm_nfs_export_record_array_free.3
/usr/share/man/man3/lsm_nfs_export_record_copy.3
/usr/share/man/man3/lsm_nfs_export_record_free.3
/usr/share/man/man3/lsm_nfs_export_root_get.3
/usr/share/man/man3/lsm_nfs_list.3
/usr/share/man/man3/lsm_plugin_info_get.3
/usr/share/man/man3/lsm_pool_element_type_get.3
/usr/share/man/man3/lsm_pool_free_space_get.3
/usr/share/man/man3/lsm_pool_id_get.3
/usr/share/man/man3/lsm_pool_list.3
/usr/share/man/man3/lsm_pool_member_info.3
/usr/share/man/man3/lsm_pool_name_get.3
/usr/share/man/man3/lsm_pool_record_array_free.3
/usr/share/man/man3/lsm_pool_record_copy.3
/usr/share/man/man3/lsm_pool_record_free.3
/usr/share/man/man3/lsm_pool_status_get.3
/usr/share/man/man3/lsm_pool_status_info_get.3
/usr/share/man/man3/lsm_pool_system_id_get.3
/usr/share/man/man3/lsm_pool_total_space_get.3
/usr/share/man/man3/lsm_pool_unsupported_actions_get.3
/usr/share/man/man3/lsm_string_list_alloc.3
/usr/share/man/man3/lsm_string_list_append.3
/usr/share/man/man3/lsm_string_list_copy.3
/usr/share/man/man3/lsm_string_list_delete.3
/usr/share/man/man3/lsm_string_list_elem_get.3
/usr/share/man/man3/lsm_string_list_elem_set.3
/usr/share/man/man3/lsm_string_list_free.3
/usr/share/man/man3/lsm_string_list_size.3
/usr/share/man/man3/lsm_system_fw_version_get.3
/usr/share/man/man3/lsm_system_id_get.3
/usr/share/man/man3/lsm_system_list.3
/usr/share/man/man3/lsm_system_mode_get.3
/usr/share/man/man3/lsm_system_name_get.3
/usr/share/man/man3/lsm_system_read_cache_pct_get.3
/usr/share/man/man3/lsm_system_read_cache_pct_update.3
/usr/share/man/man3/lsm_system_record_array_free.3
/usr/share/man/man3/lsm_system_record_copy.3
/usr/share/man/man3/lsm_system_record_free.3
/usr/share/man/man3/lsm_system_status_get.3
/usr/share/man/man3/lsm_target_port_copy.3
/usr/share/man/man3/lsm_target_port_id_get.3
/usr/share/man/man3/lsm_target_port_list.3
/usr/share/man/man3/lsm_target_port_network_address_get.3
/usr/share/man/man3/lsm_target_port_physical_address_get.3
/usr/share/man/man3/lsm_target_port_physical_name_get.3
/usr/share/man/man3/lsm_target_port_record_array_free.3
/usr/share/man/man3/lsm_target_port_record_free.3
/usr/share/man/man3/lsm_target_port_service_address_get.3
/usr/share/man/man3/lsm_target_port_system_id_get.3
/usr/share/man/man3/lsm_target_port_type_get.3
/usr/share/man/man3/lsm_volume_admin_state_get.3
/usr/share/man/man3/lsm_volume_block_size_get.3
/usr/share/man/man3/lsm_volume_cache_info.3
/usr/share/man/man3/lsm_volume_child_dependency.3
/usr/share/man/man3/lsm_volume_child_dependency_delete.3
/usr/share/man/man3/lsm_volume_create.3
/usr/share/man/man3/lsm_volume_delete.3
/usr/share/man/man3/lsm_volume_disable.3
/usr/share/man/man3/lsm_volume_enable.3
/usr/share/man/man3/lsm_volume_id_get.3
/usr/share/man/man3/lsm_volume_ident_led_off.3
/usr/share/man/man3/lsm_volume_ident_led_on.3
/usr/share/man/man3/lsm_volume_list.3
/usr/share/man/man3/lsm_volume_mask.3
/usr/share/man/man3/lsm_volume_name_get.3
/usr/share/man/man3/lsm_volume_number_of_blocks_get.3
/usr/share/man/man3/lsm_volume_physical_disk_cache_update.3
/usr/share/man/man3/lsm_volume_pool_id_get.3
/usr/share/man/man3/lsm_volume_raid_create.3
/usr/share/man/man3/lsm_volume_raid_create_cap_get.3
/usr/share/man/man3/lsm_volume_raid_info.3
/usr/share/man/man3/lsm_volume_read_cache_policy_update.3
/usr/share/man/man3/lsm_volume_record_array_free.3
/usr/share/man/man3/lsm_volume_record_copy.3
/usr/share/man/man3/lsm_volume_record_free.3
/usr/share/man/man3/lsm_volume_replicate.3
/usr/share/man/man3/lsm_volume_replicate_range.3
/usr/share/man/man3/lsm_volume_replicate_range_block_size.3
/usr/share/man/man3/lsm_volume_resize.3
/usr/share/man/man3/lsm_volume_system_id_get.3
/usr/share/man/man3/lsm_volume_unmask.3
/usr/share/man/man3/lsm_volume_vpd83_get.3
/usr/share/man/man3/lsm_volume_vpd83_verify.3
/usr/share/man/man3/lsm_volume_write_cache_policy_update.3
/usr/share/man/man3/lsm_volumes_accessible_by_access_group.3
/usr/share/man/man5/lsmd.conf.5.5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
