CREATE DATABASE IF NOT EXISTS stock
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
;

USE stock;


CREATE TABLE IF NOT EXISTS market (
	id VARCHAR(10) NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
)
COMMENT='市場類別'
ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS industry (
	market_id VARCHAR(10) NOT NULL COMMENT '市場類別的id',
	id VARCHAR(10) NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (`market_id`,`id`) USING BTREE
)
COMMENT='產業類別'
 ENGINE=InnoDB4;

CREATE TABLE IF NOT EXISTS company (
	id INT NOT NULL AUTO_INCREMENT,
	stock_code VARCHAR(20) NOT NULL COMMENT '股票代碼',
	company_name VARCHAR(256) NOT NULL,
	short_name VARCHAR(256) NOT NULL COMMENT '簡稱',
	market_id VARCHAR(10) NOT NULL COMMENT '市場類別的id',
	industry_id VARCHAR(10) NOT NULL COMMENT '產業類別的id',
	
	founding_date DATE  NULL COMMENT '成立日期',
	ipo_date DATE  NULL COMMENT '上市日期',
	
	source_time DATETIME NOT NULL COMMENT '資料日期',
	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP() COMMENT '更新時間',
	PRIMARY KEY (id)
)
COMMENT='公司資料'
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS minute_price_2330_2024 (
	source_time DATETIME NOT NULL COMMENT '資料來源的時間',
	`open` DECIMAL(6,4) NOT NULL COMMENT '開盤價',
	high DECIMAL(6,4) NOT NULL COMMENT '最高價',
	low DECIMAL(6,4) NOT NULL COMMENT '最低價',
	`close` DECIMAL(6,4) NOT NULL COMMENT '收盤價',
	`volume` BIGINT(6,4) NOT NULL COMMENT '交易量',
	`adj_close` DECIMAL(6,4) NOT NULL COMMENT '調整後收盤價',
	
	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (source_time)
)
COMMENT='2330在2024年的每5秒收盤價'
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS day_price_2330 (
	source_time DATETIME NOT NULL COMMENT '資料來源的時間',
	`open` DECIMAL(6,4) NOT NULL COMMENT '開盤價',
	high DECIMAL(6,4) NOT NULL COMMENT '最高價',
	low DECIMAL(6,4) NOT NULL COMMENT '最低價',
	`close` DECIMAL(6,4) NOT NULL COMMENT '收盤價',
	`volume` BIGINT(6,4) NOT NULL COMMENT '交易量',
	`adj_close` DECIMAL(6,4) NOT NULL COMMENT '調整後收盤價',

	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (source_time)
)
COMMENT='2024年的每天收盤價'
ENGINE=InnoDB;




CREATE TABLE IF NOT EXISTS observe_group(
	id INT NOT NULL AUTO_INCREMENT,
--    user_id INT INT NOT NULL,
	name VARCHAR(255) NOT NULL COMMENT '條件名稱',
	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (id)
)
COMMENT='觀察的條件群組'
ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS observe_condition(
	id INT NOT NULL AUTO_INCREMENT,
	condi_type int NOT NULL COMMENT '條件類型',
	condi_name VARCHAR(255) NOT NULL COMMENT '條件名稱',
	remark VARCHAR(255) NOT NULL COMMENT '備註',
	observe_group_id INT NOT NULL COMMENT '觀察的群組id',
	
	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (id)
)
COMMENT='要觀察的條件'
ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS `user`(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL,
	account VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL,
	email VARCHAR(40) NOT NULL,
	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (id)
)


CREATE TABLE IF NOT EXISTS user_stock_group(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL COMMENT '條件名稱',
	user_id INT NOT NULL ,

	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (id)
)
COMMENT='使用者的股票群組'
ENGINE=InnoDB

CREATE TABLE IF NOT EXISTS stock_group(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL COMMENT '條件名稱',

	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (id)
)
COMMENT='股票群組'
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS stock_group_mapping(
	stock_group_id INT NOT NULL COMMENT '股票群組的id',
	company_id INT NOT NULL COMMENT '公司id',

	update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),

	PRIMARY KEY (stock_group_id, stock_id)
)
COMMENT='股票群組與股票的對應'
ENGINE=InnoDB;