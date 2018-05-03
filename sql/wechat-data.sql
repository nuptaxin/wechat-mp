/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : wechat

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-05-03 20:53:31
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
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mp_msg
-- ----------------------------
INSERT INTO `mp_msg` VALUES ('1', '1234', '444', 'text', 'xxxxxId', 'test233', '0', '2018-04-28 17:05:01', '2018-04-28 17:05:01');
INSERT INTO `mp_msg` VALUES ('2', '1234', '444', 'text', 'xxxxxId', 'test233', '0', '2018-04-28 17:05:55', '2018-04-28 17:05:55');
INSERT INTO `mp_msg` VALUES ('3', '1234', '444', 'text', 'xxxxxId', 'test233你好', '0', '2018-04-28 17:09:41', '2018-04-28 17:09:41');
INSERT INTO `mp_msg` VALUES ('4', '444', '1234', 'text', 'xxxxxId', '我现在还在开发中，还没有什么功能，您刚才说的是：test233你好', '1', '2018-04-28 17:09:41', '2018-04-28 17:09:41');
INSERT INTO `mp_msg` VALUES ('5', '1234', '444', 'text', 'xxxxxId', 'test233你好', '0', '2018-05-02 11:28:51', '2018-05-02 11:28:51');
INSERT INTO `mp_msg` VALUES ('6', '444', '1234', 'text', 'xxxxxId', '我现在还在开发中，还没有什么功能，您刚才说的是：test233你好', '1', '2018-05-02 11:28:51', '2018-05-02 11:28:51');
INSERT INTO `mp_msg` VALUES ('7', '1234', '444', 'text', 'xxxxxId', 'test233你好', '0', '2018-05-02 13:26:21', '2018-05-02 13:26:21');
INSERT INTO `mp_msg` VALUES ('8', '444', '1234', 'text', 'xxxxxId', '你似乎话里有话', '1', '2018-05-02 13:26:21', '2018-05-02 13:26:21');
INSERT INTO `mp_msg` VALUES ('9', '1234', '444', 'text', 'xxxxxId', 'test233你好', '0', '2018-05-02 13:26:38', '2018-05-02 13:26:38');
INSERT INTO `mp_msg` VALUES ('10', '444', '1234', 'text', 'xxxxxId', '你、你、你欺负人家，人家不依了。。。。。', '1', '2018-05-02 13:26:38', '2018-05-02 13:26:38');
INSERT INTO `mp_msg` VALUES ('11', '1234', '444', 'text', 'xxxxxId', 'test233你好', '0', '2018-05-02 13:27:24', '2018-05-02 13:27:24');
INSERT INTO `mp_msg` VALUES ('12', '444', '1234', 'text', 'xxxxxId', '和你聊天好开心', '1', '2018-05-02 13:27:24', '2018-05-02 13:27:24');
INSERT INTO `mp_msg` VALUES ('13', '1234', '444', 'text', 'xxxxxId', '?', '0', '2018-05-02 13:27:36', '2018-05-02 13:27:36');
INSERT INTO `mp_msg` VALUES ('14', '444', '1234', 'text', 'xxxxxId', '帮助菜单：\r\n1000-扇贝单词\r\n2000-天气预报', '1', '2018-05-02 13:27:36', '2018-05-02 13:27:36');
INSERT INTO `mp_msg` VALUES ('15', '1234', '444', 'text', 'xxxxxId', '？', '0', '2018-05-02 13:27:55', '2018-05-02 13:27:55');
INSERT INTO `mp_msg` VALUES ('16', '444', '1234', 'text', 'xxxxxId', '帮助菜单：\r\n1000-扇贝单词\r\n2000-天气预报', '1', '2018-05-02 13:27:55', '2018-05-02 13:27:55');
INSERT INTO `mp_msg` VALUES ('17', '1234', '444', 'text', 'xxxxxId', '?', '0', '2018-05-02 13:28:04', '2018-05-02 13:28:04');
INSERT INTO `mp_msg` VALUES ('18', '444', '1234', 'text', 'xxxxxId', '帮助菜单：\r\n1000-扇贝单词\r\n2000-天气预报', '1', '2018-05-02 13:28:04', '2018-05-02 13:28:04');
INSERT INTO `mp_msg` VALUES ('19', '1234', '444', 'text', 'xxxxxId', '你叫神魔', '0', '2018-05-02 13:28:29', '2018-05-02 13:28:29');
INSERT INTO `mp_msg` VALUES ('20', '444', '1234', 'text', 'xxxxxId', '雷都劈到我了，我能不叫吗？', '1', '2018-05-02 13:28:29', '2018-05-02 13:28:29');
INSERT INTO `mp_msg` VALUES ('21', '1234', '444', 'text', '6550853913226860148', '你叫神魔', '0', '2018-05-02 14:00:51', '2018-05-02 14:00:51');
INSERT INTO `mp_msg` VALUES ('22', '444', '1234', 'text', '6550853913226860148', '雷都劈到我了，我能不叫吗？', '1', '2018-05-02 14:00:52', '2018-05-02 14:00:52');
INSERT INTO `mp_msg` VALUES ('23', '1234', '444', 'text', '6550853913226860148', '你叫神ss魔', '0', '2018-05-02 15:44:47', '2018-05-02 15:44:47');
INSERT INTO `mp_msg` VALUES ('24', '444', '1234', 'text', '6550853913226860148', '比神还神噢～', '1', '2018-05-02 15:44:47', '2018-05-02 15:44:47');
INSERT INTO `mp_msg` VALUES ('25', '1234', '444', 'text', '6550853913226860148', '你叫神ss魔666', '0', '2018-05-02 15:56:13', '2018-05-02 15:56:13');
INSERT INTO `mp_msg` VALUES ('26', '444', '1234', 'text', '6550853913226860148', '比神还神噢～', '1', '2018-05-02 15:56:14', '2018-05-02 15:56:14');
INSERT INTO `mp_msg` VALUES ('27', '1234', '444', 'text', '6550853913226860148', '你叫神ss魔666', '0', '2018-05-02 16:06:53', '2018-05-02 16:06:53');
INSERT INTO `mp_msg` VALUES ('28', '444', '1234', 'text', '6550853913226860148', '我不叫污神，我叫chuchu', '1', '2018-05-02 16:06:54', '2018-05-02 16:06:54');
INSERT INTO `mp_msg` VALUES ('29', '1234', '444', 'text', 'xxxxxId', 'test233你好', '0', '2018-05-03 16:05:55', '2018-05-03 16:05:55');
INSERT INTO `mp_msg` VALUES ('30', '444', '1234', 'text', 'xxxxxId', '我也这么觉得哦', '1', '2018-05-03 16:05:56', '2018-05-03 16:05:56');
INSERT INTO `mp_msg` VALUES ('31', '1234', '444', 'text', 'xxxxxId', '你好', '0', '2018-05-03 16:06:31', '2018-05-03 16:06:31');
INSERT INTO `mp_msg` VALUES ('32', '444', '1234', 'text', 'xxxxxId', '好吧，你也好。', '1', '2018-05-03 16:06:31', '2018-05-03 16:06:31');
INSERT INTO `mp_msg` VALUES ('33', '1234', '444', 'text', 'xxxxxId', '你好', '0', '2018-05-03 18:27:07', '2018-05-03 18:27:07');
INSERT INTO `mp_msg` VALUES ('34', '444', '1234', 'text', 'xxxxxId', '你好耶～', '1', '2018-05-03 18:27:08', '2018-05-03 18:27:08');
INSERT INTO `mp_msg` VALUES ('35', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:18:38', '2018-05-03 20:18:38');
INSERT INTO `mp_msg` VALUES ('36', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:22:41', '2018-05-03 20:22:41');
INSERT INTO `mp_msg` VALUES ('37', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:29:37', '2018-05-03 20:29:37');
INSERT INTO `mp_msg` VALUES ('38', '444', '1234', 'text', 'xxxxxId', '', '1', '2018-05-03 20:29:37', '2018-05-03 20:29:37');
INSERT INTO `mp_msg` VALUES ('39', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:31:20', '2018-05-03 20:31:20');
INSERT INTO `mp_msg` VALUES ('40', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:32:32', '2018-05-03 20:32:32');
INSERT INTO `mp_msg` VALUES ('41', '444', '1234', 'text', 'xxxxxId', '任正信 55 321 1.0\r\n', '1', '2018-05-03 20:32:32', '2018-05-03 20:32:32');
INSERT INTO `mp_msg` VALUES ('42', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:35:48', '2018-05-03 20:35:48');
INSERT INTO `mp_msg` VALUES ('43', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:37:45', '2018-05-03 20:37:45');
INSERT INTO `mp_msg` VALUES ('44', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:38:30', '2018-05-03 20:38:30');
INSERT INTO `mp_msg` VALUES ('45', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:40:33', '2018-05-03 20:40:33');
INSERT INTO `mp_msg` VALUES ('46', '444', '1234', 'text', 'xxxxxId', '姓名 学习时长 学习单词数 打卡率\r\n任正信553211.0', '1', '2018-05-03 20:40:33', '2018-05-03 20:40:33');
INSERT INTO `mp_msg` VALUES ('47', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:41:32', '2018-05-03 20:41:32');
INSERT INTO `mp_msg` VALUES ('48', '444', '1234', 'text', 'xxxxxId', '姓名 学习时长 学习单词数 打卡率\r\n 任正信 55 321 1.0', '1', '2018-05-03 20:41:32', '2018-05-03 20:41:32');
INSERT INTO `mp_msg` VALUES ('49', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:43:05', '2018-05-03 20:43:05');
INSERT INTO `mp_msg` VALUES ('50', '444', '1234', 'text', 'xxxxxId', '姓名 学习时长 学习单词数 打卡率\r\n 任正信2 33 22 0.8\r\n 任正信 55 321 1.0', '1', '2018-05-03 20:43:05', '2018-05-03 20:43:05');
INSERT INTO `mp_msg` VALUES ('51', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:47:04', '2018-05-03 20:47:04');
INSERT INTO `mp_msg` VALUES ('52', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:47:46', '2018-05-03 20:47:46');
INSERT INTO `mp_msg` VALUES ('53', '444', '1234', 'text', 'xxxxxId', '姓名 学习时长 学习单词数 打卡率\r\n 任正信2 33 22 0.8\r\n 任正信 55 321 1.0', '1', '2018-05-03 20:47:46', '2018-05-03 20:47:46');
INSERT INTO `mp_msg` VALUES ('54', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:48:12', '2018-05-03 20:48:12');
INSERT INTO `mp_msg` VALUES ('55', '444', '1234', 'text', 'xxxxxId', '姓名 学习时长 学习单词数 打卡率\r\n 任正信 55 321 1.0\r\n 任正信2 33 22 0.8', '1', '2018-05-03 20:48:12', '2018-05-03 20:48:12');
INSERT INTO `mp_msg` VALUES ('56', '1234', '444', 'text', 'xxxxxId', '1003', '0', '2018-05-03 20:50:30', '2018-05-03 20:50:30');
INSERT INTO `mp_msg` VALUES ('57', '444', '1234', 'text', 'xxxxxId', '名次 姓名 学习时长 学习单词数 打卡率\r\n 1 任正信 55 321 1.0\r\n 2 任正信2 33 22 0.8', '1', '2018-05-03 20:50:30', '2018-05-03 20:50:30');

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

-- ----------------------------
-- Records of user_info
-- ----------------------------
