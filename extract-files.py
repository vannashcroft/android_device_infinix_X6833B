#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/infinix/X6833B',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}-{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.mediatek.hardware.videotelephony@1.0',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/hw/android.hardware.gnss-service.mediatek': blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),

    ('vendor/lib/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so', 'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'vendor/bin/hw/android.hardware.security.keymint-service.trustonic': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V1-ndk.so'),

    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),

    'vendor/bin/hw/mt6789/camerahalserver': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so')
        .replace_needed('libbinder.so', 'libbinder-v32.so')
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libshim_ui.so'),

    ('vendor/lib/hw/android.hardware.thermal@2.0-impl.so', 'vendor/lib64/hw/android.hardware.thermal@2.0-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    ('vendor/lib/libalsautils-v32.so', 'vendor/lib64/libalsautils-v32.so'): blob_fixup()
        .fix_soname(),

    ('vendor/lib/hw/audio.primary.mediatek.so', 'vendor/lib64/hw/audio.primary.mediatek.so'): blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-v32.so')
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so')
        .replace_needed('libbinder.so', 'libbinder-v32.so')
        .add_needed('libstagefright_foundation-v33.so'),

    'system_ext/lib64/libimsma.so': blob_fixup()
         .replace_needed('libsink.so', 'libsink-mtk.so'),

    'system_ext/lib64/libsink-mtk.so': blob_fixup(),

    ('vendor/lib64/mt6789/lib3a.flash.so', 'vendor/lib64/mt6789/lib3a.ae.stat.so', 'vendor/lib64/mt6789/lib3a.sensors.flicker.so',
     'vendor/lib64/mt6789/lib3a.sensors.color.so', 'vendor/lib64/mt6789/libaaa_ltm.so', 'vendor/lib64/lib3a.ae.pipe.so',
     'vendor/lib64/libSQLiteModule_VER_ALL.so'): blob_fixup()
        .add_needed('liblog.so'),

         ('vendor/lib64/mt6789/libneuralnetworks_sl_driver_mtk_prebuilt.so', 'vendor/lib64/ese_spi_nxp.so', 'vendor/lib64/libstfactory-vendor.so',
     'vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib/libsysenv.so', 'vendor/lib64/libsysenv.so',
     'vendor/lib/libtflite_mtk.so', 'vendor/lib64/libtflite_mtk.so', 'vendor/lib64/nfc_nci_nxp_snxxx.so', 'vendor/bin/hw/android.hardware.usb@1.2-service-mediatekv2'): blob_fixup()
        .add_needed('libbase_shim.so'),

     'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

     'system_ext/bin/kpoc_charger': blob_fixup()
        .add_needed('libbinder_shim.so'),

     'vendor/lib64/mt6789/libmnl.so': blob_fixup()
	.add_needed('libcutils.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'X6833B',
    'infinix',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
