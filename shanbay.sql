/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : shanbay

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-05-03 17:53:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for checkin_record
-- ----------------------------
DROP TABLE IF EXISTS `checkin_record`;
CREATE TABLE `checkin_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `checkin_time` datetime NOT NULL COMMENT '第一次获取到打卡记录的时间，可能不准确',
  `checkin_note` varchar(255) DEFAULT NULL,
  `study_time` datetime NOT NULL,
  `study_word` int(11) NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for checkin_stat
-- ----------------------------
DROP TABLE IF EXISTS `checkin_stat`;
CREATE TABLE `checkin_stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `data_type` int(11) NOT NULL COMMENT '1-日；2-周；3-月；4-季；5-年',
  `data_date` datetime NOT NULL,
  `study_time` int(11) NOT NULL,
  `study_word` int(11) NOT NULL,
  `checkin_ratio` double DEFAULT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for crawl_record
-- ----------------------------
DROP TABLE IF EXISTS `crawl_record`;
CREATE TABLE `crawl_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_flag` int(11) NOT NULL COMMENT '0-失败；1-成功',
  `crawl_detail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` int(11) DEFAULT '0' COMMENT '0-未选择；1-男；2-女',
  `birthday` datetime DEFAULT NULL,
  `valid` int(1) NOT NULL DEFAULT '1' COMMENT '有效性：1-有效；0-无效',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `wechat_uid` varchar(255) DEFAULT NULL COMMENT '关联微信用户的uid',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
