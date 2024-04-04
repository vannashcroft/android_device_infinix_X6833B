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

# Inherit some common  stuff
$(call inherit-product, vendor/superior/config/common.mk)
TARGET_BOOT_ANIMATION_RES := 1080

## Device identifier. This must come after all inclusions
PRODUCT_DEVICE := X6833B
PRODUCT_NAME := superior_X6833B
PRODUCT_BRAND := INFINIX
PRODUCT_MODEL := INFINIX NOTE 30
PRODUCT_MANUFACTURER := Infinix
BUILD_FINGERPRINT := Infinix/X6833B-GL/Infinix-X6833B:13/TP1A.220624.014/240103V3275:user/release-keys
PRIVATE_BUILD_DESC="sys_tssi_64_armv82_infinix-user 13 TP1A.220624.014 377398 release-keys"
# Maintainer Stuff
MAINTAINER := "RAFI_AQ"
BUILD_WITH_GAPPS := true
PRODUCT_GMS_CLIENTID_BASE := android-transsion
