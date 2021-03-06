/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : wechat

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-05-02 15:15:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mp_msg
-- ----------------------------
DROP TABLE IF EXISTS `mp_msg`;
CREATE TABLE `mp_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `to_user` varchar(255) NOT NULL,
  `from_user` varchar(255) NOT NULL,
  `msg_type` varchar(255) NOT NULL,
  `msg_id` varchar(255) NOT NULL,
  `content` varchar(255) DEFAULT NULL,
  `direction` int(1) NOT NULL DEFAULT '0' COMMENT '0-用户发送；1-公众平台发送',
  `msg_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
