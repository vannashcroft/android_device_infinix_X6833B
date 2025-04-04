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
        
    'vendor/bin/hw/android.hardware.vibrator-service.mediatek': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
        
    'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
        .replace_needed('android.hardware.power-V2-ndk_platform.so', 'android.hardware.power-V2-ndk_platform.so'),
        
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
}  # fmt: skip

module = ExtractUtilsModule(
    'X6833B',
    'infinix',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
