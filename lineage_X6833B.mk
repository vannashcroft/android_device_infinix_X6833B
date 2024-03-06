#
# Copyright (C) 2023 LineageOS
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from device makefile
$(call inherit-product, device/infinix/X6833B/device.mk)

# Inherit some common crDroid stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)
TARGET_BOOT_ANIMATION_RES := 1080

## Device identifier. This must come after all inclusions
PRODUCT_DEVICE := X6833B
PRODUCT_NAME := aosp_X6833B
PRODUCT_BRAND := Infinix
PRODUCT_MODEL := NOTE 30
PRODUCT_MANUFACTURER := Infinix
TARGET_FACE_UNLOCK_SUPPORTED := true
TARGET_SUPPORTS_QUICK_TAP := true
TARGET_ENABLE_BLUR := true
WITH_GMS := true
BUILD_FINGERPRINT :=Infinix/TSSI/FULL-64-ARMV82:13/TP1A.220624.014/230712V1259:user/release-keys
PRIVATE_BUILD_DESC="sys_tssi_64_armv82_infinix-user 13 TP1A.220624.014 377398 release-keys"
WITH_GMS := true
TARGET_CORE_GMS := true
PRODUCT_GMS_CLIENTID_BASE := android-transsion
