CREATE TABLE `blog_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sort` int(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `photo_path` varchar(250) NOT NULL DEFAULT '',
  `time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL DEFAULT '0',
  `author` varchar(100) NOT NULL,
  `content` mediumtext NOT NULL,
  `click` int(20) NOT NULL DEFAULT '10',
  `summary` text NOT NULL,
  `keywords` varchar(100) DEFAULT NULL COMMENT '文章关键字',
  `is_delete` int(11) NOT NULL DEFAULT '0',
  `nav` int(11) NOT NULL,
  `state` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
